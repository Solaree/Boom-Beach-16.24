from Utils.Writer import Writer


class LogicClientAvatar(Writer):

    def encode(self):

        self.writeInt(0)

        self.writeInt(0)  # DefaultHighID
        self.writeInt(1)  # DefaultLowID
        self.writeInt(0)  # CurrentHomeHighID
        self.writeInt(1)  # CurrentHomeLowID

        self.writeByte(0)  # IsInAlliance

        self.writeInt(3)  # TownHall Level

        self.writeString("Solar")  # Name
        self.writeString(None)  # FacebookID

        self.writeInt(80)   # ExpLevel
        self.writeInt(0)  # ExpPoints
        self.writeInt(1000000000)  # Diamonds
        self.writeInt(0)  # FreeDiamonds
        self.writeInt(0)  # AttackRating
        self.writeInt(0)  # AttackKFactor
        self.writeInt(0)  # Score

        self.writeByte(0)  # NameSetByUser

        self.writeInt(0)  # CumulativePurchasedDiamonds
        self.writeInt(0)  # NumberOnePosCounter

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)