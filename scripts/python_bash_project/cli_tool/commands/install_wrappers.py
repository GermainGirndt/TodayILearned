from cli_tool.commands.base_command import BaseCommand
import os
import shutil
from argparse import _SubParsersAction, ArgumentParser


class InstallWrappers(BaseCommand):
    name = "install-wrappers"
    name_aliases = ["install-shell-wrappers", "install-cli-wrappers"]
    help = "Generate shell wrappers for commands in a bin directory."

    @staticmethod
    def add_arguments(parser: ArgumentParser):

        parser.add_argument(
            "--bin-dir",
            default="~/.local/bin/custom_cli",
            help="Directory where the shell wrappers will be created."
        )
        parser.add_argument(
            "--prefix",
            default="",
            help="Prefix to add to the wrapper names."
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Overwrite existing wrappers if they already exist."
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Simulate the creation of wrappers without making changes."
        )
        parser.add_argument(
            "--python-interpreter",
            default="python3",
            help="Python interpreter to use in the wrappers."
        )

    @staticmethod
    def run(args):
        # Expand and validate the bin directory
        args.bin_dir = os.path.expanduser(args.bin_dir)
        if not os.path.exists(args.bin_dir):
            try:
                os.makedirs(args.bin_dir)
            except OSError as e:
                print(
                    f"Error: Unable to create bin directory '{args.bin_dir}': {e}")
                return
        elif not os.access(args.bin_dir, os.W_OK):
            print(f"Error: Bin directory '{args.bin_dir}' is not writable.")
            return

        # Validate the Python interpreter
        if not shutil.which(args.python_interpreter):
            print(
                f"Error: Python interpreter '{args.python_interpreter}' not found.")
            return

        # Validate the commands directory
        commands_dir = os.path.dirname(__file__)
        if not os.path.exists(commands_dir):
            print(
                f"Error: Commands directory '{commands_dir}' does not exist.")
            return

        commands = [
            f[:-3] for f in os.listdir(commands_dir)
            if f.endswith(".py") and f not in ("__init__.py", "base_command.py", "install_wrappers.py")
        ]

        for command in commands:
            wrapper_name = f"{args.prefix}{command}"
            wrapper_path = os.path.join(args.bin_dir, wrapper_name)

            if args.dry_run:
                print(f"[DRY RUN] Would create wrapper: {wrapper_path}")
                continue

            if os.path.exists(wrapper_path) and not args.force:
                print(f"Skipping existing wrapper: {wrapper_path}")
                continue

            try:
                with open(wrapper_path, "w", encoding="utf-8") as wrapper_file:
                    wrapper_file.write(
                        f"#!/bin/sh\n"
                        f"exec {args.python_interpreter} -m cli_tool.commands.{command} \"$@\"\n"
                    )
                os.chmod(wrapper_path, 0o755)
                print(f"Created wrapper: {wrapper_path}")
            except OSError as e:
                print(f"Error: Unable to create wrapper '{wrapper_path}': {e}")
