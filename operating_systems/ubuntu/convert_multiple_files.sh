webmTOmp4 () {
  ffmpeg -i "$1".webm -qscale 0 "$1".mp4
}   

extension=".webm"
for file in ./*.webm; do
    filename=$(basename "$file" "$extension")
    echo "$filename"
    webmTOmp4 "$filename"
    

    #webmTOmp4 $filename
done