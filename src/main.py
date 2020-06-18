from modules import CraftComponent, BattleComponent, ShopComponent


#Variable Declaration
startGame = ""

#Main Engine function
def MainEngine():
    engineResponse = ""
    while engineResponse != "4":
        print("Current Area: player.area / Level: player.level\n")
        print("What would you like to do?")
        print("1.Test Battle\n2.Test Craft\n3.Test Shop\n4.Exit to Main Menu")
        engineResponse = input()
        if engineResponse =="1":
            BattleComponent.BattleMenu()
        elif engineResponse == "2":
            CraftComponent.CraftMenu()
        elif engineResponse == "3":
            ShopComponent.ShopMenu()
def startMenu():
    global startGame
    print("Please select an option")
    print("1. Start Game")
    print("2. Load Game")
    print("3. Exit")
    startGame = input()
    if startGame == "1":
        print("Starting main engine....")
        MainEngine()
    elif startGame == "2":
        print("This feature is coming soon...")
    elif startGame == "3":
        print("Exiting...")

# Start running code...
print("Welcome to Soul Slasher v0.1")
while startGame != "3":
    startMenu()

