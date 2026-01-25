import subprocess
from .base_command import BaseCommand


class GetIPCommand(BaseCommand):
    name = "get-ip"
    name_aliases = ["get-own-ip"]
    help = "Get public and private IP addresses"

    def run(self, args):
        try:
            hostname_ip = subprocess.getoutput("hostname -I").split()[0]
        except IndexError:
            hostname_ip = "Unavailable"

        eth0 = subprocess.getoutput("ipconfig getifaddr en0")
        eth1 = subprocess.getoutput("ipconfig getifaddr en1")
        ext1 = subprocess.getoutput(
            "curl --silent http://checkip.amazonaws.com").strip()
        ext2 = subprocess.getoutput("curl --silent ifconfig.me").strip()

        print(f"local     hostname     =>  {hostname_ip}")
        print(f"local     eth0         =>  {eth0}")
        print(f"local     eth1         =>  {eth1}")
        print(f"external  aws          =>  {ext1}")
        print(f"external  ifconfig.me  =>  {ext2}")
