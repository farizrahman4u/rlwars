from rlwars import *
from human_agent import *
from model import *
from rl_agent import *
from tic_tac_toe import*
import os


# Lets the user play against a pre-trained agent.



# Load model and weights
model = get_model()

def filepath(f):
	return os.path.abspath(os.path.join(__file__, os.pardir)) + '/' + f

weight_file = filepath('weights.dat')

model.load_weights(weight_file)

# Initialize players
agent = RLAgent(model)
human = HumanAgent()

# Initialize game
game = TicTacToe()

print('Player 0 is agent, Player 1 is human')

battle_field = BattleField(game, [agent, human])
battle_field.fight()
