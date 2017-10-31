#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""	Multi-class perceptron """

from graph import Graph
from graph import Variable
from graph import Placeholder
from operations import matmul
from operations import add
from operations import sigmoid
from operations import softmax
from session import Session
import numpy as np

# Create a new graph
Graph().as_default()

X = Placeholder()

# Create a weight matrix for 2 outout classes:
# One with a weight vector (1, 1) for blue and one with a 
# weight vector (-1, -1) for red
W = Variable([
	[1, -1],
	[1, -1]
])

b = Variable([0, 0])
p = softmax( add( matmul( X, W), b) )

# Create red points centered at (-2, -2)
red_points = np.random.randn(50, 2) - 2*np.ones((50, 2))
# Create blue points centered at (2, 2)
blue_points = np.random.randn(50, 2) + 2*np.ones((50, 2))

# Create a session and run the perceptron on our blue/red point
session = Session()
output_probabilities = session.run(p, {
	X: np.concatenate((blue_points, red_points))
})

print(output_probabilities[:10])
