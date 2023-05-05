from Utils.Writer import Writer
from Logic.ClientHome import *
from Logic.ClientAvatar import *


class OwnHomeDataMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 24101

    def encode(self):
        self.writeInt(0)

        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)