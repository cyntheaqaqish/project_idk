from keras.layers import InputLayer
from  keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.losses import MSE

inputs = [[1, -1]]
model = Sequential()  # matrix operation
model.add(InputLayer(input_shape=(2,)))
model.add(Dense(5, activation='relu'))  # 2 inputs 5 weights for each 2*5+5 (all of these numbers represent arrays)
model.add(Dense(3, activation='relu'))  #
model.add(Dense(2, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

opt = SGD(learning_rate=0.000001)
model.compile(loss=MSE, optimizer=opt)
