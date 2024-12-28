#!/bin/bash

# user size input
size = int(input("Enter the size of the pattern:"))

# Using loop to give coditions

row = 0

while row < size:
  for i in range(size):
    print("*", end="")
  print()
  row += 1