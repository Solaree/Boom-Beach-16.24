from Utils.Writer import Writer
from Packets.Messages.Client.ChangeAvatarNameMessage import *

class LogicChanageAvatarNameCommand(Writer):

    def __init__(self, device, playername):
        super().__init__(device)
        self.device = device
        self.playername = playername

    def encode(self):
        self.writeString(self.playername)  # Name