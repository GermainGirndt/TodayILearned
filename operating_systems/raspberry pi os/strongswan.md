### Install StrongSwan
```
sudo apt install strongswan strongswan-pki libcharon-extra-plugins
```

### Create directory with keys and certificates
mkdir -p ~/pki/{cacerts,certs,private}
chmod 700 ~/pki


### Generate a CA (Certificate Authority):

ipsec pki --gen --type rsa --size 4096 --outform pem > ~/pki/private/ca-key.pem
ipsec pki --self --ca --lifetime 3650 --in ~/pki/private/ca-key.pem \
--type rsa --dn "CN=BigBrother CA" --outform pem > ~/pki/cacerts/ca-cert.pem

### Create and sign the VPN server certificate:

ipsec pki --gen --type rsa --size 4096 --outform pem > ~/pki/private/vpn-server-key.pem
ipsec pki --pub --in ~/pki/private/vpn-server-key.pem --type rsa \
| ipsec pki --issue --lifetime 1825 --cacert ~/pki/cacerts/ca-cert.pem \
--cakey ~/pki/private/ca-key.pem --dn "CN=134.96.48.169" --san "134.96.48.169" \
--flag serverAuth --flag ikeIntermediate --outform pem > ~/pki/certs/vpn-server-cert.pem

### Configure StrongSwan

```
sudo nano /etc/ipsec.conf
```

```
config setup
    charondebug="ike 2, knl 2, cfg 2, net 2, esp 2, dmn 2,  mgr 2"

conn %default
    ikelifetime=60m
    keylife=20m
    rekeymargin=3m
    keyingtries=1
    keyexchange=ikev2
    authby=secret

conn bigbrothervpn
    left=%any
    leftsubnet=0.0.0.0/0
    leftcert=vpn-server-cert.pem
    leftid=@134.96.48.169
    right=%any
    rightdns=8.8.8.8,8.8.4.4
    rightsourceip=10.10.10.0/24
    auto=add

```

### Register the secrets file

```
sudo nano /etc/ipsec.secrets
```


```
: RSA vpn-server-key.pem
```


### Updating the firewall to allow routing and vpn traffic

```
sudo nano /etc/sysctl.conf
```

Add/uncomment:
```
net.ipv4.ip_forward=1
```

And then apply:
```
sudo sysctl -p
```

And then configure the firewall:

```
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables-save
```


### Start and Enable StrongSwan (or IPSEC)

```
sudo systemctl start ipsec
sudo systemctl status ipsec
sudo systemctl enable ipsec # starts automatically by boot
```


```
UDP port 500: This port is used for the initial key exchange and for establishing the VPN tunnel.
UDP port 4500: If NAT traversal (NAT-T) is in use (common when connecting from behind a NAT or a firewall), StrongSwan will use UDP port 4500 for encapsulating ESP packets in UDP packets.
```


```
sudo cp ~/pki/certs/vpn-server-cert.pem /etc/ipsec.d/certs/
sudo chown root:root /etc/ipsec.d/certs/vpn-server-cert.pem
sudo chmod 644 /etc/ipsec.d/certs/vpn-server-cert.pem
sudo systemctl restart ipsec


# debugging
sudo journalctl -u ipsec

```


# Client


### Generating private key for the client

```
ipsec pki --gen --type rsa --size 4096 --outform pem > ~/pki/private/client-key.pem
```

### Generating client certificate request 
```
ipsec pki --pub --in ~/pki/private/client-key.pem --type rsa | ipsec pki --issue --lifetime 3650 --cacert ~/pki/cacerts/ca-cert.pem --cakey ~/pki/private/ca-key.pem --dn "CN=contact@germaingirndt.com" --san "contact@germaingirndt.com" --outform pem > ~/pki/certs/client-cert.pem
```

### Configuring the VPN Client

- Client certificate and key
- CA certificate.


```
sudo nano /opt/homebrew/etc/ipsec.conf
```

```
conn myvpn
    right=134.96.48.169
    rightid=%any
    rightsubnet=0.0.0.0/0
    leftsourceip=%config
    auto=start
    ike=aes128-sha256-modp2048,aes128-sha256-curve25519
    keyexchange=ikev2
    ikelifetime=60m
    keylife=20m
    rekeymargin=3m
    keyingtries=1
    authby=secret
    leftauth=psk
    rightauth=psk
    type=transport
    dpdaction=clear
    dpddelay=300s
```
```
sudo nano /opt/homebrew/etc/ipsec.secrets
```

```
: RSA vpn-server-key.pem
```
```
sudo cp ~/pki/private/vpn-server-key.pem /opt/homebrew/etc/ipsec.d/private/
sudo chmod 644 /opt/homebrew/etc/ipsec.d/private/vpn-server-key.pem
sudo ipsec restart
```