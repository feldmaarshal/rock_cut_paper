from game.player import Player
from game.variants import Variants


class RockCutPaper:
    _players = []
    _cnt_players = 0
    _game_id = 1

    def add_player(self, player: Player):
        self._players += [player]
        self._cnt_players += 1
        player.player_id = self._cnt_players

    def start(self):
        print('This is rock-cut-paper game.You are welcome!\n'
              'Lets start! If you wanna quit, you should input "*" where you want')
        if len(self._players) <= 1 or len(self._players) > 3:
            raise 'CntPlayerError'
        while True:
            print(f'set game number {self._game_id}')
            self._game_id += 1

            choices = [(self._players[i].set_choice(), i) for i in range(self._cnt_players)]
            if len(set(choices)) in (1, 3):
                print('draw')
                continue
            if self._cnt_players == 2:
                if choices[0][0] == Variants.ROCK:
                    if choices[1][0] == Variants.CUT:
                        if not self._winner(choices[0][1]):
                            print('We were glad to see you! Bye!')
                            break
                        continue
                    else:
                        if not self._winner(choices[1][1]):
                            print('We were glad to see you! Bye!')
                            break
                        continue
            else:
                if choices[0][0] not in (choices[1][0], choices[2][0]):
                    if choices[0][0] == Variants.ROCK:
                        if choices[1][0] == Variants.CUT:
                            if not self._winner(choices[0][1]):
                                print('We were glad to see you! Bye!')
                                break
                            continue
                        else:
                             print('!¬!!!!!!!!!!')

                elif choices[1][0] not in (choices[0][0], choices[2][0]):
                    if choices[1][0] == Variants.ROCK:
                        if choices[0][0] == Variants.CUT:
                            if not self._winner(choices[1][1]):
                                print('We were glad to see you! Bye!')
                                break
                            continue
                        else:
                             print('!¬!!!!!!!!!!')

                elif choices[2][0] not in (choices[0][0], choices[1][0]):
                    if choices[2][0] == Variants.ROCK:
                        if choices[0][0] == Variants.CUT:
                            if not self._winner(choices[2][1]):
                                print('We were glad to see you! Bye!')
                                break
                            continue
                        else:
                             print('!¬!!!!!!!!!!')

    def _winner(self, id):
        print(f'{self._players[id].name} win !!!!!!!')
        print('if you want to continue and play next, input any button(except "*")')
        temp = input().strip()
        if temp == '*':
            return False

        return True
