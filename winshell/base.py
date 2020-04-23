# -*- coding: utf-8 -*-

__author__ = 'Alexey Elizarov (alexei.elizarov@gmail.com)'


from helpers import Observable
from subprocess import PIPE
from abc import abstractmethod
from time import sleep


class Shell(Observable):
    """
    Requirements:
        - must provide interface to Windows Command Prompt
        - must provide interface to Windows PowerShell
        - must execute commands in Windows Command Prompt
        - must execute scripts in Windows PowerShell
        - must notify observer about command execution output by request
    """

    def __init__(self, stdout=PIPE):
        """
        :param stdout: captured standard output from the child process. PIPE by default.
        """
        super().__init__()
        self._stdout = stdout  # standard captured output

    def open(self, command: str) -> None:
        """
        Open a child program in a new process and notify observers of captured output.
        :param command: sequence of program arguments.
        :return: None
        """

        try:
            # Execute a child program
            process = self._open(command)
            if not self._stdout:
                sleep(1)
        except Exception as e:
            print(e)
        else:
            try:
                # Capture output
                output = process.stdout.read().decode('cp866')
            except AttributeError as e:
                pass
            except Exception as e:
                print(e)
            else:
                # Notify observers if output is captured
                self.post(output)

    @abstractmethod
    def _open(self, command):
        pass


