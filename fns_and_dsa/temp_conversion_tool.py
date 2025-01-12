#!/bin/bash

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  # convert temp from fahrebheit to celsius
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  # convert temp from celcius to fahrenheit
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = float(input("Enter the temperature to conver: "))

unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ")

if unit == "F":
  result = convert_to_celsius(temp)
  print(f"{temp}°F is {converted_temp:.2f}°C")
elif unit == "C":
  result = convert_to_fahrenheit(temp)
  print(f"{temp}°C is {converted_temp:.2f}°F")