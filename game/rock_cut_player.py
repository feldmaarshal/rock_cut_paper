from game.player import Player
from game.variants import Variants


class RockCutPaper:
    _choices = []
    _players = []
    _cnt_players = 0
    _game_id = 1

    def add_player(self, player: Player):
        self._players += [player]
        self._cnt_players += 1
        player.player_id = self._cnt_players

    def start(self):
        print('This is rock-cut-paper game.You are welcome!\n'
              'Lets start! If you wanna quit, you should input "*" where you want\n')
        if self._cnt_players != 2:
            raise 'CntPlayerError'
        while True:
            print(f'set game number {self._game_id}\n')
            self._game_id += 1

            self._choices = [(self._players[i].set_choice(), i) for i in range(self._cnt_players)]
            temp = set(self._choices[i][0] for i in range(self._cnt_players))

            if len(temp) in (1, 3):
                print(f'\n///////////////// draw !!!!!!!///////////////////')
                break
            if self._cnt_players == 2:
                if not self._two_player():
                    break

    def _two_player(self):
        if self._choices[0][0] == Variants.ROCK:
            if self._choices[1][0] == Variants.CUT:
                if not self._winner(self._choices[0][1]):
                    print('We were glad to see you! Bye!')
                    return False
            else:
                if not self._winner(self._choices[1][1]):
                    print('We were glad to see you! Bye!')
                    return False
        elif self._choices[0][0] == Variants.CUT:
            if self._choices[1][0] == Variants.PAPER:
                if not self._winner(self._choices[0][1]):
                    print('We were glad to see you! Bye!')
                    return False
            else:
                if not self._winner(self._choices[1][1]):
                    print('We were glad to see you! Bye!')
                    return False
        else:
            if self._choices[1][0] == Variants.ROCK:
                if not self._winner(self._choices[0][1]):
                    print('We were glad to see you! Bye!')
                    return False
            else:
                if not self._winner(self._choices[1][1]):
                    print('We were glad to see you! Bye!')
                    return False
        return True

    def _winner(self, id):
        print(f'\n/////////////////{self._players[id].name} win !!!!!!!///////////////////')
        print('if you want to continue and play next, input any button(except "*")')
        temp = input().strip()
        if temp == '*':
            return False

        return True
