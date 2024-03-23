# Formatting to FAT32

To format your SSD as FAT32 using the Terminal on your Mac, you'll follow a similar process but with a command specific to creating a FAT32 file system. Here's how you can do it:

```bash
diskutil list
```

```bash
diskutil unmountDisk /dev/diskX
```

```bash
diskutil randomDisk 2 /dev/diskXµ
# override the disk with random data two times
```

```bash
diskutil eraseDisk FAT32 YourVolumeName MBRFormat /dev/diskX
# volume name in one word, max 11 characters
```

```bash
diskutil list
```
