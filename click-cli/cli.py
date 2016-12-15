#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

from click_cli import __version__ as VERSION
from click_cli.lib.cli_common import BaseCLI
# include cli sub groups
import click_cli.commands.action1
import click_cli.commands.action2


class CLI(BaseCLI):

    SUB_GROUPS_REGISTRY = []

    @classmethod
    def register_cli(cls):
        for group in cls.SUB_GROUPS_REGISTRY:
            cls.cli.add_command(group)

    @staticmethod
    @click.group(subcommand_metavar='COMMAND [OPTIONS]',
                 context_settings=BaseCLI.CONTEXT_SETTINGS)
    @click.option('-v', '--verbose',
                  default=False,
                  is_flag=True,
                  help='Verbose mode')
    @click.version_option(version=VERSION)
    @BaseCLI.context()
    def cli(ctx, **kwargs):
        """
        cli
        """
        # DEBUG INFO
        ctx.config_dict.update(**kwargs)


if __name__ == "__main__":
    CLI.cli()
