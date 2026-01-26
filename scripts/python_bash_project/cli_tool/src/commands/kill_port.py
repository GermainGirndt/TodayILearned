import subprocess
from .base_command import BaseCommand


class KillPortCommand(BaseCommand):
    name = "kill-port"
    name_aliases = ["kill-processes-on-port"]
    help = "Kill processes listening on a port"

    @staticmethod
    def add_arguments(parser):
        parser.add_argument(
            "ports", type=int, nargs="+", help="Port(s) to free")

    def run(self, args):
        empty = []
        killed = []
        failed = []
        for port in args.ports:
            try:
                output = subprocess.check_output(
                    ["sudo", "lsof", "-t", f"-i:{port}"], stderr=subprocess.DEVNULL
                ).decode().strip()
                if output:
                    subprocess.run(["sudo", "kill", "-9"] + output.split())
                    killed.append(port)
                else:
                    empty.append(port)
            except subprocess.CalledProcessError:
                failed.append(port)

        print("kill-port results:")
        if killed:
            print(f"Killed: {', '.join(map(str, killed))}.")
        if failed:
            print(f"Failed: {', '.join(map(str, failed))}.")
        if empty:
            print(f"Not Found: {', '.join(map(str, empty))}.")
