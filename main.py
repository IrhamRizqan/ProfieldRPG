import os
import random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False


HP = 100
MAXHP = HP
ATK = 5
pot = 2
elix = 2
gold = 0
x = 0
y = 0

# map = [["tile1"],["tile2"],["tile1"],
#        ["tile2"],["tile3"],["tile1"],
#        ["tile3"],["tile3"],["tile3"]]

        # x = 0     x = 1      x = 2        x = 3       x = 4       x = 5          x = 6
map = [["Plains",  "Plains",   "Plains",   "Plains",  "Forest", "Mountain",       "Cave"],  # y = 0
       ["Forest",  "Forest",   "Forest",   "Forest",  "Forest",    "Hills",   "Mountain"],  # y = 1
       ["Forest",  "Fields",   "Bridge",   "Plains",   "Hills",   "Forest",      "Hills"],  # y = 2
       ["Plains",    "Shop",     "Town",    "Major",  "Plains",    "Hills",   "Mountain"],  # y = 3
       ["Plains",  "Fields",   "Fields",   "Plains",   "Hills", "Mountain",   "Mountain"]]  # y = 4

y_len = len(map)-1
x_len = len(map[0])-1
biome = {
    "Plains": {
        "t": "Plains",
        "e": True},
    "Forest": {
        "t": "Forest",
        "e": True},
    "Fields": {
        "t": "Fields",
        "e": False},
    "Town": {
        "t": "Town",
        "e": False},
    "Hills": {
        "t": "Hills",
        "e": True},
    "Mountain": {
        "t": "Mountain",
        "e": True},
    "Cave": {
        "t": "Cave",
        "e": True},
    "Shop": {
        "t": "Shop",
        "e": False},
    "Bridge": {
        "t": "Bridge",
        "e": True},
    "Major": {
        "t": "Major",
        "e": False},
}
e_list = ["Goblin", "Dragon Bat", "Orc", "Ogre"]
mobs = {
    "Goblin": {
        "HP": 15,
        "ATK": 3,
        "Gold": 3
    },
    "Dragon Bat": {
        "HP": 20,
        "ATK": 4,
        "Gold": 5
    },
    "Orc": {
        "HP": 35,
        "ATK": 5,
        "Gold": 8
    },
    "Ogre": {
        "HP": 50,
        "ATK": 7,
        "Gold": 15
    },
}

def clear():
    os.system("cls")

def draw():
    print("<>-----------------------<>")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key),
        str(fight),
        str(standing),
    ]
    
    filename = f"proField_{name}"
    f = open(filename, "w")
    
    for item in list:
        f.write(item + "\n")
    f.close()

def heal(amount):
    global HP, pot, elix, gold
    if HP + amount < MAXHP:
        HP += amount
    else:
        HP = MAXHP
    print("You've been healed to ", str(HP), "!")

def battle():
    global fight, play, run, HP, pot, elix, gold, boss
    
    
    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Yogg-Saron"
    hp = mobs[enemy]["HP"]
    hpmax = HP
    atk = mobs[enemy]["ATK"]
    enemyGold = mobs[enemy]["Gold"]
    
    while fight:
        clear()
        draw()
        print(f"You are facing {enemy}!")
        draw()
        print(enemy ,"'s HP: ", str(hp), "/", str(hpmax))
        print("Your HP: ", str(HP), "/", str(MAXHP))
        print("Potion: ", str(pot))
        print("Elixir: ", str(elix))
        draw()
        print("1. Attack")
        if pot > 0:
            print("2. Use Potion (10 HP)")
        if elix > 0:
            print("3. Use Elixir (30 HP)")
        draw()
        
        choise = input("> ")
        
        match choise:
            case "1":
                hp -= ATK
                print("You dealt ", str(ATK), " damage to ", enemy, " !")
                if hp > 0:
                    HP -= atk
                    print(enemy, " dealt ", str(atk), " damage to you !")
                input("> ")
            case "2":
                if pot > 0:
                    pot -= 1
                    heal(10)
                    HP -= atk
                    print(enemy, " dealt ", str(atk), " damage to you !")
                else:
                    print("You don't have any Potions!")
                input("> ")
            case "3":
                if elix > 0:
                    elix -= 1
                    heal(30)
                    HP -= atk
                    print(enemy, " dealt ", str(atk), " damage to you !")
                else:
                    print("You don't have any Elixirs!")
                input("> ")
            case "4":
                pass
            
        if HP <= 0:
            clear()
            print("You died!")
            draw()
            fight = False
            play = False
            run = False
            print("Game Over!")
            input("> ")
            quit()
        
        if hp <= 0:
            clear()
            print("You defeated ", enemy, " !")
            draw()
            fight = False
            gold += enemyGold
            print("You've Found ", str(enemyGold), " Gold!")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've Found a Potion!")
            if enemy == "Yogg-Saron":
                draw()
                print("Congratulations! You defeated the Boss")
                boss = False
                play = False
                run = False
            input("> ")
            clear()
            
def shop():
    global buy, gold, pot, elix, ATK
    
    while buy:
        clear()
        draw()
        print("Welcome to the shop!")
        draw()
        print("Gold: ", str(gold))
        print("Potion: ", str(pot))
        print("Elixir: ", str(elix))
        print("ATK: ", str(ATK))
        draw()
        print("1. Buy Potion 10 HP (5 Golds)")
        print("2. Buy Elixir (17 Golds)")
        print("3. Buy Weapon Upgrade +2 ATK Stats (50 Golds)")
        print("4. Leave")
        draw()
        
        choise = input("> ")
        
        match choise:
            case "1":
                if gold >= 5:
                    gold -= 5
                    pot += 1
                    print("You've bought a potion!")
                else:
                    print("You don't have enough gold!")
            case "2":
                if gold >= 17:
                    gold -= 17
                    elix += 1
                    print("You've bought an elixir!")
                else:
                    print("You don't have enough gold!")
            case "3":
                if gold >= 50:
                    gold -= 50
                    ATK += 2
                    print("You've bought a weapon upgrade!")
                else:
                    print("You don't have enough gold!")
            case "4":
                buy = False
        
def mayor():
    global speak, key
    
    while speak:
        clear()
        draw()
        print("Welcome to the mayor's office!")
        draw()
        if ATK <= 25:
            print("The mayor is a bit scared of you.")
            key = False
        else: 
            print("The mayor is a bit impressed by you.")
            key = True
        draw()
        print("1. Leave")
        
        choise = input("> ")
        match choise:
            case "1":
                speak = False
        
def cave():
    global boss, key
    
    while boss:
        clear()
        draw()
        print("You choose to woke up the Yogg-Saron")
        draw()
        if key:
            print("1. Use Key")
        print("2. Turn Back")
        draw()
        
        choise = input("> ")
        match choise:
            case "1":
                if key:
                    fight = True
                    battle()
            case "2":
                boss = False
            
while run:
    while menu:
        clear()
        draw()
        print("1. New Game")
        print("2. Load Game")
        print("3. Rules")
        print("4. Quit")
        draw()
        if rules:
            print("Rules: 1. Its Under Construction")
            rules = False
        else:
            choise = int(input("> "))
            
        match choise:
            case 1:
                clear()
                name = input("Tell me your name, Adventure. ")
                menu = False
                play = True
            case 2:
                try: 
                    f = open("proField_Irham", "r")
                    load_list = f.readlines()
                    if len(load_list) == 11:
                        name = load_list[0][:-1]
                        HP = int(load_list[1][:-1])
                        ATK = int(load_list[2][:-1])
                        pot = int(load_list[3][:-1])
                        elix = int(load_list[4][:-1])
                        gold = int(load_list[5][:-1])
                        x = int(load_list[6][:-1])
                        y = int(load_list[7][:-1])
                        key = bool(load_list[8][:-1])
                        fight = bool(load_list[9][:-1])
                        standing = bool(load_list[10][:-1])
                    else:
                        print("Corrupt Saved game")
                        menu = True
                except OSError:
                    print("No saved game found.")
                    menu = True
                clear()
                print("Hello", name, "!")
                play = True
                menu = False
                print("Press Enter")
                choise = input("> ")
                clear()
            case 3:
                rules = True
                pass
            case 4:
                print("Quitting...")
                quit()
            case _:
                print("Invalid choice. Please try again.")
                
    while play:
        save()
        clear()
        
        if not standing:
            if biome[map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()
        draw()
        print("Location: "+ biome[map[y][x]]["t"])
        print("Coord: ", x,y)
        draw()
        print("Name: ", name)
        print("HP: ", str(HP), "/", str(MAXHP))
        print("ATK: ", str(ATK))
        print("Potion: ", str(pot))
        print("Elixir: ", str(elix))
        print("Gold: ", str(gold))
        draw()
        print("0. Save and Exit")
        if y > 0:
            print("1. North")
        if x < x_len:
            print("2. East")
        if y < y_len:
            print("3. South")
        if x > 0:
            print("4. West")
        if pot > 0:
            print("5. Use Potion (10 HP)")
        if elix > 0:
            print("6. Use Elixir (30 HP)")
        if map[y][x] == "Shop" or map[y][x] == "Mayor" or map[y][x] == "Cave":
            print("7. Enter")
        draw()
        
        dest = input("> ")
        
        match dest:
            case "0":
                save()
                print("Saving....")
                print("Saved! Quiting...")
                quit()
            case "1":
                if y > 0:
                    y -= 1
                    standing = False
            case "2":
                if x < x_len:
                    x += 1
                    standing = False
            case "3":
                if y < y_len:
                    y += 1
                    standing = False
            case "4":
                if x > 0:
                    x -= 1
                    standing = False
            case "5":
                standing = True
                if pot > 0:
                    pot -= 1
                    heal(10)
                else:
                    print("No potion!")
            case "6":
                standing = True 
                if elix > 0:
                    elix -= 1
                    heal(30)
                else:
                    print("No elixir!")
            case "7":
                if map[y][x] == "Shop":
                    buy = True
                    shop()
                if map[y][x] == "Mayor":
                    speak = True
                    mayor()
                if map[y][x] == "Cave" : 
                    boss = True     
                    cave()   
            
                