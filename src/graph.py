#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The Graph class, which is holding a computational graph """

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
