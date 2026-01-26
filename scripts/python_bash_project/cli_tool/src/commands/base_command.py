# cli_tool/commands/base_command.py
from argparse import _SubParsersAction, ArgumentParser
import argparse


class BaseCommand:
    name = ""
    name_aliases = None
    help = ""

    @classmethod
    def add_parser(cls, subparsers: _SubParsersAction):
        parser = subparsers.add_parser(cls.name, help=cls.help)
        cls.add_arguments(parser)
        parser.set_defaults(func=cls().run)

    @staticmethod
    def add_arguments(parser: ArgumentParser):
        pass

    def run(self, args: argparse.Namespace):
        raise NotImplementedError
