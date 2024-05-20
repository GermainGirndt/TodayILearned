# Download Videos using HLS (HTTPS Live Streaming)

- Example 1

```
ffmpeg -i "https://your-hls-url/playlist.m3u8" -c copy output.mp4
```

- Example 2:

The nextwork tab streams the following:
https://some-domain/deliveries/7601e1770ae1b2c5ebd5a7b95bde455ac2a41324acxs.m3u8/seg-1-v1-a1.ts

Each .ts file is a fragment of the actual video ID 7601e1770ae1b2c5ebd5a7b95bde455ac2a41324acxs.m3u8. You can then run:

```
ffmpeg -i "https://embed-cloudfront.wistia.com/deliveries/4401e1770ae1b2c5ebd5a7b95bde455ac2a71e75.m3u8" -c copy video_name.mp4
```

### Explanation

.ts stands stands for Transport Stream. More specifically, MPEG-2 Transport Stream files, which are used in broadcasting and streaming applications to deliver video and audio data.

Some other extensions:

Master Playlist (.m3u8): Points to different versions of the stream, often at different bitrates, resolutions, and sometimes even different languages or captions. Enables adaptive bitrate streaming (ABR), allowing the player to dynamically switch between different streams to provide the best possible viewing experience without buffering.

Media Playlist (.m3u8): Lists the individual .ts files. This playlist contains the actual URLs to the individual video segments and provides the necessary information for the player to download and play these segments in the correct order.

Segment Files (.ts): Contain the actual video and audio data.

#### Master Playslist

For example, the master playlist might look like this:

```
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=1280000
https://example.com/low.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=2560000
https://example.com/mid.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=5120000
https://example.com/high.m3u8
```

#### Media Playlist

```
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:3
#EXTINF:10.000,
https://embed-cloudfront.wistia.com/deliveries/4401e1770ae1b2c5ebd5a7b95bde455ac2a71e75.m3u8/seg-1-v1-a1.ts
#EXTINF:10.000,
https://embed-cloudfront.wistia.com/deliveries/4401e1770ae1b2c5ebd5a7b95bde455ac2a71e75.m3u8/seg-2-v1-a1.ts
#EXTINF:10.000,
https://embed-cloudfront.wistia.com/deliveries/4401e1770ae1b2c5ebd5a7b95bde455ac2a71e75.m3u8/seg-3-v1-a1.ts
```

You can use ffmpeg to download and combine these .ts files into a single video file by providing the .m3u8 URL:

### Download with best quality

To ensure that you are downloading the best quality version of the stream, you can use the -map option to select the specific variant or the highest quality stream. Here's how you can do it:

1. Check the Available Streams:

First, inspect the master playlist to identify the available streams and their qualities. You can do this by opening the .m3u8 URL in a browser or using a tool like ffprobe to list the available variants.

ffprobe "https://example.com/master.m3u8"

2. Select the Best Quality Stream:

Once you have identified the highest quality stream, you can specify it using ffmpeg.
Here’s an example of how you might use ffmpeg to ensure you’re downloading the best quality:

```
# Using ffmpeg to download the best quality
ffmpeg -i "https://example.com/master.m3u8" -map p:0 -c copy output.mp4
```

-map p:0 tells ffmpeg to use the first program (variant) listed in the master playlist. This might not always be the highest quality, so it’s better to inspect the playlist and choose accordingly.
