#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The Operation class, which represents the graph nodes of a computational
    graph."""

from graph import Graph

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


