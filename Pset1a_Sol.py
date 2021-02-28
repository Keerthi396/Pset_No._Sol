#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:52:36 2021

@author: keerthi
"""
#The User to enter the following variables:
annual_salary = int(input("Enter the starting annual salary: "))
portion_saved = float(input("Enter the portion of salary to be saved: "))
total_cost = int(input("Enter the cost you dream house: "))
monthly_saved = (annual_salary*portion_saved)/12

# Standard Requirement
#pdp = float(input("Enter the portion down payment: "))
#portion_down_payment = pdp*total_cost
portion_down_payment = 0.25*total_cost
current_savings = 0
months = 0
#annual_rate = float(input("Enter the annual rate: "))
annual_rate = 0.04

# "While loop" used to match the current savings with the down portion down payment
#and "if" is used to take the count until saving matches with portion down payment
while current_savings < portion_down_payment:
    savings = (current_savings*annual_rate/12) + monthly_saved
    current_savings = current_savings + savings
    if(savings != portion_down_payment):
        months = months + 1
        print("\n------------------------------------------")
        #Output to the programmer.
        print("\n|\tMonth: ",months,"\t|\tsavings: ",round(savings,2),"\t|")
print("\n------------------------------------------")

# Output to the user (Which is important to show)

print("\n\n\n Monthly Savings: ",monthly_saved)
print("\n Portion down payment: ",portion_down_payment)
print("\n Total Savings: ",current_savings)
print("\n Number of months: ",months)