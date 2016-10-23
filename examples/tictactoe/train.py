from keras.models import *
from keras.layers import *
from keras.optimizers import *
from qlearning4k import *
from expert_agent import *
from rlwars import *
from tic_tac_toe import *
from rl_agent import *
from model import *
import os


# Here we train an agent using the q learing algorithm
# The agent is trained against a weak agent (50% error), and tested against a strong agent(10% error)



train = True  # If False, model will not be trained. Instead previously trained weights will be loaded


# Get the model defined in model.py
model = get_model()

# Q-learning agent
q_agent = Agent(model, memory_size=100000)

# Create an expert agent, with an error rate of 50%
expert_agent = ExpertAgent(error=.5)

# Create tic tac toe game instance
game = TicTacToe()

# Create a training ground, where the Q-learing agent can train against the expert agent
training_ground = TrainingGround(game, expert_agent)

def filepath(f):
	return os.path.abspath(os.path.join(__file__, os.pardir)) + '/' + f

weight_file = filepath('weights.dat')
if train:
	# train
	q_agent.train(training_ground, nb_epoch=100000, epsilon=0.1, gamma=0.9)
	model.save_weights(weight_file)
else:
	# load pre-trained weights
	if not os.path.isfile(weight_file):
		print('Pre-trained weights not available. Train again.')
		exit()
	model.load_weights(weight_file)

# Reduce error rate of expert agent to 10%
expert_agent.error = 0.1

# test
q_agent.play(training_ground, nb_epoch=10, visualize=True)
