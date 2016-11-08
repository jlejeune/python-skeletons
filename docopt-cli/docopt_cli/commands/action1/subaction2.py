"""The action1 subaction2 command."""

from docopt_cli.commands.action1 import Action1

#cli.py action1 subaction2 [--optional_arg3=<arg3>] [--optional_arg1 | --optional_arg2]
class Subaction2(Action1):
    """
    Explanation of action1 subaction2

    Usage:
        cli.py action1 subaction2 [--optional_arg3=<arg3>] [--optional_arg1 | --optional_arg2]

    Options:
        --optional_arg1             explanation of optionnal_arg1
        --optional_arg2             explanation of optionnal_arg2
        --optional_arg3=<arg3>      explanation of optionnal_arg3 which takes a required arg3
    """

    def run(self):
        print "Execute action1 subaction2 with theses args:\n", self.options
