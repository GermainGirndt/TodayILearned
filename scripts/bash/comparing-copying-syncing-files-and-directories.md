# Compare number of files

```
find "directory_name" -type f | wc -l

find "directory_name--2" -type f | wc -l
```

### Compare Stored Bytes

```
du -sk "directory_name"

du -sk "directory_name--2"
```

### Compare Checksums

```
find "directory_name" \
-type f -print0 | xargs -0 shasum | sort > hashes1.txt

find "directory_name--2" \
-type f -print0 | xargs -0 shasum | sort > hashes2.txt

cut -d ' ' -f 1 hashes1.txt | sort > hashes1_only.txt
cut -d ' ' -f 1 hashes2.txt | sort > hashes2_only.txt

diff hashes1_only.txt hashes2_only.txt
```

### Copy files from one to other directory, while showing progress and allowing stop/resuming

- `rsync` — copy/synchronize the two directory trees.
- `-a` — “archive mode”: recursively copies folders and tries to preserve metadata such as modification times, permissions, symlinks, etc.
- `--partial` — if a file is interrupted halfway through, keep the partial file instead of throwing it away.
- `--info=progress2` shows the progress for the total process

```
# note: showing just one progress (ensure version >3)
rsync -a --partial --info=progress2 \
  "dir1" \
  "dir2"
```

### Compare files in two different directories (e.g. after copying dir1 -> dir2)

```
rsync -rnc --itemize-changes \
  "dir1" \
  "dir2"
```
