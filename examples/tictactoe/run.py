from keras.models import *
from keras.layers import *
from qlearning4k import *
from expert_agent import *
from rlwars import *
from tic_tac_toe import *
from rl_agent import *


# We create 2 neural network powered agents

# agent1
model1 = Sequential()
model1.add(Flatten(input_shape=(1, 3, 3)))
model1.add(Dense(9))
model1.compile(loss='mse', optimizer='sgd')
agent1 = Agent(model1, memory_size=100)

# agent2
model2 = Sequential()
model2.add(Flatten(input_shape=(1, 3, 3)))
model2.add(Dense(20))
model2.add(Activation('relu'))
model2.add(Dense(9))
model2.compile(loss='mse', optimizer='sgd')
agent2 = Agent(model2, memory_size=100)



# Create an expert agent, with an error rate of 20%
expert_agent = ExpertAgent(0.2)

# Create tic tac toe game instance
game = TicTacToe()

# Create a training ground, where agent1 and agent2 can train with the expert agent
training_ground = TrainingGround(game, expert_agent)

# Train each agent
# Note that agent1 and agent2 plays X while exper agent plays 0
agent1.train(training_ground, nb_epoch=100)
agent2.train(training_ground, nb_epoch=100)
# Training complete, now we let the agents fight each other. Before that, we need to create agents which are compatible with rlwars.
# Qlearning4k agents are not compatible with rlwars

agent1 = RLAgent(model1)
agent2 = RLAgent(model2)

# Both agents play X by default. Since they are playing against each other now, we have to switch one of their symbols.
agent2.X = False

# Create a battle field

battle_field = BattleField(game, [agent1, agent2])

# Let the fight begin !
battle_field.fight(nb_epoch=10, verbose=2)
