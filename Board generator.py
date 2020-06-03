from random import seed,shuffle, randint
import tkinter as tk

GoalList=[
	"VISITALLADULT|1 Skulltula from 3 different Adult Dungeons",
	"VISITALLCHILD|1 Skulltula from each Child Dungeon",
	"VISITALLADULT|Obtain 1 Small Key in 3 different Adult Dungeons",
       "DUNGEONS|DEKUBOSS|DODONGOBOSS|FORESTBOSS|WATERBOSS|SHADOWBOSS|2 Stones",
       "DUNGEONS|DEKUBOSS|DODONGOBOSS|FORESTBOSS|WATERBOSS|SHADOWBOSS|3 Medallions",
       "DUNGEONS|DEKUBOSS|DODONGOBOSS|FORESTBOSS|WATERBOSS|SHADOWBOSS|4 Medallions",
       "DUNGEONS|FORESTBOSS|WATERBOSS|SHADOWBOSS|Beat 2 adult dungeons",
	"FIBK|FOBK|SHBK|SPBK|WBK|GBK|2 Boss Keys",
       "FIRETEMPLE|FIBK|Fire Temple Boss Key",
       "FORESTTEMPLE|FOBK|Forest Temple Boss Key",
       "WBK|Water Temple Boss Key",
       "SHBK|Shadow Temple Boss Key",
       "SPBK|Spirit Temple Boss Key",
       "GBK|Ganon's Castle Boss Key",
	"BOOTS|At least 2 Boots",
	"SHIELDS|At least 2 Shields",
	"SWORDS|WALLET|3rd Sword Slot Occupied",
       "TUNICS|WALLET|Goron Tunic",
       "TUNICS|WALLET|GIANTSWALLET|Zora Tunic",
	"COMPASSES|4 Compasses",
       "COMPASSES|5 Compasses",
	"MAPS|4 Maps",
       "MAPS|5 Maps",
       "Map & Compass in Deku Tree",
       "Map & Compass in Dodongo’s Cavern",
       "Map & Compass in Bottom of the Well",
       "Map & Compass in Forest Temple",
       "Map & Compass in Fire Temple",
       "Map & Compass in Shadow Temple",
       "Map & Compass in Ice Cavern",
       "NUT|30 Deku Nut Capacity or Better",
       "BOMBBAG|Bomb Bag 30 or Better",
	"WALLET|GIANTSWALLET|500 Rupees",
       "WALLET|GIANTSWALLET|Giant's Wallet or better",
       "SLINGSHOT|Fairy Slingshot",
       "SLINGSHOT|Bullet Bag 40 or Better",
       "DEKUSTICK|20 Deku Stick Capacity or Better",
       "BOW|QUIVER|Fairy Bow",
       "BOW|QUIVER|Quiver 40 or Better",
       "STRENGTH|Goron Bracelet or Better",
       "STRENGTH|Silver Gauntlets or Better",
       "SCALE|Silver Scale or Better",
       "BOTTLE|Fill at least 2 Bottle Slots",
	"SONGS|5 Songs",
	"SONGS|6 Songs",
	"HEARTS|9 Hearts",
	"HEARTS|10 Hearts",
	"All 3 Kokiri Forest area Skulltulas",
	"All 3 Skulltulas in Bottom of the Well",
	"All 3 Skulltulas in Ice Cavern",
	"All 4 Gerudo Valley area Skulltulas",
	"All 4 Lon-Lon Ranch area Skulltulas",
	"All 4 Lost Woods area Skulltulas",
	"All 4 Skulltulas in Deku Tree",
	"All 4 Skulltulas in Jabu-Jabu",
	"All 4 Wasteland/ Colossus area Skulltulas",
       "LAKEHYLIA|3 Lake Hylia Skulltulas",
	"All 5 Skulltulas in Dodongo's Cavern",
       "FIRESKULLS|4 Skulltulas in Fire Temple",
	"FIRESKULLS|All 5 Skulltulas in Fire Temple",
	"All 5 Skulltulas in Forest Temple",
       "SHADOWSKULLS|4 Skulltulas in Shadow Temple",
	"SHADOWSKULLS|All 5 Skulltulas in Shadow Temple",
       "SPIRITSKULLS|4 Skulltulas in Spirit Temple",
	"SPIRITSKULLS|All 5 Skulltulas in Spirit Temple",
       "WATERSKULLS|3 Skulltulas in Water Temple",
	"All 8 Death Mountain area Skulltulas",
	"All 8 Kakariko area Skulltulas",
	"DOMAINSKULLS|All 4 Child Zora's Domain area Skulltulas",
	"DOMAINSKULLS|All 4 Adult Zora's Domain area Skulltulas",
       "Both Gerudo's Fortress area Skulltulas",
       "All 4 Adult Zora's Domain area Skulltulas",
       "All 4 Child Zora's Domain area Skulltulas",      
       "Both Hyrule Field area Skulltulas",
       "4 Soft Soil Skulltulas",
	"DODONGOBOSS|Beat Dodongo's Cavern",
	"DEKUBOSS|Beat the Deku Tree",
	"FORESTBOSS|Beat the Forest Temple",
	"SHADOWBOSS|Beat the Shadow Temple",
	"WATERBOSS|Beat the Water Temple",
       "FORESTTEMPLE|Defeat Amy (Green Poe)",
       "GTG|ICECAVERN|Defeat a White Wolfos",
       "DODONGOSCAVERN|LIZALFOS|Defeat all Lizalfos in Dodongo's Cavern",
       "SPIRITTEMPLE|LIZALFOS|Defeat all Lizalfos in Spirit Temple",
       "JABUJABUSBELLY|Defeat Big Octo",
       "SHADOWBOSS|Defeat Bongo-Bongo",
       "FIRETEMPLE|Defeat both Flare Dancers",
       "WATERTEMPLE|Defeat Dark Link",
       "DODONGOBOSS|Defeat King Dodongo",
       "FORESTTEMPLE|Defeat Meg (purple Poe)",
       "WATERBOSS|Defeat Morpha",
       "IRONKNUCKLE|SPIRITBOSS|Defeat Nabooru-Knuckle",
       "FORESTBOSS|Defeat Phantom Ganon",
       "DEKUBOSS|Defeat Queen Gohma",
       "FORESTKEYS|Obtain 4 Different Keys in Forest Temple",
       "FORESTKEYS|Obtain all 5 Small Keys in Forest Temple",
       "WATERKEYS|Obtain 4 Different Small Keys in Water Temple",
       "SHADOWKEYS|Obtain 4 Different Small Keys in Shadow Temple",
       "SHADOWKEYS|Obtain all 5 Small Keys in Shadow Temple",
       "FIREKEYS|Obtain 6 Different Small Keys in Fire Temple",
       "FIREKEYS|Obtain all 8 Small Keys in Fire Temple",
       "IRONKNUCKLE|Defeat 4 Different Iron Knuckles",
       "FIRETEMPLE|Free all 9 Gorons in Fire Temple",
       "GANONSCASTLE|Get to the end of Fire Trial",
       "GANONSCASTLE|Get to the end of Forest Trial",
       "GANONSCASTLE|Get to the end of Light Trial",
       "GANONSCASTLE|Get to the end of Shadow Trial",
       "GANONSCASTLE|Get to the end of Spirit Trial",
       "GTG|Obtain 4 Different Keys in Gerudo Training Grounds",
       "GTG|Obtain 5 Different Keys in Gerudo Training Grounds",
	"BOTTLE|Bottle of Blue Fire",
       "BOTTLE|Bottled Fairy",
       "BOTTLE|EPONA|Bottle of Milk",
       "BOTTLE|Find Ruto's Letter",
	"SONG|Bolero of Fire",
       "SONG|Requiem of Spirit",
       "SONG|Saria's Song",
       "SONG|Minuet of Forest",
       "SONG|EPONA|Epona's Song",
	"EPONA|Cow in House",
	"Defeat a Skull Kid",
	"Double Defense OR Double Magic",
	"GTG|Gerudo's Card",
	"MASK|Spooky Mask",
	"BEANS|Plant bean in Death Mountain Crater",
	"FAIRYSPELL|At least two Fairy Spells",
	"Win A Bombchu Bowling Prize",
	"Fall Prey to 3 Ice Traps",
	"Find the Randomised Green Rupee",
       "SKULLREWARD|Collect the reward for 10 skulltula tokens",
       "SKULLREWARD|Collect the reward for 20 skulltula tokens",
       "Collect the song/item from Sheik at Colossus",
       "Collect the item/song from the pot in Goron City",
       "Collect the item/song from Deku Theatre Skull Mask",
       "SILVERRUPEES|Complete 3 Silver Rupee Rooms",
       "SILVERRUPEES|Complete 4 Silver Rupee Rooms",
       "ELEMENTALARROWS|At least 2 Elemental Arrows",
       "Defeat 3 Different Big Poes",
       "Defeat 4 Different Like-Likes",
       "Open Shadow Temple",
        ]

class SeedGUI():
    def __init__(self, master):
        self.seed=StringVar()
        randomSeed=randint(10000000, 99999999)
        self.seed.set(str(randomSeed))

        self.master.title("Seed for board generation")
        self.SeedLabel=Label(self.master, text="Enter an integer seed for the board randomisation:")
        self.SeedBox=Entry(self.master, textvariable=self.seed, state=NORMAL)
        self.SeedLabel.grid(row=1, column=1)
        self.SeedBox.grid(row=1, column=2)
        self.GenerateBoardButton=Button(self.master, text="Generate board", command=self.VerifySeed)
        self.GenerateBoardButton.grid(row=3, column=1, columnspan=2)

    def VerifySeed(self):
        try:
            self.seed=int(self.seed.get())
        except:
            self.ErrorLabel=Label(self.master, text="Error importing seed. Verify seed is integer")
            self.ErrorLabel.grid(row=1, column=3)
            return
        self.master.destroy()
        
        
        
def GenerateBoard(randomisationSeed, goalList):
    goalDict={}
    goalSet=set()
    goals=[]
    for entry in goalList:
        splitTags=entry.split('|')
        if len(splitTags)==1:
            goalDict[entry]=[]
        else:
            goal=splitTags[-1]
            tagList=splitTags[0:-1]
            goalDict[goal]=tagList
    seed(randomisationSeed)
    shuffle(goalList)
    while len(goals)<25:
        newGoal=goalList.pop()
        if len(goalDict[newGoal])==0:
            goals.append(newGoal)
            continue
        for tag in goalDict[newGoal]:
            if tag in goalSet:
                continue
        goalSet.update(goalDict[newGoal])
        goals.append(newGoal)
    return goals
        
        
    
            

