#!/bin/bash
from datetime import datetime, timedelta

def display_current_datetime():
  # saving crrent date
  current_date = datetime.now()
  # display the current date and time in the format YYYY-MM-DD HH:MM:SS.
  print(f"current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

number_of_days = input("Enter number of days to add to the current date:")

def calculate_future_date():
  # getting the current date
  current_date = datetime.now()
  # calculate future date
  future_date = current_date + timedelta(days=number_of_days)
  # formate and print future date
  print(f"future date: {future_date.strftime('%Y-%m-%d')}") 