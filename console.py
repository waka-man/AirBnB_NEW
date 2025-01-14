"""
This module contains the entry point of the command interpreter
"""

#!/usr/bin/env python3
import cmd
class HBNBCommand(cmd.Cmd):
    """
    The class that implements the command interpreter
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Exits the command interpreter.

        Args:
            line: The input line as a string (not used).

        Returns:
            True, which indicates the command to exit the interpreter.
        """

        return True

    def do_EOF(self, line):
        """
        Handles the EOF (End Of File) command to exit the command interpreter.

        Args:
            line: The input line as a string (not used).

        Returns:
            True, which indicates the command to exit the interpreter.
        """

        return True

    def do_help(self, arg):
        """
        Displays help for commands.

        Args:
            arg: The command to display help for, or None to display general help.

        Returns:
            None
        """
        return super().do_help(arg)
    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.

        If this method returns True, the next line entered will be treated as a
        new command. Otherwise, the empty line is ignored.

        Returns:
            False, indicating that the empty line is ignored.
        """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
