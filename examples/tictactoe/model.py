from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras.optimizers import sgd


def get_model():
	model = Sequential()
	model.add(Flatten(input_shape=(1, 3, 3)))
	model.add(Dense(100, activation='relu'))
	model.add(Dense(100, activation='relu'))
	model.add(Dense(9))
	model.compile(loss='mse', optimizer=sgd(lr=.2))
	return model
