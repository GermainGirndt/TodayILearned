# Client Setup

Linux:

```
sh <(curl -sSf https://downloads.nordcdn.com/apps/linux/install.sh)

nordvpn login

nordvpn connect
```

# Commands

## Log in

```
nordvpn login
```

## Connect to VPN

note: To connect to specific servers, use nordvpn connect <country_code server_number> (eg.

```
nordvpn connect <country_code server_number>
```

eg.:

```
nordvpn connect uk715
```

## Disconnect from VPN.

```
nordvpn disconnect
```

## Connect to the closest Double VPN server.

```
nordvpn connect double_vpnd
```

## Connect to a specific country using DoubleVPN servers.

```
nordvpn connect --group double_vpn <country_code>
```

## connect to a P2P server.

```
nordvpn connect P2P
```

## connect to servers located in the Americas.

```
nordvpn connect The_Americas
```

## connect to a Dedicated IP server.

```
nordvpn connect Dedicated_IP
```

## Set a configuration option.

```
nordvpn set or nordvpn s
```

# Possible options:

## Enable or disable CyberSec

```
nordvpn set cybersec on or off
```

## Enable or disable Kill Switch

```
nordvpn set killswitch on or off
```

## Enable or disable auto-connect. You can set a specific server for automatic connection using

```
nordvpn set autoconnect on or off
nordvpn set autoconnect on country_code+server_number. Example: nordvpn set autoconnect on us2435.
```

## Enable or disable notifications

```
nordvpn set notify on or off
```

## Set custom DNS (you can set up a single DNS or two like shown in this command).

```
nordvpn set dns 1.1.1.1 1.0.0.1
```

## Switch between UDP and TCP protocols

```
nordvpn set protocol udp or tcp
```

## Enable or disable Obfuscated Servers.

Notes: More security layers; Onion based

```
nordvpn set obfuscate on or off
```

## Set connection technology (OpenVPN or NordLynx)

```
nordvpn set technology
```

## Add a rule to whitelist a specified incoming port. You can also whitelist multiple ports — just

```
nordvpn whitelist add port 22
```

Notes: separate their numbers with a space.

## Remove the rule to whitelist a specified port.

```
nordvpn whitelist remove port 22
```

## Add a rule to whitelist a specified subnet.

```
nordvpn whitelist add subnet 192.168.0.0/16
```

## Remove the rule to whitelist a specified subnet.

```
nordvpn whitelist remove subnet 192.168.0.0/16
```

## See account information

```
nordvpn account
```

## Register a new user account

```
nordvpn register
```

## Rate your last connection quality (1-5)

```
nordvpn rated
```

## See the current settings.

```
nordvpn settings
```

## See the connection status.

```
nordvpn status
```

## See the country list.

```
nordvpn countries
```

nordvpn cities- See the city list. E.g.: nordvpn cities united_states

## See a list of available server groups.

```
nordvpn groups
```

## Log out.

```
nordvpn logout
```

## See the list of available commands or help for a specific command.

```
nordvpn help or nordvpn h
```
