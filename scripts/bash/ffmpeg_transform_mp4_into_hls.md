### Preparing Directories

```
mkdir -p hls
```

### Converting video into different resolutions:

```
ffmpeg -i sample.mp4 \
-filter_complex "[0:v]split=3[vhd][vmd][vsd]; \
[vhd]scale=1920:1080[vhdout]; \
[vmd]scale=1280:720[vmdout]; \
[vsd]scale=854:480[vsdout]" \
-map "[vhdout]" -map 0:a \
-map "[vmdout]" -map 0:a \
-map "[vsdout]" -map 0:a \
-var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" \
-hls_time 6 \
-hls_playlist_type vod \
-master_pl_name master.m3u8 \
-hls_segment_filename "hls/%v/%03d.ts" \
hls/%v/index.m3u8
```
