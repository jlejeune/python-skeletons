"""The config command."""


from docopt_cli.commands.base import Base


class Action1(Base):
    """
    Explanation of action1

    Usage:
      cli.py action1 <command>

    Commands:
      subaction1                 explanation of subaction1 for action1 command
      subaction2                 explanation of subaction2 for action1 command
    """

    def __init__(self, options):
        Base.__init__(self, options)

    def run(self):
        raise NotImplementedError(
            'You must implement the run() method yourself!')
