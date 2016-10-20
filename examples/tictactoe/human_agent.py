from rlwars import RandomAgent
import numpy as np


'''
Interface for user to interact with an agent.
'''


# Note :  Human plays 0 by default. To switch this, set X = False

def display_grid(grid):
	for i in range(3):
		x = ''
		for j in range(3):
			c = grid[i][j]
			if c == -1:
				x += str(i * 3 + j + 1) + ' '
			if c == 1:
				x += 'X '
			elif c == 0:
				x += 'O '
		print(x)

class HumanAgent(RandomAgent):

	X = False

	def __init__(self):
		pass

	def get_action(self, state):
		display_grid(state)
		while True:
			i = int(raw_input('Enter cell number to play : ')) - 1
			if i > 8 or i < 0 or state[i / 3, i % 3] != -1:
				print('Cell not empty !')
			else:
				return i
