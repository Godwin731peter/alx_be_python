#!/bin/bash
#User's number choice
number = float(input("Enter a number to see its multiplication table:"))

# Iterating/calculating multiplication table based on user's input

for e in range(1, 11):
  product = number * e
  print(f"{number} * {e} = {product}")