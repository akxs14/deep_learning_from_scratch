#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The Variable class, is the type of a variable held in a graph node."""

from graph import Graph

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
