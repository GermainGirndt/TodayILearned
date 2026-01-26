# cli_tool/commands/kill_process.py
from .base_command import BaseCommand
import subprocess


class KillProcessCommand(BaseCommand):
    name = "kill-process"
    name_aliases = ["kill-process-containing-name",
                    "kill-by-name",
                    "killname"]
    help = "Kill process containing name"

    @staticmethod
    def add_arguments(parser):
        parser.add_argument("name", help="Process name")

    def run(self, args):
        name = args.name
        if subprocess.call(["pgrep", "-x", name], stdout=subprocess.DEVNULL) != 0:
            print(f"No process found with name: {name}")
            return

        before = int(subprocess.getoutput(f"pgrep -x {name} | wc -l"))
        subprocess.run(["pkill", name])
        after = int(subprocess.getoutput(f"pgrep -x {name} | wc -l"))
        print(
            f"Killed {before - after} instances of {name}. Remaining: {after}")
