from rlwars import MultiPlayerGame
import numpy as np



class TicTacToe(MultiPlayerGame):
	'''Classic 3 x 3 TicTacToe
	Blank boxes are -1
	Zeros are 0s
	Xs are 1s
	'''

	X = 0  # By default, player 0 plays X

	@property
	def name(self):
	    return 'TicTacToe'
	
	def reset(self):
		self.grid = np.zeros((3, 3)) - 1
		self._next_player = np.random.randint(2)

	@property
	def nb_actions(self):
		# 9 boxes (3 x 3 grid)
	    return 9

	def play(self, action):
		x = action / 3
		y = action % 3
		#Make sure the box is blank
		if self.grid[x, y] != -1:
			return
		self.grid[x, y] = 1 if self.X == self._current_player else 0
		super(TicTacToe, self).play(action)
		'''
		print(self.get_state())
		import matplotlib.pyplot as plt
		plt.imshow(self.get_state(), interpolation='none')
		global i
		plt.savefig("images/" + self.name + str(i) + ".png")
		i += 1
		raw_input('press any key')
		'''
	def is_over(self):
		if not np.any(self.grid == -1):
			# Game is over for sure if no blank spaces left
			return True
		else:
			# check winning conditions
			indices = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
			for i in indices:
				cells = [self.grid[x / 3, x % 3] for x in i]
				if cells[0] != -1 and cells[0] == cells[1] and cells[0] == cells[2]:
					return True
		# There are still empty spaces and no one has won, so game is not over
		return False

	def winner(self):
		indices = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
		for i in indices:
			cells = [self.grid[x / 3, x % 3] for x in i]
			if cells[0] != -1 and cells[0] == cells[1] and cells[0] == cells[2]:
				if cells[0]:
					return self.X
				else:
					return 1 - self.X
		# Nobody won
		return None

	def get_scores(self):
		if self.is_over():
			_winner = self.winner()
			if _winner == 0:
				return [1, -1]
			elif _winner == 1:
				return [-1, 1]
			else:
				# Draw
				return [0.5, 0.5]
		else:
			# Game i still in progress.
			return [0, 0]

	def get_state(self):
		return self.grid.copy()

	def get_possible_actions(self, player=None):
		return [i for i in range(9) if self.grid[i / 3, i % 3] == -1]