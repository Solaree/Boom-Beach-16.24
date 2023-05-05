from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.LoginOkMessage import *
from Packets.Messages.Server.OwnHomeDataMessage import *

class LoginMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)

    def decode(self):
        self.HighID = self.ReadUint32()
        self.LowID = self.ReadUint32()

        self.Token = self.ReadString()

        self.MajorVersion = self.ReadUint32()
        self.ContentVersion = self.ReadUint32()  # Unk
        self.BuildVersion = self.ReadUint32()

        self.ResourceSha = self.ReadString()
        self.UDID = self.ReadString()
        self.OpenUDID = self.ReadString()
        self.MacAddress = self.ReadString()
        self.DeviceModel = self.ReadString()

        self.PreferredLanguage = self.ReadUint32()

        self.OSLanguage = self.ReadString()
        self.ADID = self.ReadString()
        self.OSVersion = self.ReadString()

        self.IsAndroid = self.ReadBool()
        self.UnkBool1 = self.ReadBool()  # Unk

        self.UnkOpenUDID = self.ReadString() # Unk
        self.UnkString2 = self.ReadString()  # Unk
        self.UnkString3 = self.ReadString() # Unk
        self.UnkString4 = self.ReadString() # Unk

        self.UnkBool2 = self.ReadBool()  # Unk

    def process(self):
        LoginOkMessage(self.device).Send()
        OwnHomeDataMessage(self.device).Send()

        if self.UDID == "":
            self.UDID = "Unknown"

        if self.UnkString2 == "":
            self.UnkString2 = "None"

        if self.UnkString3 == "":
            self.UnkString3 = "None"

        if self.UnkString4 == "":
            self.UnkString4 = "None"

        print(f"\n------------------------------\n[*] Received client data:\n------------------------------\nHighID: {self.HighID}\nLowID: {self.LowID}\nPassToken: {self.Token}\nGameVersion: {self.MajorVersion}\nGameBuild: {self.BuildVersion}\nContentVersion: {self.ContentVersion}\nResource SHA: {self.ResourceSha}\nUDID: {self.UDID}\nOpenUDID: {self.OpenUDID}\nMacAddress: {self.MacAddress}\nDeviceModel: {self.DeviceModel}\nPreferredLanguage: {self.PreferredLanguage}\nOS Language: {self.OSLanguage}\nADID: {self.ADID}\nOSVersion: {self.OSVersion}\nIsAndroid: {self.IsAndroid}\n------------------------------\n[*] Received unknown client data:\n------------------------------\nUnkBool: {self.UnkBool1}\nUnkOpenUDID: {self.UnkOpenUDID}\nUnkString: {self.UnkString2}\nUnkString: {self.UnkString3}\nUnkString: {self.UnkString4}\nUnkBool: {self.UnkBool2}\n------------------------------\n")