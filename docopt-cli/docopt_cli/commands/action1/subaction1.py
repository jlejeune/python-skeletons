"""The action1 subaction1 command."""

from docopt_cli.commands.action1 import Action1


class Subaction1(Action1):
    """
    Explanation of action1 subaction1

    Usage:
        cli.py action1 subaction1 <required_arg> [--optional_arg]

    Options:
        --optional_arg        explanation of optionnal_arg
    """

    def run(self):
        print "Execute action1 subaction1 with theses args:\n", self.options
