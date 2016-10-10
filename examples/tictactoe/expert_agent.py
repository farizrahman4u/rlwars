'''A hard coded agent expert in the game of tic tac toe.
The agent can never be beaten by default. The agent can be
made to make intentional errors using the error argument.
For example, if error = 0.1, the agent will make a mistake
10% of the time.
'''

# Note : Expert agent plays 0 by default. To switch this, set X = True


from rlwars import RandomAgent
import numpy as np
import random


class ExpertAgent(RandomAgent):

	X = False

	def __init__(self, error=0.):
		self.error = error

	def get_action(self, state):
		if np.random.random() < self.error:
			return np.random.randint(9)
		else:
			if self.X:
				mask = (state == 0) + (state  == 1)
				state = (1 - state) * mask + state * (1 - mask)
				del mask
			indices = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
			# Check for immediate wins
			action_candidates = []
			for i in indices:
				cells = np.array([state[x / 3, x % 3] for x in i])
				if np.sum(cells == 0) == 2 and np.sum(cells == -1) == 1:
					action_candidates += [i[np.argmax(cells == -1)]]
			if len(action_candidates) > 0:
				return random.sample(action_candidates, 1)[0]	
			# Check for immediate threats
			action_candidates = []
			for i in indices:
				cells = np.array([state[x / 3, x % 3] for x in i])
				if np.sum(cells == 1) == 2 and np.sum(cells == -1) == 1:
					action_candidates += [i[np.argmax(cells == -1)]]
			if len(action_candidates) > 0:
				return random.sample(action_candidates, 1)[0]
			# Some hard coded logic
			action_candidates = []
			for i in indices:
				cells = np.array([state[x / 3, x % 3] for x in i])
				if np.sum(cells == 1) == 1 and np.sum(cells == -1) == 2:
					_i = i[:]
					_i.pop(np.argmin(cells == -1))
					action_candidates += _i
			if len(action_candidates) > 0:
				return random.sample(action_candidates, 1)[0]			
			action_candidates = [x for x in range(9) if state[x / 3, x % 3] == -1]
			if len(action_candidates) > 0:
				if 4 in action_candidates:
					return 4
				else:
					return random.sample(action_candidates, 1)[0]
			return 0
