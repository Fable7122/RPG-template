# 4 Player RPG Battle Documentation
**This code is outdated, and does not work**

## Playing the game:
>When the game waits for your input, your available options are the words within the brackets. If there are no words in brackets, then just press enter
>to continue. Your input must be exactly the same as the typed word(s) in the brackets, so if you want to ensure that you get it correct, then you could
>copy and paste the command. If you do not type it correctly, it will send you back to the beginning of the current player's turn, with an error message
above stating that you need to type the command correctly.

## Required packages:
>I'm sure you can figure it out by looking at the python file, but Pandas is required. That's it!

## The moves:

 - **Player 1:**
    - **Sword -** Has 6-8 damage range, with a 70% hit chance
    - **Double Shot -** Waits until player 2 makes their move, and if the chosen move is Bow, then the damage is doubled (in game reason being that player 1 and player 2 shoot together)

 - **Player 2:**
    - **Bow -** Has a fixed damage of 3, with a 100% hit chance
    - **Team Healing -** Asks for how much you would like to heal your team by (with the minimum being 2 and maximum 6) and then consumes 6 mp plus the amount you healed by

 - **Player 3:**
    - **Dagger -** Has a damage range of 3-4, with a 90% hit chance
    - **Agility -** Boosts player 3's defense by 20 every time it is used with the max being 80. The first two uses (going up to 60 defense) consumes 6 MP, and the last one consumes 8

 - **Player 4:**
    - **Great Axe -** All of nothing weapon, with an attack range of 1-12 damage, and a 50% hit chance
     - **Rage -** Adds 2 damage to the great axe's damage dealt while active, but also takes double damage from enemies. Does not take up player 4's action, so you can attack after enabling it. Consumes 2 MP upon activation, and then 1 MP for every turn it is active. Can be disabled during player 4's turn without taking an action.

## MP and HP:
You start out holding a max of 20 MP, and 4 health potions. Health potions do not have a max of 4, but instead 8.
