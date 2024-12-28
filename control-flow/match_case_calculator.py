#!/bin/bash
# Users input base
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

#applying match statement for conditions and calculations
match operation:
  case "+":
    result = num1 + num2
    print(f"The result is {result}.")
  case "-":
    result = num1 - num2
    print(f"The result is {result}.")
  case "*":
    result = num1 * num2
    print(f"The result is {result}.")
  case "/":
    if num2 == 0:
      print("Cannot divide by zero.")
    else:
      result = num1 / num2
      print(f"The result is {result}.")