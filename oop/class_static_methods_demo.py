#!/bin/bash
class Calculator:
  calculate_type = "Arithmetic operations"

  @staticmethod
  def add(a, b):
    return a + b
  
  @classmethod
  def multiply(cls, a, b):
    print(f"Calculation type: {cls.calculate_type}")
    return a * b