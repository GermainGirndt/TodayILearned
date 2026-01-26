import os
import subprocess
from .base_command import BaseCommand


class ScanVulnerabilitiesOnIPCommand(BaseCommand):
    name = "scan-vulnerabilities-on-ip"
    name_aliases = ["scan-vulnerabilities", "scan-vul"]
    help = "Scan IP for vulnerabilities"

    @staticmethod
    def add_arguments(parser):
        parser.add_argument("ip", help="IP address to scan")

    def run(self, args):
        print(f"Scanning {args.ip} with Nmap...")
        subprocess.run(["nmap", "--script", "vuln", args.ip])
