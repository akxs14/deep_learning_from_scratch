#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The add class, extends the Operation class and adds the addition
    functionality in our system."""

from operation import Operation

class add(Operation):
	""" Returns x + y element-wise. """

	def __init__(self, x, y):
		""" The class Constructor

		Args:
			x: First summand node
			y: Second summand node
		"""
		super().__init__([x,y])

	def compute(self, x_value, y_value):
		""" Compute the output of the add operation

		Args:
			x_value: First summand value
			y_value: Second summand value
		"""
		self.inputs = [x_value, y_value]
		return x_value + y_value
