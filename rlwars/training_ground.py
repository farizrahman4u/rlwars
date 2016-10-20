'''
This is where Reinforcement learning agents will train against hard coded agents in multi-player games
'''


# Note : By convention, Learning agent is player 0 and Hard-coded agent is player 1

from qlearning4k.games.game import Game


class TrainingGround(Game):


	def __init__(self, game, hard_agent):
		self.game = game
		self.agent = hard_agent
		super(TrainingGround, self).__init__()

	@property
	def nb_actions(self):
	    return self.game.nb_actions

	@property
	def name(self):
	    return self.game.name + '_TrainingGround'
	
	def reset(self):
		self.game.reset()
		while self.game.current_player() == 1:
			self.game.play(self.agent.get_action(self.game.get_frame()))

	def get_state(self):
		return self.game.get_state()

	def get_frame(self):
		return self.game.get_frame()

	def draw(self):
		return self.game.draw()

	def play(self, action):
		if self.game.current_player() == 0:
			self.game.play(action)
			while not self.game.is_over() and self.game.current_player() == 1:
				self.game.play(self.agent.get_action(self.game.get_frame()))

	def get_score(self):
		return self.game.get_scores()[0]

	def is_over(self):
		return self.game.is_over()

	def is_won(self):
		if not self.is_over():
			return False
		else:
			return not self.game.winner()

	def get_possible_actions(self):
		return self.game.get_possible_actions(0)
