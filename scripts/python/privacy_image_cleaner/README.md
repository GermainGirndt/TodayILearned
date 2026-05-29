# Privacy Image Cleaner – Cleaning Photos, Camera, Metadata, AI Generation marks

### Step 1: Strip every type of metadata

The first and most important step. If you only do one thing, do this — it handles the Layer 1 detection that accounts for the majority of AI labels in practice.

You need to remove all of the following, not just some of them:

EXIF data — camera make, model, software field, GPS coordinates, timestamps, editing history
IPTC fields — source, creator, description, keywords
XMP metadata — the XML-based metadata that Adobe products use, which includes the "Made with AI" indicators
C2PA manifests — the cryptographically signed provenance blocks, which are the most important thing to remove in 2026. Content Credentials removal is covered in depth in our C2PA guide.
PNG text chunks — if your image is a PNG from Stable Diffusion, the generation parameters are stored in these chunks and must be removed separately from EXIF
Embedded thumbnails — many EXIF-cleaning tools forget that images contain small preview thumbnails which themselves have metadata

### Step 2: Change the pixels

Randomly changes the pixel values across the whole image (equal probability of changing a RGB value for a given pixel to -2, -1, 0. +1, +2). Remember to respect the 0-255 RGB limits.

### Step 3: Re-encode as a fresh file

After stripping metadata and modifying pixels, save the result as to a different format (JPEG -> PNG; PNG -> JPEG) to remove format-specific metadata, which might carry other informations.

Then, re-encoding to the original format using a smaller quality level (e.g. 85-90%)

### Step 4: Verify the metadata

Do not skip this step. There are two quick checks you can run:
EXIF, XMP, C2PA manifest, PNG text chunks.
