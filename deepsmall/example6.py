#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""	Multi-class perceptron """

from graph import *
from operations import *
from gradients import *
from session import Session
from train import *
import numpy as np

# Create a new graph
Graph().as_default()

X = Placeholder()
c = Placeholder()

# Initialize weights randomly
W = Variable(np.random.randn(2, 2))
b = Variable(np.random.randn(2))

# Build perceptron
p = softmax( add(matmul(X, W), b) )

# Build cross-entropy loss
J = negative(reduce_sum(reduce_sum(multiply(c, log(p)), axis=1)))

# Build minimization op
minimization_op = GradientDescentOptimizer(learning_rate = 0.01).minimize(J)

# Create red points centered at (-2, -2)
red_points = np.random.randn(50, 2) - 2*np.ones((50, 2))
# Create blue points centered at (2, 2)
blue_points = np.random.randn(50, 2) + 2*np.ones((50, 2))

# Build placeholder inputs
feed_dict = {
    X: np.concatenate((blue_points, red_points)),
    c:
        [[1, 0]] * len(blue_points)
        + [[0, 1]] * len(red_points)

}

# Create session
session = Session()

# Perform 100 gradient descent steps
for step in range(100):
    J_value = session.run(J, feed_dict)
    if step % 10 == 0:
        print("Step:", step, " Loss:", J_value)
    session.run(minimization_op, feed_dict)

# Print final result
W_value = session.run(W)
print("Weight matrix:\n", W_value)
b_value = session.run(b)
print("Bias:\n", b_value)
