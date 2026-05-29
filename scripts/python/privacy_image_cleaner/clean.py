#!/usr/bin/env python3
from PIL import Image, ImageFilter, ImageDraw
from pathlib import Path
import argparse
import subprocess
import random
import numpy as np

from PIL import Image, ImageOps


def run(cmd):
    return subprocess.run(cmd, check=True, text=True, capture_output=True)


def strip_metadata_with_exiftool(path: Path) -> None:
    run([
        "exiftool",
        "-overwrite_original",
        "-all=",
        "-EXIF:all=",
        "-IPTC:all=",
        "-XMP:all=",
        "-JUMBF:all=",   # C2PA/Content Credentials where supported
        "-PNG:all=",
        str(path),
    ])


def reencode_without_metadata(src: Path, dst: Path, quality: int = 85) -> None:
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        if dst.suffix.lower() in [".jpg", ".jpeg"]:
            im = im.convert("RGB")
            im.save(dst, "JPEG", quality=quality, optimize=True)
        elif dst.suffix.lower() == ".png":
            im.save(dst, "PNG", optimize=True)
        else:
            raise ValueError("Output must be .jpg/.jpeg or .png")


def verify(path: Path) -> None:
    print("\nMetadata check:")
    result = run(["exiftool", "-a", "-G1", "-s", str(path)])
    suspicious = [
        "EXIF", "IPTC", "XMP", "JUMBF", "C2PA",
        "Software", "Make", "Model", "GPS",
        "Creator", "Description", "Parameters"
    ]
    lines = [
        line for line in result.stdout.splitlines()
        if any(term.lower() in line.lower() for term in suspicious)
    ]
    print("\n".join(lines)
          if lines else "No obvious EXIF/IPTC/XMP/C2PA/PNG text metadata found.")


def pixelwise_random_transform(
    src: Path,
    dst: Path,
    transformation_range: list[int],
) -> None:
    """
    Randomly transforms RGB pixel values across the whole image.

    Each RGB channel value is independently changed by a random integer
    sampled uniformly from the inclusive range [min, max].

    Example:
        transformation_range = [-2, 2]
        -> equal probability for: -2, -1, 0, +1, +2

    Values are clipped to the valid RGB range [0, 255].

    Args:
        src: Source image path.
        dst: Destination image path.
        transformation_range: [min, max] inclusive.
    """
    if len(transformation_range) != 2:
        raise ValueError(
            "transformation_range must contain exactly two values: [min, max]"
        )

    min_delta, max_delta = transformation_range

    if min_delta > max_delta:
        raise ValueError(
            "transformation_range[0] must be <= transformation_range[1]")

    # Load image and force RGB mode
    img = Image.open(src).convert("RGB")

    # Convert to int16 to avoid uint8 overflow during arithmetic
    pixels = np.array(img, dtype=np.int16)

    # Generate random per-channel changes with equal probability
    deltas = np.random.randint(
        min_delta,
        max_delta + 1,  # inclusive upper bound
        size=pixels.shape,
        dtype=np.int16,
    )

    # Apply transformation and clip to valid RGB range
    transformed = np.clip(pixels + deltas, 0, 255).astype(np.uint8)

    # Save output
    out_img = Image.fromarray(transformed, mode="RGB")
    out_img.save(dst)


def apply_focus_blur(
    src: Path,
    dst: Path,
    focus_center: tuple[int, int],
    focus_radius: tuple[int, int],
    blur_intensity: float = 6.0,
    transition: float = 40.0,
) -> None:
    """
    Simulate camera-like shallow depth of field by keeping an elliptical
    region sharp while progressively blurring surrounding areas.

    The function creates:
    - a sharp version of the image
    - a blurred version of the image
    - a soft mask defining the focus region

    The result blends the focused region into a blurred background,
    approximating a shallow depth-of-field effect.

    Args:
        src:
            Path to the source image.

        dst:
            Path where the processed image will be saved.

        focus_center:
            (x, y) coordinates of the focus center in image pixels.

            Coordinate system:
            - (0, 0) is the top-left corner
            - x increases to the right
            - y increases downward

            Example:
                (500, 300)

        focus_radius:
            (radius_x, radius_y) of the focused elliptical region in pixels.

            Example:
                (200, 150)

            Meaning:
                - radius_x controls horizontal focus extent
                - radius_y controls vertical focus extent

            The ellipse must fully fit inside the image canvas.

        blur_intensity:
            Gaussian blur radius applied to the out-of-focus region.

            Typical values:
                0.2 - 1.0 -> subtle blur
                2.0 - 5.0 -> moderate blur
                >5.0      -> strong blur

            Must be >= 0.

        transition:
            Softness of the focus boundary in pixels.

            Higher values create smoother transitions between
            focused and blurred regions.

            Typical values:
                10 - 30 -> sharper focus edge
                30 - 80 -> smoother, more camera-like transition

            Must be >= 0.

    Raises:
        ValueError:
            If:
            - blur_intensity < 0
            - transition < 0
            - focus_center lies outside image bounds
            - focus_radius contains negative values
            - focus ellipse would extend outside the image

    Returns:
        None
    """
    if blur_intensity < 0:
        raise ValueError("blur_intensity must be >= 0")

    if transition < 0:
        raise ValueError("transition must be >= 0")

    img = Image.open(src).convert("RGB")
    width, height = img.size

    cx, cy = focus_center
    rx, ry = focus_radius

    # Validate focus center
    if not (0 <= cx < width):
        raise ValueError(
            f"focus_center x-coordinate ({cx}) is outside image bounds "
            f"[0, {width - 1}]"
        )

    if not (0 <= cy < height):
        raise ValueError(
            f"focus_center y-coordinate ({cy}) is outside image bounds "
            f"[0, {height - 1}]"
        )

    # Validate radius
    if rx < 0 or ry < 0:
        raise ValueError(
            "focus_radius values must be >= 0 "
            f"(received: ({rx}, {ry}))"
        )

    # Maximum allowable radius from center to canvas edge
    max_rx = min(cx, width - 1 - cx)
    max_ry = min(cy, height - 1 - cy)

    if rx > max_rx:
        raise ValueError(
            f"focus_radius x ({rx}) exceeds canvas size from center. "
            f"Maximum allowed x radius at center ({cx}, {cy}) "
            f"is {max_rx}"
        )

    if ry > max_ry:
        raise ValueError(
            f"focus_radius y ({ry}) exceeds canvas size from center. "
            f"Maximum allowed y radius at center ({cx}, {cy}) "
            f"is {max_ry}"
        )

    # Create blurred image
    blurred = img.filter(
        ImageFilter.GaussianBlur(radius=blur_intensity)
    )

    # Create focus mask
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)

    # White region = focused area
    draw.ellipse(
        (
            cx - rx,
            cy - ry,
            cx + rx,
            cy + ry,
        ),
        fill=255,
    )

    # Smooth transition between focus and blur
    mask = mask.filter(
        ImageFilter.GaussianBlur(radius=transition)
    )

    # Blend sharp + blurred image
    result = Image.composite(img, blurred, mask)

    result.save(dst)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("-o", "--output")
    parser.add_argument("--quality", type=int, default=85)
    args = parser.parse_args()

    src = Path(args.input)
    if not src.exists():
        raise FileNotFoundError(src)

    original_ext = src.suffix.lower()
    first_encoding_ext = ".png" if original_ext in [
        ".jpg", ".jpeg"] else ".jpg"

    # step 1 – reencode without metadata and strip metadata
    reencoded_without_metadata = src.with_name(
        src.stem + "_step_1_reencoded_without_metadata" + first_encoding_ext)
    reencode_without_metadata(src, reencoded_without_metadata, args.quality)
    strip_metadata_with_exiftool(reencoded_without_metadata)

    # step 2 – apply pixelwise random transform to remove residual metadata in pixel values
    pixelwise_transformed = src.with_name(
        src.stem + "_step_2_pixelwise_transformed" + first_encoding_ext)
    pixelwise_random_transform(
        reencoded_without_metadata, pixelwise_transformed, [-5, 14])

    # step 3 – reencode + new metadata strip
    reencoded = Path(args.output) if args.output else src.with_name(
        src.stem + "_step_3_reencoded" + original_ext)
    reencode_without_metadata(pixelwise_transformed, reencoded, args.quality)
    strip_metadata_with_exiftool(reencoded)

    # step 4
    blurred = Path(args.output) if args.output else src.with_name(
        src.stem + "_step_4_blurred" + original_ext)
    apply_focus_blur(
        src=reencoded,
        dst=blurred,
        focus_center=(300, 400),
        focus_radius=(280, 380),
        blur_intensity=1.0,
        transition=50.0,
    )

    # step 5
    print("Before cleaning:")
    verify(src)
    print("After cleaning:")
    verify(blurred)
    print(f"\nSaved: {blurred}")


if __name__ == "__main__":
    main()
