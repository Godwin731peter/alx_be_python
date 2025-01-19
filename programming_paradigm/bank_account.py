#!/bin/bash
class BankAccount:
  def __init__(self, account_balance=0):
    self.account_balance = account_balance

  def deposit(self, amount):
    return amount + self.account_balance
  
  def withdraw(self, amount):
    if self.account_balance > amount:
      BankAccount.account_balance -= amount
      return True
    else:
      return False
    
  def display_balance(self):
    amount = self.account_balance
    print(f"Current Balance: ${amount}")