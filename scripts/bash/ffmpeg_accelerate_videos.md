## Summary

- H.264 CRF 18: big files, excellent quality, extremely compatible, easy to play.
- HEVC: smaller files at similar or better quality, but harder to decode and not universally supported.

### CPU

### CRF 18 Excellent (visually lossless)

CRF 18 in H.264 is a constant-quality setting that produces very high-quality video, usually close to visually lossless. It uses an older codec (H.264) that is widely supported and easy to decode, but it is less efficient, meaning it needs a higher bitrate (larger file size) to reach that level of quality. The output is predictable, consistent, and plays smoothly almost everywhere.

```
ffmpeg -i input.mp4 -filter_complex "[0:v]setpts=PTS/1.03[v];[0:a]atempo=1.03[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset slow -c:a aac -b:a 192k output.mp4
```

### GPU

##### HEVC (H.265) hardware encode (better compression, but more decoding; better quality):

HEVC (H.265) is a newer, more advanced codec designed to compress video more efficiently. It can deliver the same or better visual quality as H.264 using fewer bits, resulting in noticeably smaller file sizes. However, quality depends more on the encoder (hardware or software), and hardware encoders are sometimes less precise than H.264 software encoders. HEVC also requires more decoding power and isn’t supported by all devices or browsers.

```
ffmpeg -i input.mp4 \
-filter_complex "[0:v]setpts=PTS/1.03[v];[0:a]atempo=1.03[a]" \
-map "[v]" -map "[a]" \
-c:v hevc_videotoolbox -q:v 30 \
-c:a aac -b:a 192k \
output_hevc.mp4

```
