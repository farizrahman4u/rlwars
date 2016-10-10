from qlearning4k.games.game import Game

class MultiPlayerGame(Game):
	'''Abstract class for multi player games, where the players take turns
	'''

	_current_player = 0

	@property
	def name(self):
		return 'MultiPlayerGame'
	
	@property
	def nb_players(self):
	    return 2

	def current_player(self):
		return self._current_player

	def play(self, action):
		'''Should be called by derived class
		'''
		if self._current_player == self.nb_players - 1:
			self._current_player = 0
		else:
			self._current_player += 1

	def get_scores(self):
		return 0

	def get_score(self, player):
		return self.get_scores[player]

	def winner(self):
		return None

