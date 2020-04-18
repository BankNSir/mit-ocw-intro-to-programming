#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:25:42 2020

@author: natawat
"""

# user input annual_salary, portion saved, total_cost

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salaryto save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04 # return of investment (annual rate)
monthly_salary = annual_salary / 12
down_cost = portion_down_payment * total_cost

month_passed = 0
while current_savings < down_cost:
    if month_passed % 6 == 0 and month_passed != 0:            
        monthly_salary += monthly_salary * semi_annual_raise
    month_passed += 1
    current_savings += current_savings*r/12 + monthly_salary*portion_saved

print("Number of month: {}".format(month_passed))




