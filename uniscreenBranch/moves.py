import random, dataController as dc, curses, time
dmgMod = 0
stdscr = curses.initscr()
height, width = stdscr.getmaxyx()

def enemydis(name: str):
     stdscr.move(height - 9, 0)
     stdscr.clrtoeol()
     stdscr.addstr(height - 9, 0, f"{name}: {dc.readData("Enemy health", 0)}/{dc.readData("Enemy health", 1)} health")

def talk(message: str, enemy: str, person="", input=True):
    if person != "":
        if ":" not in person:
            person = person + ":"
    stdscr.clear()
    stdscr.refresh()
    enemydis(enemy)
    stdscr.addstr(height - 3, 0, person)
    stdscr.addstr(height - 1, 0, message)
    stdscr.refresh()
    if input == True:
        k = 0
        stdscr.nodelay(True)
        k = stdscr.getch()
        while k != -1:
            k = stdscr.getch()
        while (k != 10):
            curses.curs_set(0)
            k = stdscr.getch()
    stdscr.nodelay(False)

def menu(options: list, back: bool, message="", person="") -> int:
    if person != "":
        if ":" not in person:
            person = person + ":"
    stdscr.refresh()
    k = 0
    optionsBackup = []
    loc = 0
    if back == True:
        options.append("Back")
    for x in range(len(options)):
        optionsBackup.append(options[loc])
        loc = loc + 1
    optionsBackup[0] = "[" + optionsBackup[0] + "]"
    menu = ""
    for i in optionsBackup:
        menu = menu + i + " "
     
    stdscr.move(height - 5, 0)
    stdscr.clrtoeol()
    stdscr.move(height - 3, 0)
    stdscr.clrtoeol()
    stdscr.move(height - 1, 0)
    stdscr.clrtoeol()
    stdscr.addstr(height - 5, 0, person)
    stdscr.addstr(height - 3, 0, message)
    stdscr.addstr(height - 1, 0, menu)
    stdscr.refresh()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)
    loc = 0
    while True:
        stdscr.refresh()
        k = stdscr.getch()
        if k == curses.KEY_RIGHT:
            temp = ""
            optionsBackup.remove("[" + options[loc] + "]")
            optionsBackup.insert(loc, options[loc])
            try:
                loc = loc + 1
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
            except:
                optionsBackup = []
                loc = 0
                for x in range(len(options)):
                    optionsBackup.append(options[loc])
                    loc = loc + 1
                loc = 0
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
            menu = ""
            for i in optionsBackup:
                menu = menu + i + " "
            
            stdscr.addstr(height - 1, 0, menu)
            stdscr.refresh()

        elif k == curses.KEY_LEFT:
            temp = ""
            optionsBackup.remove("[" + options[loc] + "]")
            optionsBackup.insert(loc, options[loc])
            if loc > 0:
                loc = loc - 1
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
            else:
                optionsBackup = []
                loc = 0
                for x in range(len(options)):
                    optionsBackup.append(options[loc])
                    loc = loc + 1
                loc = len(options) - 1
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
            menu = ""
            for i in optionsBackup:
                menu = menu + i + " "
            
            stdscr.addstr(height - 1, 0, menu)
            stdscr.refresh()
        
        elif k == 127:
            if back == True:
                loc = len(options) - 1
                optionsBackup = []
                loc = 0
                for x in range(len(options)):
                    optionsBackup.append(options[loc])
                    loc = loc + 1
                loc = len(options) - 1
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
                menu = ""
                for i in optionsBackup:
                    menu = menu + i + " "

                stdscr.addstr(height - 1, 0, menu)
                stdscr.refresh()
        
        if k == 10:
            return loc

def sword(enemy: str):
     global dmg, dmgMod
     dmgMod = 0
     if dc.readData("Loadout", 0) == 1:
        dmg = dc.readMove("Sword", 0)
        primary = "sword"
        hitchance = dc.readMove("Sword", 1)
     elif dc.readData("Loadout", 0) == 2:
        dmg = dc.readMove("Dagger", 0)
        primary = "dagger"
        hitchance = dc.readMove("Dagger", 1)
     elif dc.readData("Loadout", 0) == 3:
        dmg = dc.readMove("Great Axe", 0)
        primary = "great axe"
        hitchance = dc.readMove("Great Axe", 1)
     if dc.readMove("Rage", 0) == 1:
          dmgMod = dmgMod + 2
     dmg = dmg + dmgMod
     if random.randint(1, 100) <= hitchance:
        dc.manipData("Enemy health", 0, dmg, "-")
        if dc.readData("Enemy health", 0) <= 0:
            dc.setData("Enemy health", 0, 0)
            talk(f"You dealt {dmg} damage to the enemy, killing them", enemy=enemy)
        else:
            talk(f"You dealt {dmg} damage to the enemy, lowering them to {dc.readData("Enemy health", 0)} health", enemy=enemy)
            dc.setData("Triggers", 0, 1)
            return f"Player: Attacked with {primary}, dealing {dmg} damage"
     else:
          talk("You missed", enemy=enemy)
          dc.setData("Triggers", 0, 1)
          return f"Player: Missed attack with {primary}"

def agility(enemy: str):
    if dc.readData("Loadout", 0) == 1:
        weapon = "Sword"
    elif dc.readData("Loadout", 0) == 2:
        weapon = "Dagger"
    elif dc.readData("Loadout", 0) == 3:
        weapon = "Great Axe"
    if dc.readData("MP", 0) < dc.readMove("Agility", 1):
         talk("You do not have enough MP", enemy=enemy)
         action = None
    else:
        if dc.readMove(weapon, 1) >= 100:
                talk("Your hit chance is at the max and cannot be increased anymore", enemy=enemy)
                action = None
                dc.setData("Triggers", 0, 1)
        else:
            if dc.readMove(weapon, 1) == 90:
                dc.setMove(weapon, 1, 100)
                dc.manipData("MP", 0, dc.readMove("Agility", 1), "-")
                talk("You raised your hit chance to max", enemy=enemy)
            else:
                dc.manipMove(weapon, 1, dc.readMove("Agility", 0), "+")
                dc.manipData("MP", 0, dc.readMove("Agility", 1), "-")
                dc.manipMove("Agility", 1, 2, "*")
                talk("You raised your hit chance by 10", enemy=enemy)
            action = None
            dc.setData("Triggers", 0, 1)

def shield(enemy: int):
    if dc.readData("MP", 0) < dc.readMove("Shield", 1):
         talk("You do not have enough MP\n", enemy=enemy)
         action = None
    else:
        if dc.readEnemy(enemy, 4) == 10:
                talk(f"The {enemy}'s hit chance is at the lowest it can be and cannot be decreased anymore", enemy=enemy)
                action = None
                dc.setData("Triggers", 0, 1)
        else:
                if dc.readEnemy(enemy, 4) == 15:
                    dc.setEnemy(enemy, 4, 10)
                    dc.manipData("MP", 0, dc.readMove("Shield", 1), "-")
                    talk(f"You lowered the {enemy}'s hit chance to the lowest", enemy=enemy)
                else:
                    dc.manipEnemy(enemy, 4, 5, "-")
                    dc.manipData("MP", 0, dc.readMove("Shield", 1), "-")
                    dc.manipMove("Shield", 1, 3, "+")
                    talk(f"You lowered the {enemy}'s hit chance by 5", enemy=enemy)
                action = None
                dc.setData("Triggers", 0, 1)

def fireball(enemyname: str):
    global dmg, dmgMod
    dmgMod = 0
    if dc.readData("MP", 0) >= 6:
        dc.manipData("MP", 0, 6, "-")
        if random.randint(1, 100) > dc.readMove("Fireball", 2):
            talk("You missed", enemyname)
            action = None
            dc.setData("Triggers", 0, 1)
        else:
            dmg = int(dc.readMove("Fireball", 0))
            dmg = dmg + dmgMod
            dc.manipData("Enemy health", 0, dmg, "-")
            if dc.readData("Enemy health", 0) <= 0:
                dc.setData("Enemy health", 0, 0)
                talk(f"You dealt {dmg} fire damage to the {enemyname}, killing them", enemyname)
                action = None
            else:
                talk(f"You cast fireball at the enemy dealing {dmg} fire damage, knocking the {enemyname} down to {dc.readData("Enemy health", 0)} health. Residual damage for 1 turn is also applied", enemyname)
                dc.setMove("Fireball", 1, 1)
                action = None
                dc.setData("Triggers", 0, 1)
    else:
        talk("You do not have enough mp to use this action", enemyname)

#Rage
def rage(enemy: str):
    if dc.readMove("Rage", 0) == 1:
        if menu(["Yes", "No"], False, f"Do you want to disable rage? ({dc.readData("MP", 0)}/{dc.readData("MP", 1)} MP left)"):
            dc.setMove("Rage", 0, 0)
            talk("Rage is deactivated", enemy=enemy)
            dc.setData("Triggers", 0, 1)
        else:
            return
    else:
        if dc.readData("MP", 0) >= 3:
                dc.setMove("Rage", 0, 1)
                dc.manipData("MP", 0, 2, "-")
                talk("Rage activated", enemy=enemy)
                action = None
                dc.setData("Triggers", 0, 1)
        else:
                talk("You do not have sufficient MP", enemy=enemy)
                action = None

def gun(enemy: str):
    talk("3", enemy=enemy, input=False)
    time.sleep(1)
    talk("2", enemy=enemy, input=False)
    time.sleep(1)
    talk("1", enemy=enemy, input=False)
    time.sleep(1)
    talk("Fire!", enemy=enemy, input=False)
    delta = 0
    dmgMod = 0
    k = 0
    stdscr.nodelay(True)
    while delta < 10000000:
        curses.curs_set(0)
        k = stdscr.getch()
        if k == 10:
            break
        delta += 1
    if delta <= 100:
        dmg = 10
        if dc.readMove("Rage", 0) == 1:
            dmgMod = dmgMod + 2
        dmg = dmg + dmgMod
        if dmg >= dc.readData("Enemy health", 0):
            dc.setData("Enemy health", 0, 0)
            talk(f"Headshot! You dealt 10 damage, killing the {enemy}", enemy=enemy)
        else:
            dc.manipData("Enemy health", 0, dmg, "-")
            talk(f"Headshot! You dealt 10 damage to the {enemy}", enemy=enemy)
    elif delta <= 100000:
        dmg = 8
        if dc.readMove("Rage", 0) == 1:
            dmgMod = dmgMod + 2
        dmg = dmg + dmgMod
        if dmg >= dc.readData("Enemy health", 0):
            dc.setData("Enemy health", 0, 0)
            talk(f"You got a body shot, dealing 8 damage, and killing the {enemy}", enemy=enemy)
        else:
            dc.manipData("Enemy health", 0, dmg, "-")
            talk(f"You got a body shot, dealing 8 damage to the {enemy}", enemy=enemy)
    elif delta <= 9999999:
        dmg = 5
        if dc.readMove("Rage", 0) == 1:
            dmgMod = dmgMod + 2
        dmg = dmg + dmgMod
        if dmg >= dc.readData("Enemy health", 0):
            dc.setData("Enemy health", 0, 0)
            talk(f"You got a limb shot, dealing 5 damage, and killing the {enemy}", enemy=enemy)
        else:
            dc.manipData("Enemy health", 0, dmg, "-")
            talk(f"You got a limb shot, dealing 5 damage to the {enemy}", enemy=enemy)
    else:
        talk("You missed", enemy=enemy)
    stdscr.nodelay(False)