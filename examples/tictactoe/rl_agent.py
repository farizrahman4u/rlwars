from rlwars import RandomAgent
import numpy as np


'''Reinforcement learning agent wrapper around a Keras model. After training a Qlearning4k agent against an expert agent,
simply initialize an RLAgent instance using the Qlearning4k agent's model.
'''


# Note :  RLAgent plays X by default. To switch this, set X = False


class RLAgent(RandomAgent):

	X = True

	def __init__(self, model):
		self.model = model

	def get_action(self, state):
		possible_actions = [i for i in range(9) if state[i / 3, i % 3] == -1]
		if not self.X:
			mask = (state == 0) + (state  == 1)
			state = (1 - state) * mask + state * (1 - mask)
			del mask
		state = np.expand_dims(state, 0)
		state = np.expand_dims(state, 0)
		q = self.model.predict(state)[0]
		q = [q[i] for i in possible_actions]
		return possible_actions[np.argmax(q)]
