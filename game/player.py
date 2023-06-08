from game.variants import Variants


class Player:
    name = str
    _choice = None
    player_id = None

    def __init__(self, name):
        self.name = name

    def set_choice(self):

        while True:
            print("what is your choice?(write rock, cut or paper")
            temp = input()
            temp.upper().strip()

            if temp == 'rock':
                self._choice = Variants.ROCK
                break
            elif temp == 'cut':
                self._choice = Variants.CUT
                break
            elif temp == 'paper':
                self._choice = Variants.PAPER
                break
            else:
                print('it is not correct')
                continue

    def drop_choice(self) -> Variants:
        self.set_choice()
        return self._choice
