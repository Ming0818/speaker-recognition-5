#!/usr/bin/env python
'''
train text independent speaker recognition convolutional neural network.
save model and parameters.
'''
__author__ = "Sophia Zheng, Rish Gupta, and Manish Pandit"

import os
import keras
from keras.utils import to_categorical
import numpy as np
import voxforge
from reports import plot_history
from srs_builder import ModelBuilder
from config import activation, optimizer, dropout_rate, epochs, batch_size
from config import reports_dir

# get training and dev data
X_Train, Y_Train = voxforge.get_train_data()
X_Dev, Y_Dev = voxforge.get_dev_data()

builder = ModelBuilder(X_Train[0].shape, Y_Train.shape[1])
model = builder(activation=activation, optimizer=optimizer, dropout_rate=dropout_rate)

# print the model
print(model.summary())

# Run the optimization process and validate against dev set
# Note: We are reading data in batch mode from h5 file so shuffle 
# parameter is required.
history = model.fit(X_Train, Y_Train,
    batch_size = batch_size, epochs = epochs, verbose = 1, 
    validation_data = (X_Dev, Y_Dev), shuffle = 'batch')

# plot history
plot_history(history)

# Save the trained model and its parameters
builder.save(model)

