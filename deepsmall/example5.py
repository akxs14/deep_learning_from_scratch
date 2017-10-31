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
from operations import negative
from operations import log
from operations import reduce_sum
from operations import multiply
from session import Session
import numpy as np

# Create a new graph
Graph().as_default()

X = Placeholder()
c = Placeholder()

# Create a weight matrix for 2 outout classes:
# One with a weight vector (1, 1) for blue and one with a 
# weight vector (-1, -1) for red
W = Variable([
	[1, -1],
	[1, -1]
])

b = Variable([0, 0])
p = softmax( add( matmul( X, W), b) )

# Cross-entropy loss
J = negative(reduce_sum(reduce_sum(multiply(c, log(p)), axis=1)))

# Create red points centered at (-2, -2)
red_points = np.random.randn(50, 2) - 2*np.ones((50, 2))
# Create blue points centered at (2, 2)
blue_points = np.random.randn(50, 2) + 2*np.ones((50, 2))

session = Session()
print(session.run(J, {
	X: np.concatenate((blue_points, red_points)),
	c:
		[[1, 0]] * len(blue_points)
		+ [[0, 1]] * len(red_points)
	}))
