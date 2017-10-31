#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Graph:
    """ Represents a computational graph """

    def __init__(self):
        """ Constructor"""
        self.operations = []
        self.placeholders = []
        self.variables = []

    def as_default(self):
        global _default_graph
        _default_graph = self



class Operation:
    """ Represents a graph node that performs a computation.
        An 'Operation' is a node in a 'Graph' that takes zero objects as input.
    """
    def __init__(self, input_nodes = []):
        """Constructor"""
        self.input_nodes = input_nodes

        # Initialize list of consumers
        self.consumers = []

        # Append this operation to the list of consumers of all input nodes
        for input_node in input_nodes:
            input_node.consumers.append(self)

        # Appen this operation to the list of operations in the currently
        # active default graph
        _default_graph.operations.append(self)


    def compute(self):
        """ Computes the output of this operation.
            Must be implemented by the particular operation.
        """
        pass


class Placeholder:
    """ Represents a placeholder node that has to be provided with a
        value computing the output of a computational graph.
    """

    def __init__(self):
        """ Constructor"""
        self.consumers = []

        # Append this placeholder to the list of placeholders in the 
        # currently active default graph.
        _default_graph.placeholders.append(self)




class Variable:
    """ Represents a variable, in a node of a computational graph."""

    def __init__(self, initial_value = None):
        """ Constructor

        Args:
            initial_value: The initial value of the variable
        """
        self.value = initial_value
        self.consumers = []

        # Append this variable to the list of variables in the currently
        # active computational graph
        _default_graph.variables.append(self)


