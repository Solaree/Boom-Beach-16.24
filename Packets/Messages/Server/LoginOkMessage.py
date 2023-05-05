from Utils.Writer import Writer


class LoginOkMessage(Writer):

    def __init__(self, device):
        super().__init__(device)
        self.device = device
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeInt(0)  # AccountHighID
        self.writeInt(1)  # AccountLowID
        self.writeInt(0)  # HomeHighID
        self.writeInt(1)  # HomeLowID

        self.writeString("solarnik1337")  # PassToken
        self.writeString("facebookid")  # FacebookID
        self.writeString("gamecenterid")  # GameCenterID

        self.writeInt(16)  # MajorVersion
        self.writeInt(24)  # BuildVersion
        self.writeInt(1)  # ContentVersion

        self.writeString("dev")  # ServerEnvironment
        self.writeString("EN")  # CountryCode
        self.writeString()  # FacebookAppID
        self.writeString()  # GameCenterAppID
        self.writeString()  # Unk