import random, moves, dataController as dc, time, curses
dmgMod = 0
stdscr = curses.initscr()
height, width = stdscr.getmaxyx()
log = []

def enemydis(name: str):
     stdscr.move(height - 9, 0)
     stdscr.clrtoeol()
     stdscr.addstr(height - 9, 0, f"{name}: {dc.readData("Enemy health", 0)}/{dc.readData("Enemy health", 1)} health")

def talk(message: str, person=""):
     if person != "":
        if ":" not in person:
            person = person + ":"
     if person != "":
          stdscr.move(height - 3, 0)
          stdscr.clrtoeol()
     stdscr.move(height - 2, 0)
     stdscr.clrtoeol()
     stdscr.move(height - 1, 0)
     stdscr.clrtoeol()
     stdscr.refresh()
     stdscr.addstr(height - 3, 0, person)
     stdscr.addstr(height - 1, 0, message)
     stdscr.refresh()
     k = 0
     while (k != 10):
          curses.curs_set(0)
          k = stdscr.getch()

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
    if person != "": 
          stdscr.move(height - 5, 0)
          stdscr.clrtoeol()
    if message != "": 
          stdscr.move(height - 3, 0)
          stdscr.clrtoeol()
    stdscr.move(height - 1, 0)
    stdscr.clrtoeol()
    if person != "":
          stdscr.addstr(height - 5, 0, person)
    if message != "": 
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


#Battle function
def battle(enemy: int, xp):
     enemyhealth = dc.readEnemy(enemy, 1)
     hitChance = dc.readEnemy(enemy, 4)
     dmgRange = [dc.readEnemy(enemy, 2), dc.readEnemy(enemy, 3)]
     dc.setData("Enemy health", 0, enemyhealth)
     dc.setData("Enemy health", 1, enemyhealth)
     if dc.readData("Loadout", 0) == 1:
          attack = "Sword"
     elif dc.readData("Loadout", 0) == 2:
          attack = "Dagger"
     elif dc.readData("Loadout", 0) == 3:
          attack = "Great Axe"
     elif dc.readData("Loadout", 0) == 4:
          attack = "Gun"
     if dc.readData("Loadout", 1) == 1:
          defend = "Shield"
     elif dc.readData("Loadout", 1) == 2:
          defend = "Agility"
     if dc.readData("Loadout", 2) == 1:
          special = "Fireball"
     elif dc.readData("Loadout", 2) == 2:
          special = "Rage"
     talk(f"You encountered a {enemy}!")
     while (dc.readData("Enemy health", 0) > 0 and dc.readData("Player health", 0) > 0):

          enemydis(enemy)
          enemyhealth = dc.readData("Enemy health", 0)
          hitChance = dc.readEnemy(enemy, 4)
          dmgRange = [dc.readEnemy(enemy, 2), dc.readEnemy(enemy, 2)]
          dc.setData("Enemy health", 0, enemyhealth)
          if dc.readMove("Rage", 0) == 1:
               dc.manipData("MP", 0, 1, "-")
          #Attack and Heal options
          action = menu(["Action", "Potions", "Info", "Log"], False, "What will you do?")
          #Action
          if action == 0:
               action = menu([f"{attack}", f"{defend}", f"{special}"], True, "Moves:")
               #Sword move
               if action == 0:
                    if attack in ["Sword", "Dagger", "Great Axe"]:
                         if len(log) == 8:
                              log.pop(4)
                         log.insert(0, moves.sword(enemy=enemy))
                         action = None
                    elif attack == "Gun":
                         moves.gun(enemy=enemy)
                         action = None

               #Shield move
               if action == 1:
                    if defend == "Shield":
                         moves.shield(enemy)
                         action = None
                    elif defend == "Agility":
                         moves.agility(enemy)
                         action = None

               #Fireball move
               if action == 2:
                    if special == "Fireball":
                         moves.fireball(enemy)
                         action = None
                    elif special == "Rage":
                         moves.rage(enemy)
                         action = None
                         
               elif action == 3:
                    stdscr.clear()
                    continue

          #Heal
          elif action == 1:
               action = menu([f"Health potions: {dc.readData("Health potions", 0)}/{dc.readData("Health potions", 1)}", f"MP potions: {dc.readData("MP potions", 0)}/{dc.readData("MP potions", 1)}"], True, f"Health: {dc.readData("Player health", 0)}/{dc.readData("Player health", 1)} | MP: {dc.readData("MP", 0)}/{dc.readData("MP", 1)}")

               #Use health potions
               if action == 0:
                    if dc.readData("Health potions", 0) <= 0:
                         talk("You don't have anymore health potions left")
                         action = None
                    else:
                         heal = dc.readData("Player health", 0) + 4
                         if dc.readData("Player health", 0) == dc.readData("Player health", 1):
                              talk("You are already at max health")
                         elif heal > dc.readData("Player health", 1):
                              if dc.readData("Player health", 0) >= (dc.readData("Player health", 0) - 3):
                                   while dc.readData("Player health", 0) != dc.readData("Player health", 1):
                                        dc.manipData("Player health", 0, 1, "+")
                                   talk("You healed to full health")
                                   dc.manipData("Health potions", 0, 1, "-")
                                   dc.setData("Triggers", 0, 1)
                                   action = None
                         elif heal < dc.readData("Player health", 1):
                              dc.manipData("Player health", 0, 4, "+")
                              dc.manipData("Health potions", 0, 1, "-")
                              talk(f"You healed to {dc.readData("Player health", 0)} health")
                              dc.setData("Triggers", 0, 1)
                              action = None
               elif action == 1:
                    if dc.readData("MP potions", 0) <= 0:
                         talk("You don't have anymore MP potions left")
                         action = None
                    else:
                         Mp = dc.readData("MP", 0) + 8
                         if dc.readData("MP", 0) == dc.readData("MP", 1):
                              talk("You are already at max MP")
                         elif Mp > dc.readData("MP", 1):
                              if dc.readData("MP", 0) >= (dc.readData("MP", 0) - 7):
                                   while dc.readData("MP", 0) != dc.readData("MP", 1):
                                        dc.manipData("MP", 0, 1, "+")
                                   talk("MP restored")
                                   dc.manipData("MP potions", 0, 1, "-")
                                   dc.setData("Triggers", 0, 1)
                                   action = None
                         elif Mp < dc.readData("MP", 1):
                              dc.manipData("MP", 0, 8, "+")
                              dc.manipData("MP potions", 0, 1, "-")
                              talk(f"MP restored to {dc.readData("MP", 0)}/{dc.readData("MP", 1)}")
                              dc.setData("Triggers", 0, 1)
                              action = None
               elif action == 2:
                    stdscr.move(height - 2, 0)
                    stdscr.clrtoeol()
                    continue
          
          elif action == 2: #Reformat this so the player sees these stats at the top, and can choose what move they'd like the description for
               stdscr.clear()
               stdscr.addstr(height - 7, 0, f"Health: {dc.readData("Player health", 0)}/{dc.readData("Player health", 1)}")
               stdscr.addstr(height - 6, 0, f"Attack: {dc.readMove(attack, 0)} DMG")
               stdscr.addstr(height - 5, 0, f"Hit Chance: {dc.readMove(attack, 1)}")
               stdscr.addstr(height - 4, 0, f"MP: {dc.readData("MP", 0)}/{dc.readData("MP", 1)}")
               stdscr.addstr(height - 3, 0, f"Health Potions: {dc.readData("Health potions", 0)}/{dc.readData("Health potions", 1)}")
               stdscr.refresh()
               while True:
                    action = menu([f"{attack}", f"{defend}", f"{special}"], True)
                    if action == 0:
                         if attack == "Sword":
                              talk("Sword - Your first main source of damage. It deals 8 damage by default, and has a hit chance of 80%")
                         elif attack == "Gun":
                              talk("Gun - Time your shots to deal more damage. The closer you press enter to when the countdown ends, the more damage you deal. 10 max damage by default")
                         elif attack == "Dagger":
                              talk("Dagger - A lightweight alternative to the sword. It deals 4 damage by default, but has a guarenteed hit chance")
                         elif attack == "Great Axe":
                              talk("Great Axe - A heavyweight alternative to the sword. It deals 12 damage by default, but has a 30% hit chance")
                    elif action == 1:
                         if defend == "Shield":
                              talk("Shield - Allows you to lower the enemy's hit chance rather than increase your own. Exponentially increases MP used, starting at 1")
                         elif defend == "Agility":
                              talk("Agility - Allows you to raise the hit chance of your weapon for this combat encounter. Exponentially increases MP used, starting at 1")
                         elif defend == "Tough Skin":
                              talk("Tough Skin - Reduces the enemy's attack damage by 1 plus the amount of times the move has been used(EX. First turn takes 1, second takes 2). Consumes 3 MP")
                    elif action == 2:
                         if special == "Rage":
                              talk("Rage - Become enraged, allowing you to deal +2 damage per attack, and taking double damage while active. Can be deactivated if used again. Uses 2 MP on activation and 1 for every turn active. Status is indicated by the color of the move.")
                         elif special == "Fireball":
                              talk("Fireball - Launches a fireball at the enemy, dealing 6 damage, and hurting the enemy for 1 damage after their turn for 1 turn. Consumes 6 MP")
                    elif action == 3:
                         stdscr.clear()
                         break
          elif action == 3:
               stdscr.clear()
               y = height - 2
               for i in log:
                    stdscr.addstr(y, 0, i)
                    y -= 2
               stdscr.refresh()
               k = 0
               while k != 10:
                    curses.curs_set(0)
                    k = stdscr.getch()
               stdscr.clear()
          
          #Enemy's turn
          if dc.readData("Triggers", 0) == 1:
               if dc.readData("Enemy health", 0) <= 0:
                    continue
               else:
                    if random.randint(1, 100) <= hitChance:
                         dmg = random.randint(dmgRange[0], dmgRange[1])
                         if dc.readMove("Rage", 0) == 1:
                              dmg = dmg * 2
                         dc.manipData("Player health", 0, dmg, "-")
                         if dc.readData("Player health", 0) <= 0:
                              talk(f"The {enemy} dealt {dmg} damage to you, killing you.")
                         else:
                              talk(f"The {enemy} hit you, dealing {dmg} damage to you. You have {dc.readData("Player health", 0)}/{dc.readData("Player health", 1)} health left")
                              dc.setData("Triggers", 0, 0)
                              if len(log) == 8:
                                   log.pop(4)
                              log.insert(0, f"Enemy: {enemy} dealt {dmg} damage to you")
                    else:
                         talk(f"The {enemy} missed")
                         dc.setData("Triggers", 0, 0)
                         if len(log) == 8:
                              log.pop(4)
                         log.insert(0, f"Enemy: {enemy} missed its attack")
                    
                    #Fireball residual damage
                    if dc.readMove("Fireball", 1) != 0:
                         dc.manipData("Enemy health", 0, dc.readMove("Fireball", 1), "-")
                         if dc.readData("Enemy health", 0) <= 0:
                              talk(f"The fireball's residual damage killed the {enemy}")
                         else:
                              talk(f"The {enemy} took {dc.readMove("Fireball", 1)} residual damage from the fireball, leaving them at {dc.readData("Enemy health", 0)} health. The residual damage wore off")
                              dc.setMove("Fireball", 1, 0)
                              dc.setData("Triggers", 0, 0)
                              if len(log) == 8:
                                   log.pop(4)
                              log.insert(0, f"Player: {enemy} took {dc.readMove("Fireball", 1)} residual fireball damage")
     #Battle end
     if dc.readData("Enemy health", 0) <= 0:
          dc.resetMove()
          dc.resetEnemy()
          stdscr.clear()
          stdscr.refresh()
          talk(f"{enemy} defeated")
          if type(xp) == bool:
               xp = str(xp)
               xp = str(int((round(dc.readEnemy(enemy, 1)) / 2) * (dc.readEnemy(enemy, 3) - dc.readEnemy(enemy, 2))))
               xp = int(xp)
          if (dc.readData("XP", 0) + xp) >= dc.readData("XP", 1):
               temp = dc.readData("XP", 0)
               temp2 = dc.readData("XP", 1)
               temp3 = dc.readData("XP", 2)
               dc.manipData("XP", 0, xp, "+")
               while dc.readData("XP", 0) >= dc.readData("XP", 1):
                    dc.manipData("XP", 2, 1, "+")
                    dc.manipData("XP", 0, dc.readData("XP", 1), "-")
                    dc.manipData("XP", 1, 2, "*")
               talk(f"{xp} XP", "Rewards:")
               stdscr.clear()
               stdscr.refresh()
               y = height - 1
               for x in range(3):
                    y -= 1
                    stdscr.clear()
                    stdscr.addstr(y, 0, f"{xp} XP")
                    stdscr.addstr(y - 2, 0, "Rewards:")
                    stdscr.refresh()
                    time.sleep(0.3)
               stdscr.addstr(height - 1, 0, f"{temp}/{temp2} XP")
               stdscr.refresh()
               for x in range(xp):
                    temp += 1
                    if temp == temp2:
                         temp2 *= 2
                         temp = 0
                    stdscr.move(height - 1, 0)
                    stdscr.clrtoeol()
                    stdscr.addstr(height - 1, 0, f"{temp}/{temp2} XP")
                    stdscr.refresh()
                    time.sleep(0.04)
               stdscr.clear()
               stdscr.addstr(height - 3, 0, f"{temp}/{dc.readData("XP", 1)} XP")
               stdscr.addstr(height - 1, 0, f"Level up! | Level {dc.readData("XP", 2)}")
               stdscr.refresh()
               k = 0
               while k != 10:
                    k = stdscr.getch()
               stdscr.clear()
               stdscr.addstr(height - 8, 0, f"{temp}/{dc.readData("XP", 1)} XP")
               stdscr.addstr(height - 6, 0, f"Level up! | Level {dc.readData("XP", 2)}")
               stdscr.addstr(height - 4, 0, f"Health: {dc.readData("Player health", 0)}/{dc.readData("Player health", 1)} + {round(dc.readData("XP", 2)/2)}")
               stdscr.addstr(height - 3, 0, f"Attack: {dc.readMove(attack, 0)} + {round(dc.readData("XP", 2)/2)}")
               stdscr.addstr(height - 2, 0, f"MP: {dc.readData("MP", 0)}/{dc.readData("MP", 1)} + {round(dc.readData("XP", 2)/2)}")
               stdscr.addstr(height - 1, 0, f"Health potions: {dc.readData("Health potions", 0)}/{dc.readData("Health potions", 1)} + {dc.readData("XP", 2) - temp3}")
               stdscr.refresh()
               k = 0
               while k != 10:
                    k = stdscr.getch()
               dc.manipData("Player health", 0, (round(dc.readData("XP", 2)/2)), "+")
               dc.manipData("Player health", 1, (round(dc.readData("XP", 2)/2)), "+")
               dc.manipMove("Sword", 0, (round(dc.readData("XP", 2)/2)), "+")
               dc.manipMove("Great Axe", 0, (round(dc.readData("XP", 2)/2)), "+")
               dc.manipMove("Dagger", 0, (round(dc.readData("XP", 2)/2)), "+")
               dc.manipData("MP", 1, (round(dc.readData("XP", 2)/2)), "+")
               dc.manipData("MP", 0, (round(dc.readData("XP", 2)/2)), "+")
               dc.manipData("Health potions", 1, (dc.readData("XP", 2) - temp3), "+")
               dc.manipData("Health potions", 0, (dc.readData("XP", 2) - temp3), "+")

               stdscr.addstr(height - 4, 0, f"Health: {dc.readData("Player health", 0)}/{dc.readData("Player health", 1)}         ")
               stdscr.addstr(height - 3, 0, f"Attack: {dc.readMove(attack, 0)}    ")
               stdscr.addstr(height - 2, 0, f"MP: {dc.readData("MP", 0)}/{dc.readData("MP", 1)}    ")
               stdscr.addstr(height - 1, 0, f"Health potions: {dc.readData("Health potions", 0)}/{dc.readData("Health potions", 1)}    ")
               stdscr.refresh()
               k = 0
               while k != 10:
                    curses.curs_set(0)
                    k = stdscr.getch()
               return
          else:
               temp = dc.readData("XP", 0)
               temp2 = dc.readData("XP", 1)
               temp3 = dc.readData("XP", 2)
               dc.manipData("XP", 0, xp, "+")
               talk(f"{xp} XP", "Rewards:")
               stdscr.clear()
               stdscr.refresh()
               y = height - 1
               for x in range(3):
                    y -= 1
                    stdscr.clear()
                    stdscr.addstr(y, 0, f"{xp} XP")
                    stdscr.addstr(y - 2, 0, "Rewards:")
                    stdscr.refresh()
                    time.sleep(0.3)
               stdscr.addstr(height - 1, 0, f"{temp}/{temp2} XP")
               stdscr.refresh()
               for x in range(xp):
                    temp += 1
                    if temp == temp2:
                         temp2 *= 2
                         temp = 0
                    stdscr.move(height - 1, 0)
                    stdscr.clrtoeol()
                    stdscr.addstr(height - 1, 0, f"{temp}/{temp2} XP")
                    stdscr.refresh()
                    time.sleep(0.04)
               stdscr.clear()
               stdscr.addstr(height - 1, 0, f"{temp}/{dc.readData("XP", 1)} XP")
               k = 0
               while k != 10:
                    curses.curs_set(0)
                    k = stdscr.getch()
               return
          
                    
                    
                    
     elif dc.readData("Player health", 0) <= 0:
          talk(f"You died to the {enemy}")
     return