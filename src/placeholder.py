#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The placeholder class. Its role is to hold the value of a variable 
 	which is goin to be used by an operation as an input. 
 """

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


