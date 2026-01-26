import os
import subprocess
from .base_command import BaseCommand


class CheckPortCommand(BaseCommand):
    name = "check-port"
    name_aliases = [
        "check-port-status",
        "check-ports",
        "check-port",
        "checkports",
        "checkport"]
    help = "Check if ports are in use"

    @staticmethod
    def add_arguments(parser):
        parser.add_argument("ports", nargs="+", type=int)

    def run(self, args):
        for port in args.ports:
            print(f"\nChecking port: {port}")
            print("Using LSOF:")
            subprocess.run(["lsof", "-i", f":{port}"])
            print("Using NETSTAT:")
            subprocess.run(f"netstat -tuln | grep :{port}", shell=True)
            print("-" * 40)
