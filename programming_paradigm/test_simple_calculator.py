#!/bin/bash
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

  def setUp(self):
    self.calc = SimpleCalculator()

  def test_addition(self):
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)
    self.assertEqual(self.calc.add(-2, -4), -6)
    self.assertEqual(self.calc.add(0, 0), 0)
    self.assertEqual(self.calc.add(1.5, 2.9), 4.4)

  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(4, 2), 2)
    self.assertEqual(self.calc.subtract(2, 4), -2)
    self.assertEqual(self.calc.subtract(-2, -3), 1)
    self.assertEqual(self.calc.subtract(0, 0), 0)
    self.assertEqual(self.calc.subtract(2.5, 1.2), 1.3)

  def test_multiplication(self):
    self.assertEqual(self.calc.multiply(2, 3), 6)
    self.assertEqual(self.calc.multiply(-6, 3), -18)
    self.assertEqual(self.calc.multiply(-6, -3), 18)
    self.assertEqual(self.calc.multiply(0, 3), 0)
    self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

  def test_divide(self):
    self.assertEqual(self.calc.divide(6, 3), 2)
    self.assertEqual(self.calc.divide(-6, 3), -2)
    self.assertEqual(self.calc.divide(-6, -3), 2)
    self.assertEqual(self.calc.divide(0, 3), 0)
    self.assertEqual(self.calc.divide(5, 2), 2.5)
    self.assertEqual(self.calc.divide(5, 0))

  def test_division_by_zero(self):
    self.assertIsNone(self.calc.divide(10, 0))
    self.assertIsNone(self.calc.divide(0, 0))