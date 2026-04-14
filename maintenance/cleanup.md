### Clean Up – Cleaning Files

Use the command below to investigate the folders occuping the most size.

```
sudo du -h -d 1 ~/ | sort -hr | head -20
```

- For more granuality:

```
 du -h -d 2 ~/ | sort -hr | head -30
```
