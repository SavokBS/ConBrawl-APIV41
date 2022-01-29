from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Packets.Server.Home.OwnHomeDataMessage import *
import time


class LobbyInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(ClientsManager.GetCount())
        self.writeString(f"ConStars\nCurrent account: {pl.name}\n{pl.name}'s club: {pl.club.name}\n{time.asctime()}")
        self.writeVInt(0)

    def decode(self):
        fields = {}
        fields["PlayerCount"] = self.readVInt()
        fields["Text"] = self.readString()
        fields["Unk1"] = self.readVInt()
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23457

    def getMessageVersion(self):
        return self.messageVersion