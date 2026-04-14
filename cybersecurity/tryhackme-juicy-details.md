brew install lnav

### Feroxbuster

feroxbuster is a fast web content discovery tool used in pentesting and CTFs.
It brute-forces web servers to find:
hidden files
directories
backup files
admin panels
APIs
Basically: it discovers things not linked on the website.

```
feroxbuster -u http://192.168.10.4 -w /usr/share/wordlists/dirb/common.txt
```

It will scan thousands of paths quickly.

To find:
admin panels
upload pages
backup files (.bak, .zip)
config files
web shells
forgotten directories

### Backup files

###### 1

2h54m57s│access.log┌::ffff:192.168.10.5 - - [11/Apr/2021:11:08:29 +0200] "GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0" 200 1924 "-" "-" │

`/nice ports,/Trinity.txt.bak` is the appache backup for `/usr/share/doc/nmap/nselib/data/http-default-accounts-fingerprints.lua`

###### 2

Sun Apr 11 09:35:45 2021 [pid 8154] [ftp] OK DOWNLOAD: Client "::ffff:192.168.10.5", "/www-data.bak", 2602 bytes, 544.81Kbyte/sec

download www-data.bak with sshd credentials

### SQLMap

Automated tool for exploring sql vulnerabilities automatically (SQl injection of multiple forms)

#### SQL Injection Done

    1h54m21s││::ffff:192.168.10.5 - - [11/Apr/2021:11:32:51 +0200] "GET /rest/products/search?q=qwert%27))%20UNION%20SELECT%20id,%20email,%20password,%20%274%27,%│
