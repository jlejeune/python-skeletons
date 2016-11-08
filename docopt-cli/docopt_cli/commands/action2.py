"""The config command."""

from docopt_cli.commands.base import Base


class Action2(Base):
    """
    Explanation of action2

    Usage:
        cli.py action2 <required_arg>
    """

    def __init__(self, options):
        Base.__init__(self, options)

    def run(self):
        print "Execute action1 subaction2 with theses args:\n", self.options
