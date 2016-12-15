# -*- coding: utf-8 -*-

import click

from click_cli.lib.cli_common import BaseCLI


class Action2(BaseCLI):

    SUB_GROUP_COMMANDS = ['subaction1', 'subaction2']
    SUB_GROUP_NAME = 'action2'

    @staticmethod
    @click.group(subcommand_metavar='COMMAND [OPTIONS]',
                 context_settings=BaseCLI.CONTEXT_SETTINGS)
    @BaseCLI.context()
    def action2(ctx, **kwargs):
        """
        Explanation of action2
        """
        # just update context for action2 subcommands here
        ctx.config_dict.update(**kwargs)

    @staticmethod
    @click.command()
    @click.option('--optional_arg', type=click.STRING, help="Explanation of optional arg")
    @BaseCLI.context()
    def subaction1(ctx, **kwargs):
        """
        Explanation of action2 subaction1
        """
        ctx.config_dict.update(**kwargs)
        click.echo("Execute action2 subaction1 with this context:\n %s" %
                   ctx.config_dict)

    @staticmethod
    @click.command()
    @click.option('--arg', type=click.STRING, required=True, help="Explanation of required arg")
    @click.option('--optional_arg', type=click.STRING, help="Explanation of optional arg")
    @BaseCLI.context()
    def subaction2(ctx, **kwargs):
        """
        Explanation of action2 subaction2
        """
        ctx.config_dict.update(**kwargs)
        click.echo("Execute action2 subaction1 with this context:\n %s" %
                   ctx.config_dict)
