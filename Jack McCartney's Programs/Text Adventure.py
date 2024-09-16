# Post Analysis Note: The purpose of this code is to create a very basic RPG combat system using python
# Post Analysis Note: This code was written a few months ago before I learned a couple more things about programming, so there are a few things that can be improved upon in this code which I will go over
# Post Analysis Note: There are no comments within this code, which hurts its readability

import random
print(f'The Great Text Adventure!!')
input(f'Press enter to continue ')

# Post Analysis Note: The variables and function are named appropriately, and are easy to understand what their purpose is. 
# Post Analysis Note: The good naming conventions are a good programming principle and avoid S.T.U.P.I.D.'s Indescriptive Naming Principle

player_stats = {
    'MaxHP': 100,
    'CurrentHP': 100,
    'Strength': 10,
    'Dexterity': 10,
    'Intelligence': 10,
    'Defense': 20,
    'Temp Defense': 0,
}
enemy_stats = {
    'MaxHP': 50,
    'CurrentHP': 50,
    'Strength': 5,
    'Dexterity': 5,
    'Intelligence': 1,
    'Defense': 5,
    'Temp Defense': 0,
}
print(f'Player Stats: {player_stats}')

# Post Analysis Note: The entire combat system is stored within a single function. This is not ideal given the size. It would be better split up into a class with separate functions running different aspects
# Post Analysis Note: This goes against the single responsibility principle, and should be compartmentalised into smaller parts.

# Post Analysis Note: The lack of line breaks within this function makes it harder to read

# Post Analysis Note: If you were to use this code for combat against a different enemy, you would be able to change the enemy_stats dictionary to create a new enemy, but the printed text is fixed to include 'baseball'
# Post Analysis Note: It is good that the program still theoretically works with different enemy stats, since the name doesn't change, you have to modify the code in the function in order to change it
# Post Analysis Note: This goes against S.O.L.I.D's Open/Closed Principle, which states that your program should be open to extension, but closed to modification
def baseball_combat():
    print(f'A wild baseball appears and attacks you!')
    while player_stats['CurrentHP'] > 0:
        atk_hit = random.randint(0,60)
        if atk_hit > player_stats['Defense'] + player_stats['Temp Defense']:
            atk_dmg = random.randint(0,20)
            player_stats['CurrentHP'] = player_stats['CurrentHP'] - atk_dmg
            print(f'You got hit by a baseball. You take {atk_dmg} damage')
            print(f'You have {(player_stats["CurrentHP"])} Hit Points left')
        else:
            print(f'The baseball missed its attack!')
        if player_stats['CurrentHP'] < 1:
            print('You died. You got hit by a baseball multiple times before falling over')
            print('GAME OVER')
            break
        print('Your Turn')
        player_stats['Temp Defense'] = 0
        text_input=(input('Enter "a" to attack, "d" to defend, "w" to wait '))
        if text_input == 'a':
            atk_hit = random.randint(0,60)
            if atk_hit > enemy_stats['Defense'] + enemy_stats['Temp Defense']:
                atk_dmg = random.randint(0,20)
                enemy_stats['CurrentHP'] = enemy_stats['CurrentHP'] - atk_dmg
                print(f'You punch the baseball. The baseball takes {atk_dmg} damage')
                print(f'The baseball has {(enemy_stats["CurrentHP"])} Hit Points left')
            else:
                print(f'You missed your attack!')
        elif text_input == 'd':    
            player_stats['Temp Defense'] = 50
            print('You defend. Ready to dodge any attack')
        else:
            print('You wait.')
        if enemy_stats['CurrentHP'] < 1:
            print('You have annihilated the baseball with your bare hands')
            print('YOU WON!!')
            break
baseball_combat()


# Post Analysis Note: While this code can be improved upon, it is still decent code. The code does not repeat itself (D.R.Y.), and it is kept as simple as it can be (K.I.S.S.)
# Post Analysis Note: It also achieved its goal to create a simple combat system
