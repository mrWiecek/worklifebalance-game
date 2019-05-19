from data import Data
from player import Player


def main():
    """
    Function creates main loop of a game and sets up default values for player.
    """

    print('Welcome stranger!')
    name = input('{: >20}'.format('Input you name! : '))
    print('')

    # set up data object
    data = Data()

    # set up player give player data
    player = Player(str(name).title(), data)
    print(f'\tHello {player.name}.\nGood luck!!!', end='\n\n')

    # set up default active events,
    for i in range(3):
        player.add_event(data.random_event())

    # main loop
    while not(player.work_points >= 100 and player.life_points >= 100):
        player.action()
        player.update_player()

    print('Congratulations you win!!!')


if __name__ == '__main__':
    main()
