import random


health = 20
maxhealth = 20
healthpotions = 3
defense = 0

#Battle function
def battle(enemy: str, enemyhealth: int):
     global health, maxhealth, healthpotions, defense, turnover
     print(f"You started a battle with the {enemy}. It has {enemyhealth} health. What will you do?\n")
     while enemyhealth > 0 and health > 0:

          #Attack and Heal options
          action = input("[Attack] [Heal]\n")

          #Attack
          if action == "Attack":
               action = input("[Sword] [Shield] [Back]\n")

               #Sword move
               if action == "Sword":
                    dmg = random.randint(1, 4)
                    enemyhealth = enemyhealth - dmg
                    if enemyhealth <= 0:
                         print(f"You dealt {dmg} damage to the enemy, killing them")
                         action = None
                    else:
                         print(f"You dealt {dmg} damage to the enemy, lowering them to {enemyhealth} health\n")
                         action = None
                         with open("turnStatus.txt", "w") as f:
                              f.write("True ")
                              f.close()
               #Shield move
               if action == "Shield":
                    defense = 2
                    print("You raised your defense by 2\n")
                    action = None
                    with open("turnStatus.txt", "w") as f:
                         f.write("True ")
                         f.close()
               elif action == "Back":
                    continue
               elif action not in ["Sword", "Shield", "Back", None]:
                    print("Please type your choice correctly\n")
                    action = None

          #Heal
          if action == "Heal":
               action = input(f"[Health potions: {healthpotions}] [Back]\n")

               #Use health potions
               if action == "Health potions":
                    heal = health + 4
                    if heal <= maxhealth:
                         health = health + 4
                         healthpotions = healthpotions - 1
                         print(f"\nYou healed to {health} health\n")
                         with open("turnStatus.txt", "w") as f:
                              f.write("True ")
                              f.close()
                    else:
                         print("You are already at full health\n")
               elif action == "back":
                    print("[Attack] [Heal]\n")
               elif action not in ["Health potions", "Back"]:
                    print("Please type your choice correctly\n")
          elif action not in ["Attack", "Heal", "Back", None]:
               if action == None:
                    continue
               else:
                    print("Please type your choice correctly\n")
                    action = None
          
          #Enemy's turn
          with open("turnStatus.txt", "r") as f:
               turnstatus = f.read()
          if turnstatus == "True ":
               dmg = random.randint(1, 6)

               #Check if player used shield
               if defense != 0:
                    hit = random.randint(defense, 10)
                    if hit == 10:
                         print(f"The {enemy} missed its attack")
                         with open("turnStatus.txt", "w") as f:
                              f.write("False")
                              f.close()
                    elif hit != 10:
                         health = health - dmg
                         if health > 0:
                              print(f"The {enemy} hit you, dealing {dmg} damage to you. You have {health} health left\n")
                              with open("turnStatus.txt", "w") as f:
                                   f.write("False")
                                   f.close()
                         elif health <= 0:
                              print(f"The {enemy} hit you, dealing {dmg} damage to you\n")
                              with open("turnStatus.txt", "w") as f:
                                   f.write("False")
                                   f.close()
               #Normal enemy move
               else:     
                    health = health - dmg
                    print(f"The {enemy} hit you, dealing {dmg} damage to you. You have {health} health left\n")
                    with open("turnStatus.txt", "w") as f:
                         f.write("False")
                         f.close()
     
     #Battle end
     if enemyhealth <= 0:
          print(f"You have defeated the {enemy}")
          exit()
     elif health <= 0:
          print(f"You died to the {enemy}")
          exit()
     return

battle("Bob", 12)