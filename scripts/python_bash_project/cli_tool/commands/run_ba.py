import os
import subprocess
from pathlib import Path
from .base_command import BaseCommand


class CdbaCommand(BaseCommand):
    name = "cdba"
    help = "Change to project dir and activate env"

    def run(self, args):
        home = Path.home()
        print(f"Run manually:")
        print(
            f"cd {home}/source/bachelor-thesis && source {home}/miniforge3/bin/activate llm_env")


class BallmCommand(BaseCommand):
    name = "ballm"
    help = "Run final_llama_cpp.py script"

    def run(self, args):
        script = Path.home() / "source/bachelor-thesis/code/src/final_llama_cpp.py"
        subprocess.run(["python", str(script)])


class BatestCommand(BaseCommand):
    name = "batest"
    help = "Run unittest discovery"

    def run(self, args):
        home = Path.home()
        cmd = f"cd {home}/source/bachelor-thesis && source {home}/miniforge3/bin/activate llm_env && cd code/src && python -m unittest discover -s . -p 'test_*.py'"
        subprocess.run(cmd, shell=True)
