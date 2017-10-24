#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The matmul class, extends the Operation class and adds the
    multiplication functionality in our system."""

from operation import Operation

class matmul(Operation):
	"""Multiplies matrix a by matrix b, producing a * b."""
	
	def __init__(self, a, b):
		""" Constructor 

		Args:
			a: First matrix
			b: Second matrix
		"""
		super().__init__([a,b])

	def compute(self, a_value, b_value):
		""" Compute the output of the matmul operation. 

		note: The function parameters should be numpy arrays.

		Args:
			a_value: First matrix value
			b_value: Second matrix value
		"""
		self.input = [a_value, b_value]
		return a_value.dot(b_value)
