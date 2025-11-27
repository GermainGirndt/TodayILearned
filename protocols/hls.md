# 🎥 Introduction to HLS (HTTP Live Streaming)

**HLS (HTTP Live Streaming)** is a media-streaming protocol created by **Apple** for delivering audio and video over the internet.
It works by splitting video into small files (“segments”) and delivering them over standard **HTTP/HTTPS**.

It is widely used for live broadcasts, streaming platforms, and adaptive streaming.

---

## 🧩 How HLS Works

### 1. **Segmented Media**

Video is encoded and split into small chunks, typically **2–6 seconds** long:

- `.ts` segments (MPEG-TS format)
- or `.m4s` segments (fMP4) in modern Low-Latency HLS

### 2. **Playlist File (`.m3u8`)**

A playlist describes the order of segments.

Example:

```m3u
#EXTM3U
#EXTINF:4.0,
segment0001.ts
#EXTINF:4.0,
segment0002.ts
```

### 3. **HTTP Delivery**

A video player downloads:

1. the `.m3u8` playlist
2. the listed media segments

…using standard **HTTP/HTTPS**.

### 4. **Live Streaming**

For live content, the `.m3u8` playlist is continuously updated as new segments are produced.

---

## ⭐ Key Features of HLS

| Feature                    | Description                                                            |
| -------------------------- | ---------------------------------------------------------------------- |
| **Adaptive Bitrate (ABR)** | Automatically adjusts video quality based on network conditions.       |
| **Uses Standard HTTP**     | No special streaming server required; works with CDNs and web servers. |
| **Firewall-friendly**      | Uses ports 80/443.                                                     |
| **Apple Native Support**   | Works out of the box on iOS, macOS, Safari.                            |
| **Supports Live & VOD**    | Suitable for both real-time streaming and stored content.              |

---

## 🔀 Adaptive Bitrate (ABR) Streaming

HLS commonly uses a **master playlist** that points to multiple bitrate variants:

```
master.m3u8
├─ 360p.m3u8
├─ 720p.m3u8
└─ 1080p.m3u8
```

Players dynamically switch between these based on bandwidth and device capabilities.

---

## 🧪 Using HLS with FFmpeg

Your command:

```bash
ffmpeg -i "https://your-hls-url/playlist.m3u8" -c copy output.mp4
```

What FFmpeg does:

1. Downloads the `.m3u8` playlist
2. Fetches all the `.ts` segment files
3. Concatenates them
4. Remuxes into an `.mp4` container
5. **No re-encoding** because of `-c copy`

---

## 📌 When to Use HLS

- Live sports and events
- OTT streaming platforms
- Mobile-friendly video streaming
- CDN-optimized delivery
- Scalable live or VOD services
