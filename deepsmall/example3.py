#!/usr/bin/env python
#! -*- coding: utf-8 -*-

""" Build a perceptron that classifies a point between two sets
	which are divided by a line between (4,0) and (0,4).
"""

from graph import Graph
from graph import Variable
from graph import Placeholder
from operations import matmul
from operations import add
from operations import sigmoid
from session import Session

# Create a new graph
Graph().as_default()

x = Placeholder()
w = Variable([1, 1])
b = Variable(0)
p = sigmoid( add( matmul( w, x), b) )

# Let's try it to calculate the probability for point (3,2)T 
# being a blue point (being over the line or p(wTx+b) > 0.5)
session = Session()
print(session.run(p, {
	x: [3, 2]
}))
