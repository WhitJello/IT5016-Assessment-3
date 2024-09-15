import random
print(f'The Great Text Adventure!!')
input(f'Press enter to continue ')


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