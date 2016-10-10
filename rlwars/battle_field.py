'''This is where agents compete with each other
'''


class BattleField(object):

	def __init__(self, game, players):
		self.game = game
		self.players = players

	def fight(self, nb_epoch=10, verbose=2):
		nb_won = [0] * len(self.players)
		nb_draw = 0
		for e in range(nb_epoch):
			if verbose >= 1:
				print('Epoch ' + str(e + 1))
			self.game.reset()
			while not self.game.is_over():
				player = self.game.current_player()
				action = self.players[player].get_action(self.game.get_frame())
				self.game.play(action)
				if verbose >= 3:
					print('Player ' + str(player) + ' : ' + str(action))
					score_txt = 'Scores : '
					scores = self.game.get_scores()
					for i in range(len(self.players)):
						score_txt += 'Player ' + str(i) + ' : ' + str(scores[i]) + ' '
					print(score_txt)

			winner = self.game.winner()
			if winner is None:
				nb_draw += 1
				if verbose >= 2:
					print('Draw.')
			else:
				nb_won[winner] += 1
				print('Game won by Player ' + str(winner))
			if verbose >= 2:
				score_txt = 'Scores : '
				scores = self.game.get_scores()
				for i in range(len(self.players)):
					score_txt += 'Player ' + str(i) + ' : ' + str(scores[i]) + ' '
				print(score_txt)
		if verbose >= 1:
			print('Final stats : ')
			for i in range(len(self.players)):
				print('Player ' + str(i) + ' : Won ' + str(nb_won[i]) + ' games.')
			print('Number of draws :' + str(nb_draw))
