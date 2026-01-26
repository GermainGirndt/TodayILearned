import argparse
import importlib
import inspect
import pkgutil
from src import commands
from src.commands.base_command import BaseCommand


def main():
    parser = argparse.ArgumentParser(description="Custom Developer CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Discover all classes with add_parser and run
    for _, modname, _ in pkgutil.iter_modules(commands.__path__):
        module = importlib.import_module(f"{commands.__name__}.{modname}")
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if (
                not issubclass(obj, BaseCommand)
                or obj is BaseCommand
            ):
                continue

            if not hasattr(obj, "name"):
                raise ValueError(
                    f"Command class {name} is missing 'name' attribute")

            obj.add_parser(subparsers)

    args = parser.parse_args()
    args.func(args)
