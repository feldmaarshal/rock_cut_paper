from game.rock_cut_player import RockCutPaper, Player


boris = Player('Boris')
nikita = Player('Nikita')
vanya = Player('Vanya')

game = RockCutPaper()

game.add_player(boris)
game.add_player(nikita)

game.start()

