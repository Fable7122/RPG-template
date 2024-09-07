import random
import pandas as pd

data = pd.read_csv('data.csv')
Pts = 0
combhealth = data.loc[1, 'variable'] + data.loc[5, 'variable'] + data.loc[8, 'variable'] + data.loc[11, 'variable']

def teamhealing(curhealth: int, healby: int):
     maxhealth = data.loc[curhealth, 'range']
     heal = data.loc[curhealth, 'variable'] + healby
     if data.loc[curhealth, 'variable'] == maxhealth:
          return None
     if heal > maxhealth:
          if data.loc[curhealth, 'variable'] >= [maxhealth - 3]:
               while data.loc[curhealth, 'variable'] != data.loc[curhealth, 'range']:
                    data.at[curhealth, 'variable'] = data.at[curhealth, 'variable'] + 1
                    data.to_csv('data.csv', index=False)
     elif heal < maxhealth:
          data.loc[curhealth, 'variable'] = heal
          data.to_csv('data.csv', index=False)

#Battle function
def battle(enemy: str, enemyhealth: int):
     global health, maxhealth, data, Pts, combhealth
     data.at[0, 'variable'] = enemyhealth
     data.at[0, 'range'] = enemyhealth
     data.to_csv('data.csv', index=False)
     print(f"\n\nYou started a battle with the {enemy}. It has {enemyhealth} health\n")
     while data.loc[0, 'variable'] > 0 and combhealth > 0:
          while Pts < 4:
               if Pts == 0:
                    if data.loc[1, 'variable'] <= 0:
                         Pts = Pts + 1
                    else:
                         print("Player 1's turn")
                         action = input("[Attack] [Heal] [Stats]\n")
                         #Player 1's Attack 
                         if action == "Attack":
                              action = input("[Sword] [Double Shot] [Back]\n")

                              #Sword move
                              if action == "Sword":
                                   dmg = random.randint(data.loc[2, 'variable'], data.loc[2, "range"])
                                   predmg = data.loc[0, 'variable'] - dmg
                                   if random.randint(1, 10) > 3:
                                        if predmg <= 0:
                                             data.at[0, 'variable'] = 0
                                             data.to_csv('data.csv', index=False)
                                             print(f"Player 1 dealt {dmg} damage to the enemy, killing them")
                                             action = None
                                             Pts = 4
                                        else:
                                             data.at[0, 'variable'] = predmg
                                             data.to_csv('data.csv', index=False)
                                             print(f"Player 1 dealt {dmg} damage to the enemy, lowering them to {data.loc[0, 'variable']} health\n")
                                             action = None
                                             Pts = Pts + 1
                                   else:
                                        print("Player 1 misses")
                                        action = None
                                        Pts = Pts + 1

                              elif action == 'Double Shot':
                                   if data.loc[4, 'variable'] == 1:
                                        print("You must wait one more turn before using this move again")
                                        action = None
                                   else:
                                        data.at[4, 'variable'] = 2
                                        data.to_csv('data.csv', index=False)
                                        print("Player 1 readies their bow and waits for Player 2's attack\n")
                                        action = None
                                        Pts = Pts + 1
                                        data.at[15, 'variable'] = 1
                                        data.to_csv('data.csv', index=False)

                              elif action == "Back":
                                   continue
                              elif action not in ["Sword", "Back", "Double Shot", None]:
                                   print("Please type your choice correctly\n")
                                   action = None

                         #Heal
                         if action == "Heal":
                              action = input(f"[Health potions: {data.loc[15, 'variable']}] [Back]\n")

                              #Use health potions
                              if action == "Health potions":
                                   health = data.loc[1, 'variable']
                                   maxhealth = data.loc[1, 'range']
                                   if data.loc[16, 'variable'] <= 0:
                                        print("The party doesn't have anymore health potions left")
                                        action = None
                                   else:
                                        heal = health + 4
                                        if health == maxhealth:
                                             print("Player 1 is already at max health\n")
                                        if heal > maxhealth:
                                             if health >= [maxhealth - 3]:
                                                  while data.loc[1, 'variable'] != data.loc[1, 'range']:
                                                       data.at[1, 'variable'] = data.at[1, 'variable'] + 1
                                                       data.to_csv('data.csv', index=False)
                                                  print("Player 1 healed to full health\n")
                                                  Pts = Pts + 1
                                        elif heal < maxhealth:
                                             health = health + 4
                                             data.loc[1, 'variable'] = health
                                             data.loc[16, 'variable'] = data.loc[15, 'variable'] - 1
                                             print(f"Player 1 healed to {health} health\n")
                                             data.loc[15, 'variable'] = 1
                                             data.to_csv('data.csv', index=False)
                                             Pts = Pts + 1
                              elif action == "back":
                                   print("[Attack] [Heal]\n")
                              elif action not in ["Health potions", "Back"]:
                                   print("Please type your choice correctly\n")
                         elif action == "Stats":
                              print(f"\n--Current Stats--\n\nPlayer 1:\n{data.loc[1, 'variable']}/{data.loc[1, 'range']} Health\n{data.loc[2, 'variable']} - {data.loc[2, 'range']} Attack\n{data.loc[3, 'variable']}/100 Defense\n")
                              print(f"Player 2:\n{data.loc[5, 'variable']}/{data.loc[5, 'range']} Health\n{data.loc[6, 'variable']} Attack\n{data.loc[7, 'variable']}/100 Defense\n")
                              print(f"Player 3:\n{data.loc[8, 'variable']}/{data.loc[8, 'range']} Health\n{data.loc[9, 'variable']} - {data.loc[9, 'range']} Attack\n{data.loc[10, 'variable']}/80 Defense\n")
                              print(f"Player 4:\n{data.loc[11, 'variable']}/{data.loc[11, 'range']} Health\n{data.loc[12, 'variable']} - {data.loc[12, 'range']} Attack\n{data.loc[13, 'variable']}/100 Defense\n")
                              print(f"Misc:\n{data.loc[14, 'variable']}/{data.loc[14, 'range']} MP\n{data.loc[16, 'variable']}/{data.loc[16, 'range']} Health potions\n")
                              print(f"Enemy:\n\"{enemy}\"\n{data.loc[0, 'variable']}/{data.loc[0, 'range']} health\n") #Add in attack power later
                              action = None
                         elif action not in ["Attack", "Heal", "Back", 'Stats', None]:
                              if action == None:
                                   continue
                              else:
                                   print("Please type your choice correctly\n")
                                   action = None
               elif Pts == 1:
                    if data.loc[5, 'variable'] <= 0:
                         Pts = Pts + 1
                    else:
                         print("Player 2's turn")
                         action = input("[Attack] [Heal] [Stats]\n")
                         #Player 2's Attack
                         if action == "Attack":
                              action = input("[Bow] [Team Healing] [Back]\n")

                              #Bow move
                              if action == "Bow":
                                   dmg = random.randint(data.loc[6, 'variable'], data.loc[6, "range"])
                                   if data.loc[4, 'variable'] == 2:
                                        dmg = 8
                                   predmg = data.loc[0, 'variable'] - dmg
                                   if predmg <= 0:
                                        if data.loc[4, 'variable'] == 2:
                                             print(f'Player 2 and Player 1 deal the final blow to the {enemy}')
                                        else:
                                             print(f"Player 2 dealt {dmg} damage to the {enemy}, killing them")
                                        data.at[0, 'variable'] = 0
                                        data.to_csv('data.csv', index=False)
                                        action = None
                                        Pts = 4
                                   else:
                                        data.at[0, 'variable'] = predmg
                                        data.to_csv('data.csv', index=False)
                                        if data.loc[4, 'variable'] == 2:
                                             print(f"Player 2 and Player 1 deal {dmg} damage to the {enemy} together, lowering the {enemy} to {data.loc[0, 'variable']} health\n")
                                        else:
                                             print(f"Player 2 dealt {dmg} damage to the {enemy}, lowering them to {data.loc[0, 'variable']} health\n")
                                        action = None
                                        Pts = Pts + 1
                              
                              #Team healing
                              elif action == 'Team Healing':
                                   healby = int(input("\nHow much do you want to heal the party by? (range is 2-6 HP)\n"))
                                   if data.loc[14, 'variable'] >= [6 + healby]:
                                        teamhealing(1, healby)
                                        teamhealing(5, healby)
                                        teamhealing(8, healby)
                                        teamhealing(11, healby)
                                        print("The party has been healed\n")
                                        data.loc[14, 'variable'] = data.loc[14, 'variable'] - [6 + healby]
                                        data.to_csv('data.csv', index=False)
                                        action = None
                                        Pts = Pts + 1
                                   else:
                                        print(f"Not enough MP (current MP: {data.loc[14, 'variable']})")
                                        action = None

                              elif action == "Back":
                                   continue
                              elif action not in ["Sword", "Back", "Team Healing", None]:
                                   print("Please type your choice correctly\n")
                                   action = None

                         #Heal
                         if action == "Heal":
                              action = input(f"[Health potions: {data.loc[15, 'variable']}] [Back]\n")

                              #Use health potions
                              if action == "Health potions":
                                   health = data.loc[5, 'variable']
                                   maxhealth = data.loc[5, 'range']
                                   if data.loc[16, 'variable'] <= 0:
                                        print("The party doesn't have anymore health potions left")
                                        action = None
                                   else:
                                        heal = health + 4
                                        if health == maxhealth:
                                             print("Player 2 is already at max health\n")
                                        if heal > maxhealth:
                                             if health >= [maxhealth - 3]:
                                                  while data.loc[5, 'variable'] != data.loc[5, 'range']:
                                                       data.at[5, 'variable'] = data.at[5, 'variable'] + 1
                                                       data.to_csv('data.csv', index=False)
                                                  print("Player 2 healed to full health\n")
                                                  Pts = Pts + 1
                                        elif heal < maxhealth:
                                             health = health + 4
                                             data.loc[5, 'variable'] = health
                                             data.loc[16, 'variable'] = data.loc[15, 'variable'] - 1
                                             print(f"Player 2 healed to {health} health\n")
                                             data.loc[15, 'variable'] = 1
                                             data.to_csv('data.csv', index=False)
                                             Pts = Pts + 1
                              elif action == "back":
                                   print("[Attack] [Heal]\n")
                              elif action not in ["Health potions", "Back"]:
                                   print("Please type your choice correctly\n")
                         elif action == "Stats":
                              print(f"\n--Current Stats--\n\nPlayer 1:\n{data.loc[1, 'variable']}/{data.loc[1, 'range']} Health\n{data.loc[2, 'variable']} - {data.loc[2, 'range']} Attack\n{data.loc[3, 'variable']}/100 Defense\n")
                              print(f"Player 2:\n{data.loc[5, 'variable']}/{data.loc[5, 'range']} Health\n{data.loc[6, 'variable']} Attack\n{data.loc[7, 'variable']}/100 Defense\n")
                              print(f"Player 3:\n{data.loc[8, 'variable']}/{data.loc[8, 'range']} Health\n{data.loc[9, 'variable']} - {data.loc[9, 'range']} Attack\n{data.loc[10, 'variable']}/80 Defense\n")
                              print(f"Player 4:\n{data.loc[11, 'variable']}/{data.loc[11, 'range']} Health\n{data.loc[12, 'variable']} - {data.loc[12, 'range']} Attack\n{data.loc[13, 'variable']}/100 Defense\n")
                              print(f"Misc:\n{data.loc[14, 'variable']}/{data.loc[14, 'range']} MP\n{data.loc[16, 'variable']}/{data.loc[16, 'range']} Health potions\n")
                              print(f"Enemy:\n\"{enemy}\"\n{data.loc[0, 'variable']}/{data.loc[0, 'range']} health\n") #Add in attack power later
                              action = None
                         elif action not in ["Attack", "Heal", "Back", 'Stats', None]:
                              if action == None:
                                   continue
                              else:
                                   print("Please type your choice correctly\n")
                                   action = None
               #Player 3's turn
               elif Pts == 2:
                    if data.loc[8, 'variable'] <= 0:
                         Pts = Pts + 1
                    else:
                         print("Player 3's turn")
                         action = input("[Attack] [Heal] [Stats]\n")
                         #Player 3's Attack
                         if action == "Attack":
                              action = input("[Dagger] [Agility] [Back]\n")

                              #Dagger move
                              if action == "Dagger":
                                   dmg = random.randint(data.loc[9, 'variable'], data.loc[9, "range"])
                                   if random.randint(1, 10) > 1:
                                        predmg = data.loc[0, 'variable'] - dmg
                                        if predmg <= 0:
                                             data.at[0, 'variable'] = 0
                                             data.to_csv('data.csv', index=False)
                                             print(f"Player 3 dealt {dmg} damage to the enemy, killing them")
                                             action = None
                                             Pts = 4
                                        else:
                                             data.at[0, 'variable'] = predmg
                                             data.to_csv('data.csv', index=False)
                                             print(f"Player 3 dealt {dmg} damage to the {enemy}, lowering them to {data.loc[0, 'variable']} health\n")
                                             action = None
                                             Pts = Pts + 1
                                   else:
                                        print("Player 3 missed")
                                        action = None
                                        Pts = Pts + 1
                              
                              #Agility
                              elif action == 'Agility':
                                   if data.loc[10, 'variable'] == 60:
                                        if data.loc[14, 'variable'] >= 8:
                                             data.at[10, 'variable'] = data.loc[10, 'variable'] + 20
                                             data.to_csv('data.csv', index=False)
                                             print(f"Player 3's agility was boosted to max\n")
                                             data.at[14, 'variable'] = data.loc[14, 'variable'] - 8
                                             data.to_csv('data.csv', index=False)
                                             action = None
                                             Pts = Pts + 1
                                        else:
                                             print(f"Not enough MP (current MP: {data.loc[14, 'variable']})\n")
                                             action = None
                                   else:
                                        if data.loc[14, 'variable'] >= 6:
                                             if data.loc[10, 'variable'] >= 80:
                                                  print("You've hit the limit for using this move (80% defense)")
                                                  action = None
                                             else:
                                                  data.at[10, 'variable'] = data.loc[10, 'variable'] + 20
                                                  data.to_csv('data.csv', index=False)
                                                  print(f"Player 3's agility was boosted to {data.loc[10, 'variable']}, allowing him to dodge attacks better\n")
                                                  data.at[14, 'variable'] = data.loc[14, 'variable'] - 6
                                                  data.to_csv('data.csv', index=False)
                                                  action = None
                                                  Pts = Pts +1
                                        else:
                                             print(f"Not enough MP (current MP: {data.loc[14, 'variable']})\n")
                                             action = None

                              elif action == "Back":
                                   continue
                              elif action not in ["Sword", "Back", "Agility", None]:
                                   print("Please type your choice correctly\n")
                                   action = None

                         #Heal
                         if action == "Heal":
                              action = input(f"[Health potions: {data.loc[15, 'variable']}] [Back]\n")

                              #Use health potions
                              if action == "Health potions":
                                   health = data.loc[8, 'variable']
                                   maxhealth = data.loc[8, 'range']
                                   if data.loc[16, 'variable'] <= 0:
                                        print("The party doesn't have anymore health potions left")
                                        action = None
                                   else:
                                        heal = health + 4
                                        if health == maxhealth:
                                             print("Player 3 is already at max health\n")
                                        if heal > maxhealth:
                                             if health >= [maxhealth - 3]:
                                                  while data.loc[8, 'variable'] != data.loc[8, 'range']:
                                                       data.at[8, 'variable'] = data.at[8, 'variable'] + 1
                                                       data.to_csv('data.csv', index=False)
                                                  print("Player 3 healed to full health\n")
                                                  Pts = Pts + 1
                                        elif heal < maxhealth:
                                             health = health + 4
                                             data.loc[8, 'variable'] = health
                                             data.loc[16, 'variable'] = data.loc[15, 'variable'] - 1
                                             print(f"Player 3 healed to {health} health\n")
                                             data.loc[15, 'variable'] = 1
                                             data.to_csv('data.csv', index=False)
                                             Pts = Pts + 1
                              elif action == "back":
                                   print("[Attack] [Heal]\n")
                              elif action not in ["Health potions", "Back"]:
                                   print("Please type your choice correctly\n")
                         elif action == "Stats":
                              print(f"\n--Current Stats--\n\nPlayer 1:\n{data.loc[1, 'variable']}/{data.loc[1, 'range']} Health\n{data.loc[2, 'variable']} - {data.loc[2, 'range']} Attack\n{data.loc[3, 'variable']}/100 Defense\n")
                              print(f"Player 2:\n{data.loc[5, 'variable']}/{data.loc[5, 'range']} Health\n{data.loc[6, 'variable']} Attack\n{data.loc[7, 'variable']}/100 Defense\n")
                              print(f"Player 3:\n{data.loc[8, 'variable']}/{data.loc[8, 'range']} Health\n{data.loc[9, 'variable']} - {data.loc[9, 'range']} Attack\n{data.loc[10, 'variable']}/80 Defense\n")
                              print(f"Player 4:\n{data.loc[11, 'variable']}/{data.loc[11, 'range']} Health\n{data.loc[12, 'variable']} - {data.loc[12, 'range']} Attack\n{data.loc[13, 'variable']}/100 Defense\n")
                              print(f"Misc:\n{data.loc[14, 'variable']}/{data.loc[14, 'range']} MP\n{data.loc[16, 'variable']}/{data.loc[16, 'range']} Health potions\n")
                              print(f"Enemy:\n\"{enemy}\"\n{data.loc[0, 'variable']}/{data.loc[0, 'range']} health\n") #Add in attack power later
                              action = None
                         elif action not in ["Attack", "Heal", "Back", 'Stats', None]:
                              if action == None:
                                   continue
                              else:
                                   print("Please type your choice correctly\n")
                                   action = None
               #Player 4's turn
               elif Pts == 3:
                    if data.loc[11, 'variable'] <= 0:
                         Pts = Pts + 1
                    else:
                         print("Player 4's turn")
                         action = input("[Attack] [Heal] [Stats]\n")
                         #Player 4's Attack
                         if action == "Attack":
                              action = input("[Great Axe] [Rage] [Back]\n")

                              #Great Axe move
                              if action == "Great Axe":
                                   dmg = random.randint(data.loc[12, 'variable'], data.loc[12, "range"])
                                   if random.randint(1, 10) > 5:
                                        if data.loc[17, 'variable'] == 1:
                                             if data.loc[14, 'variable'] >= 1:
                                                  if data.loc[14, 'variable'] == 1:
                                                       data.at[14, 'variable'] = 0
                                                       data.at[17, 'variable'] = 0
                                                       data.to_csv('data.csv', index=False)
                                                       print("Your party ran out of MP. Player 4's rage has been disabled")
                                                  else:
                                                       data.at[14, 'variable'] = data.loc[14, 'variable'] - 1
                                                       data.to_csv('data.csv', index=False)
                                             dmg = dmg + 2
                                        predmg = data.loc[0, 'variable'] - dmg
                                        if predmg <= 0:
                                             data.at[0, 'variable'] = 0
                                             data.to_csv('data.csv', index=False)
                                             print(f"Player 1 dealt {dmg} damage to the enemy, killing them")
                                             action = None
                                             Pts = 4
                                        else:
                                             data.at[0, 'variable'] = predmg
                                             data.to_csv('data.csv', index=False)
                                             print(f"Player 4 dealt {dmg} damage to the {enemy}, lowering them to {data.loc[0, 'variable']} health\n")
                                             action = None
                                             Pts = 4
                                   else:
                                        print("Player 4 missed")
                                        action = None
                                        Pts = 4
                              
                              #Rage
                              elif action == 'Rage':
                                   if data.loc[17, 'variable'] == 1:
                                        yn = input(f"Do you want to disable rage? ({data.loc[14, 'variable']} MP left)\n[Yes] [No]\n")
                                        if yn == "Yes":
                                             data.at[17, 'variable'] = 0
                                             data.to_csv('data.csv', index=False)
                                             print("Player 4's rage was deactivated\n")
                                             action = None
                                        elif yn == 'No':
                                             action = None
                                        elif yn not in ["Yes", "No"]:
                                             print("Please type your choice correctly\n")
                                             action = None
                                   else:
                                        if data.loc[14, 'variable'] >= 3:
                                             data.at[17, 'variable'] = 1
                                             data.at[14, 'variable'] = data.loc[14, 'variable'] - 1
                                             data.to_csv('data.csv', index=False)
                                             print("Player 4 activates his rage\n")
                                             action = None
                                        else:
                                             print("The party does not have sufficient MP\n")
                                             action = None

                              elif action == "Back":
                                   continue
                              elif action not in ["Great Axe", "Back", "Rage", None]:
                                   print("Please type your choice correctly\n")
                                   action = None

                         #Heal
                         if action == "Heal":
                              action = input(f"[Health potions: {data.loc[15, 'variable']}] [Back]\n")

                              #Use health potions
                              if action == "Health potions":
                                   health = data.loc[11, 'variable']
                                   maxhealth = data.loc[11, 'range']
                                   if data.loc[16, 'variable'] <= 0:
                                        print("The party doesn't have anymore health potions left")
                                        action = None
                                   else:
                                        heal = health + 4
                                        if health == maxhealth:
                                             print("Player 4 is already at max health\n")
                                        if heal > maxhealth:
                                             if health >= [maxhealth - 3]:
                                                  while data.loc[11, 'variable'] != data.loc[11, 'range']:
                                                       data.at[11, 'variable'] = data.at[11, 'variable'] + 1
                                                       data.to_csv('data.csv', index=False)
                                                  print("Player 4 healed to full health\n")
                                                  if data.loc[17, 'variable'] == 1:
                                                       if data.loc[14, 'variable'] >= 1:
                                                            if data.loc[14, 'variable'] == 1:
                                                                 data.at[14, 'variable'] = 0
                                                                 data.at[17, 'variable'] = 0
                                                                 data.to_csv('data.csv', index=False)
                                                                 print("Your party ran out of MP. Player 4's rage has been disabled")
                                                            else:
                                                                 data.at[14, 'variable'] = data.loc[14, 'variable'] - 1
                                                  Pts = Pts + 1
                                        elif heal < maxhealth:
                                             health = health + 4
                                             data.loc[11, 'variable'] = health
                                             data.loc[16, 'variable'] = data.loc[15, 'variable'] - 1
                                             print(f"Player 4 healed to {health} health\n")
                                             data.loc[15, 'variable'] = 1
                                             data.to_csv('data.csv', index=False)
                                             if data.loc[17, 'variable'] == 1:
                                                  if data.loc[14, 'variable'] >= 1:
                                                       if data.loc[14, 'variable'] == 1:
                                                            data.at[14, 'variable'] = 0
                                                            data.at[17, 'variable'] = 0
                                                            data.to_csv('data.csv', index=False)
                                                            print("Your party ran out of MP. Player 4's rage has been disabled")
                                                       else:
                                                            data.at[14, 'variable'] = data.loc[14, 'variable'] - 1
                                             Pts = Pts + 1
                              elif action == "back":
                                   print("[Attack] [Heal]\n")
                              elif action not in ["Health potions", "Back"]:
                                   print("Please type your choice correctly\n")
                         elif action == "Stats":
                              print(f"\n--Current Stats--\n\nPlayer 1:\n{data.loc[1, 'variable']}/{data.loc[1, 'range']} Health\n{data.loc[2, 'variable']} - {data.loc[2, 'range']} Attack\n{data.loc[3, 'variable']}/100 Defense\n")
                              print(f"Player 2:\n{data.loc[5, 'variable']}/{data.loc[5, 'range']} Health\n{data.loc[6, 'variable']} Attack\n{data.loc[7, 'variable']}/100 Defense\n")
                              print(f"Player 3:\n{data.loc[8, 'variable']}/{data.loc[8, 'range']} Health\n{data.loc[9, 'variable']} - {data.loc[9, 'range']} Attack\n{data.loc[10, 'variable']}/80 Defense\n")
                              print(f"Player 4:\n{data.loc[11, 'variable']}/{data.loc[11, 'range']} Health\n{data.loc[12, 'variable']} - {data.loc[12, 'range']} Attack\n{data.loc[13, 'variable']}/100 Defense\n")
                              print(f"Misc:\n{data.loc[14, 'variable']}/{data.loc[14, 'range']} MP\n{data.loc[16, 'variable']}/{data.loc[16, 'range']} Health potions\n")
                              print(f"Enemy:\n\"{enemy}\"\n{data.loc[0, 'variable']}/{data.loc[0, 'range']} health\n") #Add in attack power later
                              action = None
                         elif action not in ["Attack", "Heal", "Back", 'Stats', None]:
                              if action == None:
                                   continue
                              else:
                                   print("Please type your choice correctly\n")
                                   action = None                    
          #Enemy's turn
          if Pts == 4:
               if data.loc[0, 'variable'] > 0:
                    if data.loc[4, 'variable'] > 0:
                         data.at[4, 'variable'] = data.loc[4, 'variable'] - 1
                    attkplyr = random.randint(1,4)
                    dmg = random.randint(6, 8)
                    if attkplyr == 1:
                         if random.randint(1,10) > 3:
                              data.at[1, 'variable'] = data.loc[1, 'variable'] - dmg
                              data.to_csv('data.csv', index=False)
                              print(f"The {enemy} attacks Player 1, dealing {dmg} damage. Player 1 is now at {data.loc[1, 'variable']}/{data.loc[1, 'range']} health\n")
                         else:
                              print(f"Player 1 dodged the {enemy}'s attack")
                    elif attkplyr == 2:
                         if random.randint(1, 10) > 7:
                              data.at[5, 'variable'] = data.loc[5, 'variable'] - dmg
                              data.to_csv('data.csv', index=False)
                              print(f"The {enemy} attacks Player 2, dealing {dmg} damage. Player 2 is now at {data.loc[5, 'variable']}/{data.loc[5, 'range']} health\n")
                         else:
                              print(f"Player 2 dodged the {enemy}'s attack")
                    elif attkplyr == 3:
                         if random.randint(1, 10) > 4:
                              data.at[8, 'variable'] = data.loc[8, 'variable'] - dmg
                              data.to_csv('data.csv', index=False)
                              print(f"The {enemy} attacks Player 3, dealing {dmg} damage. Player 3 is now at {data.loc[8, 'variable']}/{data.loc[8, 'range']} health\n")
                         else:
                              print(f"Player 3 dodged the {enemy}'s attack")
                    elif attkplyr == 4:
                         if random.randint(1, 10) > 9:
                              if data.loc[17, 'variable'] == 1:
                                   dmg = dmg * 2
                              data.at[11, 'variable'] = data.loc[11, 'variable'] - dmg
                              data.to_csv('data.csv', index=False)
                              print(f"The {enemy} attacks Player 4, dealing {dmg} damage. Player 4 is now at {data.loc[11, 'variable']}/{data.loc[11, 'range']} health\n")
                         else:
                              print(f"Player 4 dodged the {enemy}'s attack")
                    Pts = 0
     #Battle end
     if data.loc[0, 'variable'] <= 0:
          print(f"The party defeated the {enemy}")
          data.at[4, 'variable'] = 0
          data.at[10, 'variable'] = data.loc[10, 'range']
          data.at[17, 'variable'] = 0
          data.to_csv('data.csv', index=False)
          return
     elif combhealth <= 0:
          print(f"The party has been wiped by the {enemy}. Game over")
          exit()
     return

battle("wild board", 50)