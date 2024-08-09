import numpy as np
import keras 
from keras import layers
from keras import ops

inputs = keras.Input(shape=(784,))#nodo de entrada
img_inputs = keras.Input(shape = (32, 32, 3))
dense = layers.Dense(64, activation = 'relu')
x = dense(inputs)
x = layers.Dense(64, activation = 'relu')(x)
outputs = layers.Dense(10)(x)
model = keras.Model(inputs = inputs, outputs = outputs, name = 'mnist_model')
model.summary()
keras.utils.plot_model(model, "my_first_model.png")
