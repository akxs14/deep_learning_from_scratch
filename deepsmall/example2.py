#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Execute the code from example 1 in a session."""

from graph import Graph
from graph import Variable
from graph import Placeholder
from operations import matmul
from operations import add
from session import Session

# Create a new graph
Graph().as_default()

# Create variables
A = Variable([[1, 0], [0, -1]])
b = Variable([1,1])

# Create placeholder
x = Placeholder()

# Create hidden node y
y = matmul(A,x)

# Create output node z
z = add(y, b)

session = Session()
output = session.run(z, { x: [1, 2] } )
print(output)