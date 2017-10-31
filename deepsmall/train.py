#!/usr/bin/env python
# -*- coding: utf-8 -*-

from queue import Queue
from graph import Graph
from graph import Variable

class GradientDescentOptimizer:

    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def minimize(self, loss):
        learning_rate = self.learning_rate

        class MinimizationOperation(Operation):
            def compute(self):
                # Compute gradients
                grad_table = compute_gradients(loss)

                # Iterate all variables
                for node in grad_table:
                    if type(node) == Variable:
                        # Retrieve gradient for this variable
                        grad = grad_table[node]

                        # Take a step along the direction of the negative gradient
                        node.value -= learning_rate * grad

        return MinimizationOperation()

