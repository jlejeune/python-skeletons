# -*- coding: utf-8 -*-

import click

from click_cli.lib.cli_common import BaseCLI


class Action1(BaseCLI):

    SUB_GROUP_COMMANDS = ['subaction1', 'subaction2']
    SUB_GROUP_NAME = 'action1'

    @staticmethod
    @click.group(subcommand_metavar='COMMAND [OPTIONS]',
                 context_settings=BaseCLI.CONTEXT_SETTINGS)
    @BaseCLI.context()
    def action1(ctx, **kwargs):
        """
        Explanation of action1
        """
        # just update context for action1 subcommands here
        ctx.config_dict.update(**kwargs)

    @staticmethod
    @click.command()
    @click.option('--optional_arg', type=click.STRING, help="Explanation of optional arg")
    @BaseCLI.context()
    def subaction1(ctx, **kwargs):
        """
        Explanation of action1 subaction1
        """
        ctx.config_dict.update(**kwargs)
        click.echo("Execute action1 subaction1 with this context:\n %s" %
                   ctx.config_dict)

    @staticmethod
    @click.command()
    @click.option('--arg', type=click.STRING, required=True, help="Explanation of required arg")
    @click.option('--optional_arg', type=click.STRING, help="Explanation of optional arg")
    @BaseCLI.context()
    def subaction2(ctx, **kwargs):
        """
        Explanation of action1 subaction2
        """
        ctx.config_dict.update(**kwargs)
        click.echo("Execute action1 subaction1 with this context:\n %s" %
                   ctx.config_dict)
