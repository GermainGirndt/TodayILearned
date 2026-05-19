# Compare number of files

```
find "directory_name" -type f | wc -l

find "directory_name--2" -type f | wc -l
```

### Compare Bytes

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
