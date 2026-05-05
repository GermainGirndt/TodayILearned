# GhostScript for PDF Compression

## Install

```
brew install ghostscript
```

## Standard Execution

### Choose one PDF Quality

```
/screen    smallest, lowest quality
/ebook     medium quality, good for sharing
/printer   higher quality
/prepress  high quality, usually larger
/default   Ghostscript default
```

### Execute Script

```
gs -sDEVICE=pdfwrite \
  -dCompatibilityLevel=1.4 \
  -dPDFSETTINGS=/ebook \
  -dNOPAUSE -dQUIET -dBATCH \
  -sOutputFile=compressed.pdf \
  input.pdf
```

## Custom DPI Settings

### Reference Presets

| Preset      | Color images | Grayscale images | Monochrome / 1-bit images | Downsampling enabled? |
| ----------- | -----------: | ---------------: | ------------------------: | --------------------- |
| `/screen`   |       72 dpi |           72 dpi |                   300 dpi | yes                   |
| `/ebook`    |      150 dpi |          150 dpi |                   300 dpi | yes                   |
| `/printer`  |      300 dpi |          300 dpi |                  1200 dpi | no                    |
| `/prepress` |      300 dpi |          300 dpi |                  1200 dpi | no                    |
| `/default`  |       72 dpi |           72 dpi |                   300 dpi | no                    |

### Custom Command

```
gs -sDEVICE=pdfwrite \
  -dCompatibilityLevel=1.4 \
  -dNOPAUSE -dQUIET -dBATCH \
  -dDownsampleColorImages=true \
  -dColorImageResolution=120 \
  -dDownsampleGrayImages=true \
  -dGrayImageResolution=120 \
  -dDownsampleMonoImages=true \
  -dMonoImageResolution=150 \
  -sOutputFile=compressed.pdf \
  input.pdf
```
