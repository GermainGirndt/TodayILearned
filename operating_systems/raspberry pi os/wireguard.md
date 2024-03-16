

wg set wg0 \ # interface
listen-port 59452 \ # listening to port
private-key path_to_private_key \ # using private key
peer string_with_public_key_here \ # allowing connections with public key
allowed-ips 192.168.188.0/24 # allowing peer to access ressources at ips