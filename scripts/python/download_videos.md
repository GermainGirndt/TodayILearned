### Install

```
pip install -U yt-dlp
```

### Use

ba = best quality

### Site

```
yt-dlp --format "bv*+ba/b" https://www.website.com
```

### With Cookies

```
yt-dlp --cookies-from-browser safari https://www.website.com/
```

For using in Photos, convert to .m4v:

- Name: VIDEO – H.264 + MP3 (MP4)
- Customize:
  - Video: H.264
  - Audio Codec: MPEG 4 Audio (AAC)

### Convert to iOS friendly format:

```
ffmpeg -i input.mp4 \
  -c:v libx264 -profile:v high -level 4.2 \
  -pix_fmt yuv420p \
  -movflags +faststart \
  -c:a aac -b:a 128k \
  output_ios.mp4
```

Notes:
Re-encodes video as H.264/AVC, with compatible (i) profile, (ii) pixels and (iii) audio formats.
