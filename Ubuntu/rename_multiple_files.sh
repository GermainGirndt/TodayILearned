old_extension="webm"
new_extension="mp4"

for old_full_filename in *.$old_extension; do
    filename=$(basename "$old_full_filename" ".$old_extension")

    full_filename="$filename.$new_extension"
    echo "$filename"
    echo "$old_full_filename"
    echo "$full_filename"

    echo ""

    #mv "$old_full_filename" "$full_filename"
done