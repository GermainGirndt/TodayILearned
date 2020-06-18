# Add cover to audio

```
ffmpeg -i in.mp3 -i test.png -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" out.mp3
```


# Convert audio to video

```
ffmpeg -i 01_-_Tiago_Tofani_-_Introduction.mp3 -i 00_-__Foto\ de\ Capa.jpg -c:a copy -c:v copy -map 0:0 -map 1:0 -id3v2_version 3 -metadata:s:v title="The Mirror" -metadata:s:v comment="Cover (front)" 01_-_Tiago_Tofani_-_Introduction.mp4
```


# Loop through mp3 files and convert it to .mp4 files, adding cover photo to it.

* **i** - inputed mp3 file
* **SUBSTRING** - inputed file string refactored to mp4
* **00_-__Foto\ de\ Capa.jpg** - cover photo added to all videos

```
for i in *.mp3; do echo ; INPUT=$i; SUBSTRING=$(echo $INPUT| cut -d'.' -f 1); echo $SUBSTRING.mp4; ffmpeg -i $i -i 00_-__Foto\ de\ Capa.jpg -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" $SUBSTRING.mp4; done
```