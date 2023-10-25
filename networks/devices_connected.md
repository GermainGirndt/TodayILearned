# Check for devices connected in the same network (private ip addreess)

# Tools

### Angry Ip Scanner

```
https://angryip.org
```

Is a network scanner that allows users to scan IP addresses and ports to gather information about network hosts. It is a cross-platform tool available for Windows, macOS, and Linux.

- open source (GNU)
- free of charge
- cross-platform

Usage example:

- Discover active hosts on network and open ports
- Provides high-level view of the network
- Scan IP Ranges of 192.168.0.0 to 192.168.0.255/24

### Wireshark

Wireshark is a free and open-source network protocol analyzer. Aanalyze network traffic and troubleshoot network issues. Wireshark allows users to capture and inspect network packets in real-time, providing detailed information about the protocols and data being transmitted over a network.

- GNU
- Free of charges

Wireshark:

- Network protocol analyzer
- Captures and analyzes network packets in real-time
- Focuses on inspecting network traffic and decoding protocols
- Offers granular view of network traffic
- Provides extensive packet-level information, including headers, payloads, timing, etc.
- Primarily used for network analysis, troubleshooting, and security analysis

### CLI

```
arp -a

```

```
sudo apt install nmap
sudo nmap -sn 192.168.1.0/24
```

```
sudo apt install arp-scan
sudo arp-scan --localnet
```
