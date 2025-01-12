#!/bin/bash

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

shopping_list = []

while True:
  display_menu()
  choice = input("Enter your choice: ").strip()

  if choice == "1":
    item = input("Enter the item to add: ").strip()
    if item:
      shopping_list.append(item)
      print(f"'{item}' has been added to the list")
    else:
      print("item name is empty")
  elif choice == "2":
    item = input("Enter the name of item to remove").strip()
    if item in shopping_list:
      shopping_list.remove(item)
      print(f"'{item}' has been removed from shopping list")
    else:
      print("item is not in shopping list")
  elif choice == "3":
    if shopping_list:
      print("current shoping list")
      for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")
    else:
      print("The shopping list is currently empty")
  elif choice == "4":
    print("Goodbye!")
  else:
    print("Invalid choice. Please try again.")