#Start with your imports. Here, you're importing TensorFlow and calling it tf for ease of use.
import tensorflow as tf
#Next, import a library called numpy, which represents your data as lists easily and quickly.
import numpy as np
#The framework for defining a neural network as a set of sequential layers is called keras, so import that, too.
from tensorflow import keras

#create the simplest possible neural network. It has one layer, that layer has one neuron, 
# and the input shape to it is only one value.
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')


#Next we feed some data. In this case, you take the six X and six Y variables from earlier.
# You can see that the relationship between those is that Y=3X+1, so where X is -1, Y is -2.
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

#The process of training the neural network, where it learns the relationship between the X's and Y's, is in the model.fit call. That's where it will go through the loop before making a guess,
#measuring how good or bad it is (the loss), or using the optimizer to make another guess. It will do that for the number of epochs that you specify.
#When you run that code, you'll see the loss will be printed out for each epoch.
model.fit(xs, ys, epochs=100)
#By the time the training is done, the loss is extremely small, showing that our model is doing a great job of inferring the relationship between the numbers.
#also noticed if i use a higher number of epochs, the model predicts better

#You have a model that has been trained to learn the relationship between X and Y. 
# You can use the model.predict method to have it figure out the Y for a previously unknown X. For example, 
# if X is 10, what do you think Y will be?
print(model.predict([10.0]))