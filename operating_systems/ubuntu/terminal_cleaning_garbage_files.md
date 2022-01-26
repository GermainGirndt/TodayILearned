# Terminal - Cleaninig Garbage Files within subfolders


# Create a directory for the garbage files to be moved in

```
for dir in *; do mkdir "$dir/Descartaveis"; done
```

# Move all files that don't have the specified name/extension

```
for dir in *; do find "./$dir/" -type f ! -name "*.mp4" -exec mv -t "./$dir/Descartaveis/" {} \+; done
```
