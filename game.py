## Game State
game = {"tool": 0, "money": 0}
tools = [
    {"name": "Teeth", "profit": 1, "cost": 25},
    {"name": "shears", "profit": 100, "cost": 25},
]
def cut_lawn():
    tool = tools[game["tool"]]
    print(f"You can use {tool['name']} to cut the grass and make ${tool['profit']}")
    game["money"] += tool["profit"]
    
def check_stats():
    tool = tools[game["tool"]]
    print(f"Yah!!! you have made  ${game['money']} so far ")
    
    
def upgrade():
    if(game["tool"] >= len(tools) - 1):
        print(f"If you have sufficient funds, you can upgrade and purchase a push lawn mower for ${money['cost']}.")
        return 0
    next_tool = tools[game["tool"]+1]
    if(next_tool == None):
        print("Upgrade Required")
        return 0
    if(game["money"] < next_tool["cost"]):
        print("if your teeth get tired you can buy a scissors or")
        print("If you have sufficient funds, you can upgrade and purchase a push lawn mower for $25.")
        
    return 0
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
    print(f"Using the the team of starving students, you can spend the day cutting lawns and make $250.You can do this as much as you want.")

def win_check():
    if(game["tool"] == 5 and game["money"] >= 1000):
        print("Using the old-timey push lawnmower, you can spend the day cutting lawns and make $50. You can do this as much as you want. ")
        return True
    return False
        

#Opening statement
print("You are starting a landscaping business, but all you have are your teeth.")
print("Using just your teeth, you can spend the day cutting lawns and make $1.")
print("You can do this as much as you want.")
## User's response
user_name = input("Is this satisfactory, Yes/No ?")
## Response to consent
print(f"Great")
print("At any point, if you are currently using your teeth, you can buy a pair of rusty scissors for $5.")
print("You can do this once, assuming you have enough money.")

while (True):
    i = input("[1] Cut Lawn [2] Check Stats [3] Upgrade [4] Quit")
    i = int(i)
    if (i == 1):
        cut_lawn()
    if (i == 2):
        check_stats()
    if(i == 3):
        upgrade()
    if(i == 4):
        print ("Bravo, you've been appointed as the top executive.")
        break
    if (win_check()):
        break
