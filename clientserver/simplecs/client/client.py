#!/usr/bin/env python3

from zmqcs.client import zmqClient
from zmqcs.common.message import CommandMSG, ErrorMSG
from simplecs.client.modules.modexample import ModExample


class Client(zmqClient):

    def __init__(self, en_async=True):
        super().__init__(en_async=en_async)
        # Compose the client modules here so they can be accesible
        self.modex = ModExample(client=self)

    def command(self, command, kwargs={}):
        """
        :param command: command to be executed at server.
        :param kwargs: arguments of the command
        :return: Either a CommandMSG or it raises an exception with error
        """
        t = CommandMSG(command=command, kwargs=kwargs)
        ans = self._command(t)
        if issubclass(type(ans), ErrorMSG):
            raise Exception(ans.msg)
        return ans

    def list_server_commands(self):
        return self.command('local.list')

    def get_server_pub_stats(self):
        return self.command('local.get_pub_stats')
