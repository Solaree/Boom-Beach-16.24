from Utils.Reader import Reader
from Packets.Messages.Server.AvailableServerCommandMessage import *


class ChangeAvatarNameMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.commandID = 3

    def decode(self):
        self.playername = self.ReadString()

    def process(self):
        AvailableServerCommandMessage(self.device, self.commandID).Send()