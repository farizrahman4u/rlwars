'''A random agent. Simply outputs a random action without looking at the game.
Serves as a base class for other agents.
'''

import numpy as np


class RandomAgent(object):

	def __init__(self, nb_actions):
		self.nb_actions = nb_actions

	def get_action(self, state):
		return np.random.randint(self.nb_actions)
