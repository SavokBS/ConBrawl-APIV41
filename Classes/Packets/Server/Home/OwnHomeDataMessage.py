import time
import brawlstats
import Configuration
import random

from Classes.Packets.PiranhaMessage import PiranhaMessage

bstoken = Configuration.settings["ApiToken"] #api token
client = brawlstats.Client(bstoken)
pl = client.get_profile(Configuration.settings["Tag"]) #tag

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVInt(int(time.time()))
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(pl.trophies) # Trophies
        self.writeVInt(pl.highest_trophies) # Highest Trophies
        self.writeVInt(pl.highest_trophies)
        self.writeVInt(200)
        self.writeVInt(pl.exp_points) # Experience
        self.writeDataReference(28, player.Thumbnail) # Thumbnail
        self.writeDataReference(43, player.Namecolor) # Namecolor

        self.writeVInt(0)

        self.writeVInt(0) # Selected Skins

        self.writeVInt(0) # Randomizer Skin Selected

        self.writeVInt(0) # Current Random Skin

        self.writeVInt(len(ownedSkins))

        for skinID in ownedSkins:
            self.writeDataReference(29, skinID)

        self.writeVInt(0) # Unlocked Skin Purchase Option

        self.writeVInt(0) # New Item State

        self.writeVInt(0)
        self.writeVInt(pl.highest_trophies)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeBoolean(True)
        self.writeVInt(player.TokensDoubler)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(141)
        self.writeVInt(135)

        self.writeVInt(5)

        self.writeVInt(93)
        self.writeVInt(206)
        self.writeVInt(456)
        self.writeVInt(792)
        self.writeVInt(729)

        self.writeBoolean(False) # Offer 1
        self.writeBoolean(False) # Offer 2
        self.writeBoolean(True) # Token Doubler Enabled
        self.writeVInt(2)  # Token Doubler New Tag State
        self.writeVInt(2)  # Event Tickets New Tag State
        self.writeVInt(2)  # Coin Packs New Tag State
        self.writeVInt(0)  # Change Name Cost
        self.writeVInt(0)  # Timer For the Next Name Change

        self.writeVInt(1) # Offers count

        self.writeVInt(1)  # RewardCount
        for i in range(1):
            self.writeVInt(20)  # ItemType
            self.writeVInt(0)
            self.writeDataReference(0)  # CsvID
            self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(950400)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(3917)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(49)
        self.writeInt(0)
        self.writeString("Unlock all skins")
        self.writeBoolean(False)
        self.writeString()
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0)

        self.writeVInt(player.Tokens)
        self.writeVInt(-1)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(len(player.SelectedBrawlers))
        for i in player.SelectedBrawlers:
            self.writeDataReference(16, i)

        self.writeString(player.Region)
        self.writeString("ConBrawl. Using BSDS")

        self.writeVInt(19)
        self.writeLong(2, 1)  # Unknown
        self.writeLong(3, 0)  # TokensGained
        self.writeLong(4, 0)  # TrophiesGained
        self.writeLong(6, 0)  # DemoAccount
        self.writeLong(7, 0)  # InvitesBlocked
        self.writeLong(8, 0)  # StarPointsGained
        self.writeLong(9, 1)  # ShowStarPoints
        self.writeLong(10, 0)  # PowerPlayTrophiesGained
        self.writeLong(12, 1)  # Unknown
        self.writeLong(14, 0)  # CoinsGained
        self.writeLong(15, 0)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeLong(16, 1)
        self.writeLong(17, 1)  # TeamChatMuted
        self.writeLong(18, 1)  # EsportButton
        self.writeLong(19, 1)  # ChampionShipLivesBuyPopup
        self.writeLong(20, 0)  # GemsGained
        self.writeLong(21, 1)  # LookingForTeamState
        self.writeLong(22, 1)
        self.writeLong(24, 1)  # Have already watched club league stupid animation

        self.writeVInt(0)

        self.writeVInt(2)  # Brawlpass
        for i in range(8, 10):
            self.writeVInt(i)
            self.writeVInt(34500)
            self.writeBoolean(True)
            self.writeVInt(0)

            self.writeByte(2)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

            self.writeByte(1)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(ownedPinsCount + ownedThumbnailCount)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        self.writeBoolean(False)

        self.writeInt(0)

        self.writeVInt(0)

        self.writeVInt(25) # Count

        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13)
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(20)
        self.writeVInt(21)
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)

        self.writeVInt(2) # Events

        self.writeVInt(0)
        self.writeVInt(12)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, random.randint(0, 500))  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0)  
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) 
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(6) 
        self.writeVInt(3)
        self.writeVInt(0)  # ChronosTextEntry
        self.writeVInt(-64)
        self.writeBoolean(False)

        self.writeVInt(0)
        self.writeVInt(13)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, random.randint(0, 500))  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) 
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(6) 
        self.writeVInt(3) 
        self.writeVInt(0)  # ChronosTextEntry
        self.writeVInt(-64)
        self.writeBoolean(False)


        self.writeVInt(0) # Comming Events

        self.writeVInt(10)  # Brawler Upgrade Cost
        self.writeVInt(20)
        self.writeVInt(35)
        self.writeVInt(75)
        self.writeVInt(140)
        self.writeVInt(290)
        self.writeVInt(480)
        self.writeVInt(800)
        self.writeVInt(1250)
        self.writeVInt(1875)
        self.writeVInt(2800)

        self.writeVInt(4)  # Shop Coins Price
        self.writeVInt(20)
        self.writeVInt(50)
        self.writeVInt(140)
        self.writeVInt(280)

        self.writeVInt(4)  # Shop Coins Amount
        self.writeVInt(150)
        self.writeVInt(400)
        self.writeVInt(1200)
        self.writeVInt(2600)

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVInt(0)

        self.writeVInt(23)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000038)  # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 1)
        self.writeLong(61, 36270)  # SupportDisabled State | if 36218 < state its true
        self.writeLong(47, 41381)
        self.writeLong(29, 0)  # Skin Group Active For Campaign
        self.writeLong(48, 41381)
        self.writeLong(50, 0)  # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1101, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 1)  # Double Token Event
        self.writeLong(31, 1)  # Gold rush event
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(17, 4)
        self.writeLong(10046, 1)

        self.writeVInt(0) # Timed Int Value Entry

        self.writeVInt(0)  # Custom Event

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeLong(player.ID[0], player.ID[1])  # PlayerID

        self.writeVInt(0) # NotificationFactory

        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString(pl.name)
        self.writeBoolean(player.Registered)
        self.writeInt(0)

        self.writeVInt(15)

        blen = len(pl.brawlers)
        # card0 = 0, 
        # card1 = 4
        # card2 = 8 
        # card3 = 12 
        # card4 = 16 
        # card5 = 20 
        # card6 = 24 
        # card7 = 28 
        # card8 = 32 
        # card9 = 36 
        # card10 = 40 
        # card11 = 44 
        # card12 = 48 
        # card13 = 52  
        # card14 = 56 
        # card15 = 60 
        # card16 = 64  
        # card17 = 68 
        # card18 = 72 
        # card19 = 95 
        # card20 = 100 
        # card21 = 105 
        # card22 = 110 
        # card23 = 115 
        # card24 = 120
        # card25 = 125
        # card26 = 130
        # card27 = 177  
        # card28 = 182 
        # card29 = 188  
        # card30 = 194 
        # card31 = 200
        # card32 = 206 
        # card34 = 218 
        # card35 = 224 
        # card36 = 230
        # card37 = 236 
        # card38 = 279 
        # card39 = 296 
        # card40 = 303 
        # card41 = 320 
        # card42 = 327 
        # card43 = 334 
        # card44 = 341 
        # card45 = 358 
        # card46 = 365
        # card47 = 372
        # card48 = 379
        # card49 = 386 
        # card50 = 393
        # card51 = 410 
        # card52 = 417 
        # card53 = 427
        # card54 = 434


        #Change anything here ONLY IF YOU UNDERSTAND WHAT ARE YOU DOING!
        print(len(pl.brawlers)) #debug thing


        self.writeVInt(3 + len(pl.brawlers))

        try:
            print(f"{pl.brawlers[0].power} loaded in cards!")
            self.writeDataReference(23, 0)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[1].power} loaded in cards!")
            self.writeDataReference(23, 4)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[2].power} loaded in cards!")
            self.writeDataReference(23, 8)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[3].power} loaded in cards!")
            self.writeDataReference(23, 12)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[4].power} loaded in cards!")
            self.writeDataReference(23, 16)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[5].power} loaded in cards!")
            self.writeDataReference(23, 20)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[6].power} loaded in cards!")
            self.writeDataReference(23, 24)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[7].power} loaded in cards!")
            self.writeDataReference(23, 28)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[8].power} loaded in cards!")
            self.writeDataReference(23, 32)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[9].power} loaded in cards!")
            self.writeDataReference(23, 36)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[10].power} loaded in cards!")
            self.writeDataReference(23, 40)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[11].power} loaded in cards!")
            self.writeDataReference(23, 44)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[12].power} loaded in cards!")
            self.writeDataReference(23, 48)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[13].power} loaded in cards!")
            self.writeDataReference(23, 52)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[14].power} loaded in cards!")
            self.writeDataReference(23, 56)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[15].power} loaded in cards!")
            self.writeDataReference(23, 60)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[16].power} loaded in cards!")
            self.writeDataReference(23, 64)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[17].power} loaded in cards!")
            self.writeDataReference(23, 68)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[18].power} loaded in cards!")
            self.writeDataReference(23, 72)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[19].power} loaded in cards!")
            self.writeDataReference(23, 95)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[20].power} loaded in cards!")
            self.writeDataReference(23, 100)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[21].power} loaded in cards!")
            self.writeDataReference(23, 105)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[22].power} loaded in cards!")
            self.writeDataReference(23, 110)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[23].power} loaded in cards!")
            self.writeDataReference(23, 115)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[24].power} loaded in cards!")
            self.writeDataReference(23, 120)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[25].power} loaded in cards!")
            self.writeDataReference(23, 125)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[26].power} loaded in cards!")
            self.writeDataReference(23, 130)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[27].power} loaded in cards!")
            self.writeDataReference(23, 177)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[28].power} loaded in cards!")
            self.writeDataReference(23, 182)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[29].power} loaded in cards!")
            self.writeDataReference(23, 188)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[30].power} loaded in cards!")
            self.writeDataReference(23, 194)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[31].power} loaded in cards!")
            self.writeDataReference(23, 200)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[32].power} loaded in cards!")
            self.writeDataReference(23, 206)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[33].power} loaded in cards!")
            self.writeDataReference(23, 218)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[34].power} loaded in cards!")
            self.writeDataReference(23, 224)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[35].power} loaded in cards!")
            self.writeDataReference(23, 230)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[36].power} loaded in cards!")
            self.writeDataReference(23, 236)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[37].power} loaded in cards!")
            self.writeDataReference(23, 279)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[38].power} loaded in cards!")
            self.writeDataReference(23, 296)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[39].power} loaded in cards!")
            self.writeDataReference(23, 303)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[40].power} loaded in cards!")
            self.writeDataReference(23, 320)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[41].power} loaded in cards!")
            self.writeDataReference(23, 327)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[42].power} loaded in cards!")
            self.writeDataReference(23, 334)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[43].power} loaded in cards!")
            self.writeDataReference(23, 341)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[44].power} loaded in cards!")
            self.writeDataReference(23, 358)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[45].power} loaded in cards!")
            self.writeDataReference(23, 365)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[46].power} loaded in cards!")
            self.writeDataReference(23, 372)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[47].power} loaded in cards!")
            self.writeDataReference(23, 379)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[48].power} loaded in cards!")
            self.writeDataReference(23, 386)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[49].power} loaded in cards!")
            self.writeDataReference(23, 393)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[50].power} loaded in cards!")
            self.writeDataReference(23, 410)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[51].power} loaded in cards!")
            self.writeDataReference(23, 417)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[52].power} loaded in cards!")
            self.writeDataReference(23, 427)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        try:
            print(f"{pl.brawlers[53].power} loaded in cards!")
            self.writeDataReference(23, 434)
            self.writeVInt(1)
        except IndexError:
            pass
        else:
            pass

        

        self.writeDataReference(5, 8)
        self.writeVInt(-1)

        self.writeDataReference(5, 10)
        self.writeVInt(-1)

        self.writeDataReference(5, 13)
        self.writeVInt(99999) # Club coins

        self.writeVInt(len(pl.brawlers))

        try:
            self.writeDataReference(16, 0)
            self.writeVInt(pl.brawlers[0].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 1)
            self.writeVInt(pl.brawlers[1].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 2)
            self.writeVInt(pl.brawlers[2].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 3)
            self.writeVInt(pl.brawlers[3].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 4)
            self.writeVInt(pl.brawlers[4].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 5)
            self.writeVInt(pl.brawlers[5].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 6)
            self.writeVInt(pl.brawlers[6].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 7)
            self.writeVInt(pl.brawlers[7].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 8)
            self.writeVInt(pl.brawlers[8].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 9)
            self.writeVInt(pl.brawlers[9].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 10)
            self.writeVInt(pl.brawlers[10].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 11)
            self.writeVInt(pl.brawlers[11].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 12)
            self.writeVInt(pl.brawlers[12].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 13)
            self.writeVInt(pl.brawlers[13].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 14)
            self.writeVInt(pl.brawlers[14].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 15)
            self.writeVInt(pl.brawlers[15].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 16)
            self.writeVInt(pl.brawlers[16].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 17)
            self.writeVInt(pl.brawlers[17].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 18)
            self.writeVInt(pl.brawlers[18].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 19)
            self.writeVInt(pl.brawlers[19].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 20)
            self.writeVInt(pl.brawlers[20].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 21)
            self.writeVInt(pl.brawlers[21].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 22)
            self.writeVInt(pl.brawlers[22].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 23)
            self.writeVInt(pl.brawlers[23].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 24)
            self.writeVInt(pl.brawlers[24].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 25)
            self.writeVInt(pl.brawlers[25].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 26)
            self.writeVInt(pl.brawlers[26].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 27)
            self.writeVInt(pl.brawlers[27].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 28)
            self.writeVInt(pl.brawlers[28].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 29)
            self.writeVInt(pl.brawlers[29].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 30)
            self.writeVInt(pl.brawlers[30].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 31)
            self.writeVInt(pl.brawlers[31].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 32)
            self.writeVInt(pl.brawlers[32].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 34)
            self.writeVInt(pl.brawlers[33].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 35)
            self.writeVInt(pl.brawlers[34].trophies)
        except IndexError:
            pass
        else:
            pass

        
        try:
            self.writeDataReference(16, 36)
            self.writeVInt(pl.brawlers[35].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 37)
            self.writeVInt(pl.brawlers[36].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 38)
            self.writeVInt(pl.brawlers[37].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 39)
            self.writeVInt(pl.brawlers[38].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 40)
            self.writeVInt(pl.brawlers[39].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 41)
            self.writeVInt(pl.brawlers[40].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 42)
            self.writeVInt(pl.brawlers[41].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 43)
            self.writeVInt(pl.brawlers[42].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 44)
            self.writeVInt(pl.brawlers[43].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 45)
            self.writeVInt(pl.brawlers[44].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 46)
            self.writeVInt(pl.brawlers[45].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 47)
            self.writeVInt(pl.brawlers[46].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 48)
            self.writeVInt(pl.brawlers[47].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 49)
            self.writeVInt(pl.brawlers[48].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 50)
            self.writeVInt(pl.brawlers[49].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 51)
            self.writeVInt(pl.brawlers[50].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 52)
            self.writeVInt(pl.brawlers[51].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 53)
            self.writeVInt(pl.brawlers[52].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 54)
            self.writeVInt(pl.brawlers[53].trophies)
        except IndexError:
            pass
        else:
            pass

        self.writeVInt(len(pl.brawlers))

        try:
            self.writeDataReference(16, 0)
            self.writeVInt(pl.brawlers[0].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 1)
            self.writeVInt(pl.brawlers[1].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 2)
            self.writeVInt(pl.brawlers[2].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 3)
            self.writeVInt(pl.brawlers[3].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 4)
            self.writeVInt(pl.brawlers[4].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 5)
            self.writeVInt(pl.brawlers[5].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 6)
            self.writeVInt(pl.brawlers[6].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 7)
            self.writeVInt(pl.brawlers[7].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 8)
            self.writeVInt(pl.brawlers[8].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 9)
            self.writeVInt(pl.brawlers[9].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 10)
            self.writeVInt(pl.brawlers[10].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 11)
            self.writeVInt(pl.brawlers[11].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 12)
            self.writeVInt(pl.brawlers[12].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 13)
            self.writeVInt(pl.brawlers[13].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 14)
            self.writeVInt(pl.brawlers[14].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 15)
            self.writeVInt(pl.brawlers[15].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 16)
            self.writeVInt(pl.brawlers[16].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 17)
            self.writeVInt(pl.brawlers[17].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 18)
            self.writeVInt(pl.brawlers[18].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 19)
            self.writeVInt(pl.brawlers[19].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 20)
            self.writeVInt(pl.brawlers[20].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 21)
            self.writeVInt(pl.brawlers[21].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 22)
            self.writeVInt(pl.brawlers[22].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 23)
            self.writeVInt(pl.brawlers[23].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 24)
            self.writeVInt(pl.brawlers[24].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 25)
            self.writeVInt(pl.brawlers[25].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 26)
            self.writeVInt(pl.brawlers[26].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 27)
            self.writeVInt(pl.brawlers[27].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 28)
            self.writeVInt(pl.brawlers[28].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 29)
            self.writeVInt(pl.brawlers[29].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 30)
            self.writeVInt(pl.brawlers[30].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 31)
            self.writeVInt(pl.brawlers[31].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 32)
            self.writeVInt(pl.brawlers[32].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 34)
            self.writeVInt(pl.brawlers[33].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 35)
            self.writeVInt(pl.brawlers[34].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        
        try:
            self.writeDataReference(16, 36)
            self.writeVInt(pl.brawlers[35].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 37)
            self.writeVInt(pl.brawlers[36].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 38)
            self.writeVInt(pl.brawlers[37].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 39)
            self.writeVInt(pl.brawlers[38].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 40)
            self.writeVInt(pl.brawlers[39].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 41)
            self.writeVInt(pl.brawlers[40].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 42)
            self.writeVInt(pl.brawlers[41].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 43)
            self.writeVInt(pl.brawlers[42].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 44)
            self.writeVInt(pl.brawlers[43].highest_trophies)
        except IndexError:
            pass
        else:
            pass
        try:
            self.writeDataReference(16, 45)
            self.writeVInt(pl.brawlers[44].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 46)
            self.writeVInt(pl.brawlers[45].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 47)
            self.writeVInt(pl.brawlers[46].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 48)
            self.writeVInt(pl.brawlers[47].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 49)
            self.writeVInt(pl.brawlers[48].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 50)
            self.writeVInt(pl.brawlers[49].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 51)
            self.writeVInt(pl.brawlers[50].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 52)
            self.writeVInt(pl.brawlers[51].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 53)
            self.writeVInt(pl.brawlers[52].highest_trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 54)
            self.writeVInt(pl.brawlers[53].highest_trophies)
        except IndexError:
            pass
        else:
            pass #high trophies end

        self.writeVInt(0)

        self.writeVInt(len(pl.brawlers))

        try:
            self.writeDataReference(16, 0)
            self.writeVInt(pl.brawlers[0].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 1)
            self.writeVInt(pl.brawlers[1].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 2)
            self.writeVInt(pl.brawlers[2].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 3)
            self.writeVInt(pl.brawlers[3].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 4)
            self.writeVInt(pl.brawlers[4].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 5)
            self.writeVInt(pl.brawlers[5].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 6)
            self.writeVInt(pl.brawlers[6].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 7)
            self.writeVInt(pl.brawlers[7].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 8)
            self.writeVInt(pl.brawlers[8].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 9)
            self.writeVInt(pl.brawlers[9].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 10)
            self.writeVInt(pl.brawlers[10].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 11)
            self.writeVInt(pl.brawlers[11].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 12)
            self.writeVInt(pl.brawlers[12].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 13)
            self.writeVInt(pl.brawlers[13].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 14)
            self.writeVInt(pl.brawlers[14].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 15)
            self.writeVInt(pl.brawlers[15].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 16)
            self.writeVInt(pl.brawlers[16].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 17)
            self.writeVInt(pl.brawlers[17].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 18)
            self.writeVInt(pl.brawlers[18].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 19)
            self.writeVInt(pl.brawlers[19].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 20)
            self.writeVInt(pl.brawlers[20].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 21)
            self.writeVInt(pl.brawlers[21].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 22)
            self.writeVInt(pl.brawlers[22].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 23)
            self.writeVInt(pl.brawlers[23].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 24)
            self.writeVInt(pl.brawlers[24].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 25)
            self.writeVInt(pl.brawlers[25].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 26)
            self.writeVInt(pl.brawlers[26].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 27)
            self.writeVInt(pl.brawlers[27].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 28)
            self.writeVInt(pl.brawlers[28].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 29)
            self.writeVInt(pl.brawlers[29].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 30)
            self.writeVInt(pl.brawlers[30].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 31)
            self.writeVInt(pl.brawlers[31].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 32)
            self.writeVInt(pl.brawlers[32].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 34)
            self.writeVInt(pl.brawlers[33].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 35)
            self.writeVInt(pl.brawlers[34].trophies)
        except IndexError:
            pass
        else:
            pass

        
        try:
            self.writeDataReference(16, 36)
            self.writeVInt(pl.brawlers[35].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 37)
            self.writeVInt(pl.brawlers[36].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 38)
            self.writeVInt(pl.brawlers[37].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 39)
            self.writeVInt(pl.brawlers[38].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 40)
            self.writeVInt(pl.brawlers[39].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 41)
            self.writeVInt(pl.brawlers[40].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 42)
            self.writeVInt(pl.brawlers[41].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 43)
            self.writeVInt(pl.brawlers[42].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 44)
            self.writeVInt(pl.brawlers[43].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 45)
            self.writeVInt(pl.brawlers[44].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 46)
            self.writeVInt(pl.brawlers[45].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 47)
            self.writeVInt(pl.brawlers[46].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 48)
            self.writeVInt(pl.brawlers[47].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 49)
            self.writeVInt(pl.brawlers[48].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 50)
            self.writeVInt(pl.brawlers[49].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 51)
            self.writeVInt(pl.brawlers[50].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 52)
            self.writeVInt(pl.brawlers[51].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 53)
            self.writeVInt(pl.brawlers[52].trophies)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 54)
            self.writeVInt(pl.brawlers[53].trophies)
        except IndexError:
            pass
        else:
            pass #power points end

        self.writeVInt(len(pl.brawlers))
        try:
            self.writeDataReference(16, 0)
            self.writeVInt(pl.brawlers[0].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 1)
            self.writeVInt(pl.brawlers[1].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 2)
            self.writeVInt(pl.brawlers[2].power - 1)
        except IndexError:
            pass
        else:
            pass
        try:
            self.writeDataReference(16, 3)
            self.writeVInt(pl.brawlers[3].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 4)
            self.writeVInt(pl.brawlers[4].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 5)
            self.writeVInt(pl.brawlers[5].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 6)
            self.writeVInt(pl.brawlers[6].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 7)
            self.writeVInt(pl.brawlers[7].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 8)
            self.writeVInt(pl.brawlers[8].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 9)
            self.writeVInt(pl.brawlers[9].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 10)
            self.writeVInt(pl.brawlers[10].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 11)
            self.writeVInt(pl.brawlers[11].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 12)
            self.writeVInt(pl.brawlers[12].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 13)
            self.writeVInt(pl.brawlers[13].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 14)
            self.writeVInt(pl.brawlers[14].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 15)
            self.writeVInt(pl.brawlers[15].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 16)
            self.writeVInt(pl.brawlers[16].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 17)
            self.writeVInt(pl.brawlers[17].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 18)
            self.writeVInt(pl.brawlers[18].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 19)
            self.writeVInt(pl.brawlers[19].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 20)
            self.writeVInt(pl.brawlers[20].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 21)
            self.writeVInt(pl.brawlers[21].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 22)
            self.writeVInt(pl.brawlers[22].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 23)
            self.writeVInt(pl.brawlers[23].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 24)
            self.writeVInt(pl.brawlers[24].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 25)
            self.writeVInt(pl.brawlers[25].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 26)
            self.writeVInt(pl.brawlers[26].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 27)
            self.writeVInt(pl.brawlers[27].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 28)
            self.writeVInt(pl.brawlers[28].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 29)
            self.writeVInt(pl.brawlers[29].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 30)
            self.writeVInt(pl.brawlers[30].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 31)
            self.writeVInt(pl.brawlers[31].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 32)
            self.writeVInt(pl.brawlers[32].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 34)
            self.writeVInt(pl.brawlers[33].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 35)
            self.writeVInt(pl.brawlers[34].power - 1)
        except IndexError:
            pass
        else:
            pass

        
        try:
            self.writeDataReference(16, 36)
            self.writeVInt(pl.brawlers[35].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 37)
            self.writeVInt(pl.brawlers[36].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 38)
            self.writeVInt(pl.brawlers[37].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 39)
            self.writeVInt(pl.brawlers[38].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 40)
            self.writeVInt(pl.brawlers[39].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 41)
            self.writeVInt(pl.brawlers[40].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 42)
            self.writeVInt(pl.brawlers[41].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 43)
            self.writeVInt(pl.brawlers[42].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 44)
            self.writeVInt(pl.brawlers[43].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 45)
            self.writeVInt(pl.brawlers[44].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 46)
            self.writeVInt(pl.brawlers[45].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 47)
            self.writeVInt(pl.brawlers[46].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 48)
            self.writeVInt(pl.brawlers[47].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 49)
            self.writeVInt(pl.brawlers[48].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 50)
            self.writeVInt(pl.brawlers[49].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 51)
            self.writeVInt(pl.brawlers[50].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 52)
            self.writeVInt(pl.brawlers[51].power - 1)
        except IndexError:
            pass
        else:
            pass

        try:
            self.writeDataReference(16, 53)
            self.writeVInt(pl.brawlers[52].power - 1)
        except IndexError:
            pass
        else:
            pass

        try: 
            self.writeDataReference(16, 54)
            self.writeVInt(pl.brawlers[53].power - 1)
        except IndexError:
            pass
        else:
            pass #power end

        self.writeVInt(0) #я люблю когда волосатые хеоны обмазываются маслом

        
        self.writeVInt(len(pl.brawlers))

        try:
            print(pl.brawlers[0].id)
            self.writeDataReference(16, 0)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[1].id)
            self.writeDataReference(16, 1)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[2].id)
            self.writeDataReference(16, 2)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[3].id)
            self.writeDataReference(16, 3)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[4].id)
            self.writeDataReference(16, 4)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[5].id)
            self.writeDataReference(16, 5)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[6].id)
            self.writeDataReference(16, 6)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[7].id)
            self.writeDataReference(16, 7)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[8].id)
            self.writeDataReference(16, 8)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[9].id)
            self.writeDataReference(16, 9)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[10].id)
            self.writeDataReference(16, 10)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[11].id)            
            self.writeDataReference(16, 11)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[12].id)
            self.writeDataReference(16, 12)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[13].id)
            self.writeDataReference(16, 13)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[14].id)
            self.writeDataReference(16, 14)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[15].id)
            self.writeDataReference(16, 15)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[16].id)
            self.writeDataReference(16, 16)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[17].id)
            self.writeDataReference(16, 17)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[18].id)
            self.writeDataReference(16, 18)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[19].id)
            self.writeDataReference(16, 19)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[20].id)
            self.writeDataReference(16, 20)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[21].id)
            self.writeDataReference(16, 21)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[22].id)
            self.writeDataReference(16, 22)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[23].id)
            self.writeDataReference(16, 23)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[24].id)
            self.writeDataReference(16, 24)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[25].id)
            self.writeDataReference(16, 25)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[26].id)
            self.writeDataReference(16, 26)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[27].id)
            self.writeDataReference(16, 27)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[28].id)
            self.writeDataReference(16, 28)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[29].id)
            self.writeDataReference(16, 29)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[30].id)
            self.writeDataReference(16, 30)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[31].id)
            self.writeDataReference(16, 31)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[32].id)
            self.writeDataReference(16, 32)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[33].id)
            self.writeDataReference(16, 34)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[34].id)
            self.writeDataReference(16, 35)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        
        try:
            print(pl.brawlers[35].id)
            self.writeDataReference(16, 36)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[36].id)
            self.writeDataReference(16, 37)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[37].id)
            self.writeDataReference(16, 38)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[38].id)
            self.writeDataReference(16, 39)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[39].id)
            self.writeDataReference(16, 40)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[40].id)
            self.writeDataReference(16, 41)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[41].id)
            self.writeDataReference(16, 42)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[42].id)
            self.writeDataReference(16, 43)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[43].id)
            self.writeDataReference(16, 44)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[44].id)
            self.writeDataReference(16, 45)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[45].id)
            self.writeDataReference(16, 46)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[46].id)
            self.writeDataReference(16, 47)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[47].id)
            self.writeDataReference(16, 48)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[48].id)
            self.writeDataReference(16, 49)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[49].id)
            self.writeDataReference(16, 50)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[50].id)
            self.writeDataReference(16, 0)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[51].id)
            self.writeDataReference(16, 52)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[52].id)
            self.writeDataReference(16, 53)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        try:
            print(pl.brawlers[53].id)
            self.writeDataReference(16, 54)
            self.writeVInt(2)
        except IndexError:
            pass
        else:
            pass

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(-1)  # Diamonds
        self.writeVInt(0)  # Free Diamonds
        self.writeVInt(player.Level)  # Player Level
        self.writeVInt(100)
        self.writeVInt(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(0)  # Battle Count
        self.writeVInt(0)  # WinCount
        self.writeVInt(0)  # LoseCount
        self.writeVInt(0)  # WinLooseStreak
        self.writeVInt(0)  # NpcWinCount
        self.writeVInt(0)  # NpcLoseCount
        self.writeVInt(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(0)

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion