import sys

from game.variants import Variants


class Player:
    name = str
    _choice = None
    player_id = None

    def __init__(self, name):
        self.name = name

    def set_choice(self):

        while True:
            print(f"{self.name}, now its your turn to choice!(write rock, cut or paper)")
            temp = input()
            temp = temp.lower().strip()

            if temp == '*':
                print('We were glad to see you! Bye!')
                sys.exit()

            if temp == 'rock':
                self._choice = Variants.ROCK
                return self._choice
            elif temp == 'cut':
                self._choice = Variants.CUT
                return self._choice
            elif temp == 'paper':
                self._choice = Variants.PAPER
                return self._choice
            else:
                print('it is not correct')
                continue
