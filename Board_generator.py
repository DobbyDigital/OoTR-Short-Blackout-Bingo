from random import seed,shuffle, randint, choice
from functools import partial
import tkinter as tk


outfile="Testing"+".txt"

class GoalList():
    def __init__(self):
        self.GoalTypeSpread5x5=[
            [[1,0,0,1,1],[1,0,0,1,0],[1,1,0,0,1],[0,1,1,1,0],[0,1,1,0,0]],
            [[0,0,1,0,1],[1,1,0,1,0],[0,1,0,1,1],[1,0,0,1,0],[1,0,1,0,0]],
            [[1,0,1,0,0],[0,0,1,1,1],[0,1,0,0,1],[0,1,1,0,0],[1,0,0,1,1]],
            [[0,1,0,1,0],[1,0,0,1,0],[0,1,1,0,1],[0,0,0,1,1],[1,1,1,0,0]],
            [[1,1,0,1,0],[1,0,0,1,1],[0,0,1,1,0],[1,0,1,0,1],[0,1,1,0,0]],
            [[0,0,0,1,1],[1,1,0,0,0],[1,0,1,1,0],[1,0,1,0,1],[0,1,1,0,1]],
            [[0,1,0,1,1],[1,1,0,0,1],[1,0,1,1,0],[0,0,0,1,1],[1,1,1,0,0]],
            [[1,0,1,0,1],[0,1,1,0,0],[0,1,0,1,0],[0,1,0,0,1],[1,0,1,1,0]],
            [[0,1,1,1,0],[1,1,0,1,0],[0,1,1,0,0],[1,0,0,0,1],[0,0,1,1,1]],
            [[0,1,0,1,0],[1,0,0,1,0],[0,1,1,0,1],[1,0,1,0,0],[0,0,0,1,1]]
            ]
        self.GoalTypeSpread4x4=[
            [[1,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,1]],
            [[0,1,0,1],[1,0,1,0],[1,0,1,0],[0,1,0,1]],
            [[1,0,1,0],[0,1,0,1],[0,1,0,1],[1,0,1,0]],
            [[1,1,0,0],[0,0,1,1],[0,0,1,1],[1,1,0,0]],
            [[0,1,0,1],[0,1,0,1],[1,0,1,0],[1,0,1,0]],
            [[0,0,1,1],[1,1,0,0],[0,0,1,1],[1,1,0,0]],
            [[1,0,1,0],[0,0,1,1],[1,1,0,0],[0,1,0,1]],
            [[0,0,1,1],[1,1,0,0],[1,1,0,0],[0,0,1,1]],
            [[0,0,1,1],[0,1,0,1],[1,0,1,0],[1,1,0,0]],
            [[1,0,1,0],[0,1,0,1],[0,1,0,1],[1,0,1,0]],
            ]

        self.DoGoalList=[
            "VISITALLADULT|1 Skulltula from 3 different Adult Dungeons",
            "VISITALLCHILD|1 Skulltula from each Child Dungeon",
            "VISITALLADULT|Obtain 1 Small Key in 3 different Adult Dungeons",
            "All 3 Kokiri Forest area Skulltulas",
            "All 3 Skulltulas in Bottom of the Well",
            "All 3 Skulltulas in Ice Cavern",
            "All 4 Gerudo Valley area Skulltulas",
            "All 4 Lon-Lon Ranch area Skulltulas",
            "All 4 Lost Woods area Skulltulas",
            "DEKUSKULLS|ALLDUNGEONSKULLS|All 4 Skulltulas in Deku Tree",
            "JABUSKULLS|ALLDUNGEONSKULLS|All 4 Skulltulas in Jabu-Jabu",
            "All 4 Wasteland/ Colossus area Skulltulas",
           "LAKEHYLIA|3 Lake Hylia Skulltulas",
            "DODONGOSKULLS|ALLDUNGEONSKULLS|All 5 Skulltulas in Dodongo's Cavern",
           "FIRESKULLS|3 Skulltulas in Fire Temple",
            "FIRESKULLS|ALLTEMPLESKULLS|All 5 Skulltulas in Fire Temple",
            "FORESTSKULLS|3 Skulltulas in Forest Temple",       
            "FORESTSKULLS|ALLTEMPLESKULLS|All 5 Skulltulas in Forest Temple",
           "SHADOWSKULLS|3 Skulltulas in Shadow Temple",
            "SHADOWSKULLS|ALLTEMPLESKULLS|All 5 Skulltulas in Shadow Temple",
           "SPIRITSKULLS|3 Skulltulas in Spirit Temple",
            "SPIRITSKULLS|ALLTEMPLESKULLS|All 5 Skulltulas in Spirit Temple",
           "WATERSKULLS|3 Skulltulas in Water Temple",
            "DEATHMOUNTAINSKULLS|All 8 Death Mountain area Skulltulas",
            "DEATHMOUNTAINSKULLS|ALLOVERWORLDSKULLS|All 8 Death Mountain area Skulltulas",
            "KAKARIKOSKULLS|6 Kakariko area Skulltulas",
            "KAKARIKOSKULLS|ALLOVERWORLDSKULLS|All 8 Kakariko area Skulltulas",
            "DOMAINSKULLS|6 Zora's Domain area Skulltulas",
            "DOMAINSKULLS|ALLOVERWORLDSKULLS|All 8 Zora's Domain area Skulltulas",
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
            "FIRETEMPLE|Free 7 Different Gorons in Fire Temple",
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
           "IRONKNUCKLE|Defeat 4 Different Iron Knuckles",
           "GANONSCASTLE|Get to the end of Fire Trial",
           "GANONSCASTLE|Get to the end of Forest Trial",
           "GANONSCASTLE|Get to the end of Light Trial",
           "GANONSCASTLE|Get to the end of Shadow Trial",
           "GANONSCASTLE|Get to the end of Spirit Trial",
            "EPONA|Cow in House",
            "Defeat a Skull Kid",
            "GTG|Gerudo's Card",
            "MASK|Spooky Mask",
            "BEANS|Plant bean in Death Mountain Crater",
            "Win A Bombchu Bowling Prize",
           "SKULLREWARD|Collect the reward for 10 skulltula tokens",
           "SKULLREWARD|Collect the reward for 20 skulltula tokens",
           "Collect the song/item from Sheik at Colossus",
           "Collect the item/song from the pot in Goron City",
           "Collect the item/song from Deku Theatre Skull Mask",
           "SILVERRUPEES|Complete 3 Silver Rupee Rooms",
           "SILVERRUPEES|Complete 4 Silver Rupee Rooms",
           "Defeat 3 Different Big Poes",
           "Defeat 4 Different Like-Likes",
           "Open Shadow Temple",
            "SPIRITTEMPLE|Defeat 2 Iron Knuckles in Spirit Temple",
            "Defeat both Dead Hands"
            ]

        self.FindGoalList=[
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
                "SONGS|At least 4 warpsongs",        
                "HEARTS|9 Hearts",
                "HEARTS|10 Hearts",
               "FORESTKEYS|Obtain 4 Different Keys in Forest Temple",
               "FORESTKEYS|MAXKEYS|Obtain all 5 Small Keys in Forest Temple",
               "WATERKEYS|Obtain 4 Different Small Keys in Water Temple",
               "SHADOWKEYS|Obtain 4 Different Small Keys in Shadow Temple",
               "SHADOWKEYS|MAXKEYS|Obtain all 5 Small Keys in Shadow Temple",
               "FIREKEYS|Obtain 6 Different Small Keys in Fire Temple",
               "FIREKEYS|MAXKEYS|Obtain all 8 Small Keys in Fire Temple",
                "BOTTLE|Bottle of Blue Fire",
               "BOTTLE|Bottled Fairy",
               "BOTTLE|EPONA|Bottle of Milk",
               "BOTTLE|Find Ruto's Letter",
                "Double Defense OR Double Magic",
                "FAIRYSPELL|At least two Fairy Spells",
                "Fall Prey to 3 Ice Traps",
               "ELEMENTALARROWS|At least 2 Elemental Arrows",
               "BOW|QUIVER|SLINGSHOT|Quiver 50 OR Bullet Bag 50"
                ]

class SeedGUI():
    def __init__(self, master):
        self.seed=tk.StringVar()
        self.master=master
        self.mode=tk.StringVar()
        self.mode.set("window")
        print("Generating default seed")
        randomSeed=randint(10000000, 99999999)
        print("Default seed generated")
        self.seed.set(str(randomSeed))
        self.outfile=tk.StringVar()
        self.outfile.set("Board_"+str(self.seed.get()))
        self.boardSize=tk.StringVar()
        self.boardSize.set("5")

        self.master.title("Seed for board generation")
        
        self.SeedLabel=tk.Label(self.master, text="Enter an integer seed for the board randomisation:")
        self.SeedBox=tk.Entry(self.master, textvariable=self.seed)
        self.SeedLabel.grid(row=1, column=1)
        self.SeedBox.grid(row=1, column=2)

        self.boardSizeLabel=tk.Label(self.master, text="What side length of board (i.e. '4' for a 4x4 board)")
        self.boardSizeLabel.grid(row=2, column=1)
        self.boardSizeBox=tk.Entry(self.master, textvariable=self.boardSize)
        self.boardSizeBox.grid(row=2, column=2)
        
        self.ModeLabel=tk.Label(self.master, text="Create JSON file instead of window?")
        self.JSONModeCheck=tk.Checkbutton(self.master, variable = self.mode, \
                         onvalue = "JSON", offvalue ="window", height=1, \
                         width = 10)
        self.ModeLabel.grid(row=3, column=1)
        self.JSONModeCheck.grid(row=3, column=2)
        
        self.OutfileLabel=tk.Label(self.master, text="What filenameshould be used for the JSON file (if applicable)")
        self.OutfileBox=tk.Entry(self.master, textvariable=self.outfile)
        self.OutfileLabel.grid(row=4, column=1, rowspan=2)
        self.OutfileBox.grid(row=4,column=2, rowspan=1)
        self.GenerateBoardButton=tk.Button(self.master, text="Generate board", command=self.VerifySeed)
        self.GenerateBoardButton.grid(row=6, column=1, columnspan=2)

    def VerifySeed(self):
        try:
            self.seed=int(self.seed.get())
            self.boardSize=int(self.boardSize.get())
        except:
            self.ErrorLabel=tk.Label(self.master, text="Error importing seed. Verify seed and board size are integer")
            self.ErrorLabel.grid(row=1, column=3)
            return
        self.master.destroy()
        
def UpdateIndex(i,j,boardSize):
    j+=1
    if j>=boardSize:
        j=0
        i+=1
    return i,j
        
def GenerateBoard(randomisationSeed, boardSize,goalList):
    goalDict={}
    goalSet=set()
    FindGoalList=[]
    DoGoalList=[]
    goals=[]
    print("Generating board")
    for entry in goalList.DoGoalList:
        splitTags=entry.split('|')
        if len(splitTags)==1:
            goalDict[entry]=[]
        else:
            goal=splitTags[-1]
            DoGoalList.append(goal)
            tagList=splitTags[0:-1]
            goalDict[goal]=tagList
    for entry in goalList.FindGoalList:
        splitTags=entry.split('|')
        if len(splitTags)==1:
            goalDict[entry]=[]
        else:
            goal=splitTags[-1]
            FindGoalList.append(goal)
            tagList=splitTags[0:-1]
            goalDict[goal]=tagList
    seed(randomisationSeed)
    if boardSize==4:
        GoalTypeSpread=choice(goalList.GoalTypeSpread4x4)
    elif boardSize==5:
        GoalTypeSpread=choice(goalList.GoalTypeSpread5x5)
    else:
        print("Unsupported board size. Board must be 4x4 or 5x5")
        raise Exception
    shuffle(FindGoalList)
    shuffle(DoGoalList)
    i=0
    j=0
    try:
        while len(goals)<boardSize**2:
            updateIndex=True
            if GoalTypeSpread[i][j]==1:
                newGoal=FindGoalList.pop()
            else:
                newGoal=DoGoalList.pop()
            if len(goalDict[newGoal])==0:
                goals.append(newGoal)
                print("New goal added")
                i,j=UpdateIndex(i,j,boardSize)
                continue
            foundBannedTag=False
            for tag in goalDict[newGoal]:
                if tag in goalSet:
                    foundBannedTag=True
                    print("Goal excluded")
                    updateIndex=False
                    break     
            if foundBannedTag==False:
                goalSet.update(goalDict[newGoal])
                goals.append(newGoal)
                print("New goal added")
            if updateIndex:
                i,j=UpdateIndex(i,j,boardSize)
    except Exception as e:
        print(e)
        print(i)
        print(j)
        raise Exception
    return goals
        
def GenerateBoardAndData(randomisationSeed, boardSize, goalList):
    goalDict={}
    goalSet=set()
    goals=[]
    print("Generating board")
    for entry in goalList:
        splitTags=entry.split('|')
        if len(splitTags)==1:
            goalDict[entry]=[]
        else:
            goal=splitTags[-1]
            tagList=splitTags[0:-1]
            goalDict[goal]=tagList
    goalList=list(goalDict.keys())
    seed(randomisationSeed)
    shuffle(goalList)
    while len(goals)<boardSize**2:
        newGoal=goalList.pop()
        if len(goalDict[newGoal])==0:
            goals.append(newGoal)
            print("New goal added")
            continue
        for tag in goalDict[newGoal]:
            if tag in goalSet:
                print("Goal excluded")
                break
        goalSet.update(goalDict[newGoal])
        goals.append(newGoal)
        print("New goal added")
    return goals, goalDict, goalSet

class BingoGoal(tk.Button):
    def __init__(self, master, colour='white', *args, **kwargs):
        self.master=master
        self.colour=colour
        super().__init__(*args, **kwargs)
        
    def ChangeColour(self):
        if self.colour=='white':
            self.colour='red'
        elif self.colour=='red':
            self.colour='green'
        else:
            self.colour='white'
        self.config(bg=self.colour)
        self.master.update_idletasks()
            

class BingoBoard():
    def __init__(self, master, goalList, seed, boardSize):
        self.master=master
        self.goalList=goalList
        self.seed=seed
        self.boardSize=boardSize
        self.goals=GenerateBoard(self.seed, self.boardSize, self.goalList)

        self.ButtonReferences={}
        row=1
        column=1

        for goal in self.goals:
            SelectGoal=partial(self.ClickSquare, row, column)
            GoalButton=BingoGoal(master=self.master, colour='white', bg='white', height=7, width=30, wraplength=80, borderwidth=1, padx=1, pady=1,text=goal, command=SelectGoal)
            self.ButtonReferences[(row,column)]=GoalButton
            GoalButton.grid(row=row, column=column)
            column+=1
            if column>=self.boardSize+1:
                row+=1
                column=1
        self.master.update_idletasks()

    def ClickSquare(self,row, column):
        self.ButtonReferences[(row, column)].ChangeColour()

def callback():
    scriptRunning=False

def GoalListToJSON(goalList, boardSize, outfile):
    with open(outfile, "w+") as f:
        f.write('Goal list (copy-paste the block below into a custom Bingosync board): \n')
        f.write("\n")
        f.write("[")
        if boardSize==5:
            for i in range(len(goalList)-1):
                f.write('{"name":"'+goalList[i]+'"}, \n')
            f.write('{"name":"'+goalList[-1]+'"} \n')
        elif boardSize==4:
            j=0
            for i in range(len(goalList)):
                f.write('{"name":"'+goalList[i]+'"}, \n')
                j+=1
                if j==4:
                   f.write('{"name":" "}, \n')
                   j=0    
            for _ in range(4):
                f.write('{"name":" "}, \n')
            f.write('{"name":" "} \n')
        f.write(']')



master=tk.Tk()
bingoList=GoalList()
seedGUIWindow=tk.Toplevel()
seedGUI=SeedGUI(seedGUIWindow)
master.wait_window(seedGUI.master)
if seedGUI.mode.get()=='JSON':
    goals=GenerateBoard(seedGUI.seed, seedGUI.boardSize,bingoList)
    GoalListToJSON(goals, seedGUI.boardSize, seedGUI.outfile.get()+'.txt')
    print("JSON file created!")
elif seedGUI.mode.get()=='window':
    Notebook=tk.Toplevel()
    Board=BingoBoard(Notebook, bingoList, seedGUI.seed,seedGUI.boardSize)
    master.wait_window(Board.master)
else:
    print("Error reading game mode:")


    


            

