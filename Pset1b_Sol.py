#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:52:36 2021

@author: keerthi
"""
#The User to enter the following variables:
annual_salary = int(input("Enter the starting annual salary: "))
portion_saved = float(input("Enter the portion of salary to be saved, as a decimal: "))
total_cost = int(input("Enter the cost you dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
monthly_saved = (annual_salary*portion_saved)/12


portion_down_payment = 0.25*total_cost
current_savings = 0
months = 0
step = 0
annual_rate = 0.04

# "While loop" used to match the current savings with the down portion down payment
#and "if" is used to take the count until saving matches with portion down payment

while current_savings < portion_down_payment:
    savings = (current_savings*annual_rate/12) + monthly_saved
    current_savings = current_savings + savings
    if(savings != portion_down_payment):
        months = months + 1        
        step = months - 1          
        if (step%6 == 0 ):
            annual_salary = annual_salary + annual_salary*(semi_annual_raise)
            monthly_saved = (annual_salary*portion_saved)/12    
            #print("\n***\tMonth: ",months,"\tStep: ",step,"\tmonthly saved: ",monthly_saved,"\tsavings: ",savings,"\tcurrent savings",current_savings,"\t***")
        else:
            monthly_saved = monthly_saved 
            #print("\nMonth: ",months,"\tStep: ",step,"\tmonthly saved: ",monthly_saved,"\tsavings: ",savings,"\tcurrent savings",current_savings)
#print("\n Number of months: ",months,"\tportion down payment: ",portion_down_payment)
print("\n Number of months: ",months)