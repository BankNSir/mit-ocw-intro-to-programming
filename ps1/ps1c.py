#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:25:42 2020

@author: natawat
"""

# user input annual_salary, portion saved, total_cost

# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salaryto save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream house: "))
# semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
annual_salary = float(input("Enter your starting salary: "))
based_monthly_salary = annual_salary/12


total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = 0.25
current_savings = 0
r = 0.04 # return of investment (annual rate)
# monthly_salary = annual_salary / 12
down_cost = portion_down_payment * total_cost

month_passed = 0
month_needed = 36
# bisection setup
bisection_step = 0
low = 0
initial_high = 10000
high = initial_high
guess = (low+high) // 2 # in decimal
is_possible = True

while abs(current_savings - down_cost) > 100:
    
    month_passed = 0
    monthly_salary = based_monthly_salary
    current_savings = 0
    
    for i in range(month_needed):
        if i % 6 == 0 and i != 0:
            monthly_salary *= 1 + semi_annual_raise
            
        current_savings += current_savings * r/12 + (guess/10000.0) * monthly_salary
    
    if current_savings < down_cost:
        low = guess
    else:
        high = guess
    
    guess = (low + high) // 2

    if initial_high - guess <= 1:
        print("It is not possible to pay the down payment in three years")
        is_possible = False
        break
    
    bisection_step += 1
    






# while abs(current_savings - down_cost) > 100:
    
#     for i in range(month_needed):
#         if i % 6 == 0 and i != 0:            
#             monthly_salary += semi_annual_raise
#         current_savings += current_savings*r/12 + (guess/10000)*monthly_salary
    
#     if current_savings < down_cost:
#         low = guess
#     else:
#         high = guess
    
#     print(current_savings)
#     guess = (low+high)/2
#     bisection_step += 1

# while current_savings < down_cost:
#     if month_passed % 6 == 0 and month_passed != 0:            
#         monthly_salary += monthly_salary * semi_annual_raise
#     month_passed += 1
#     current_savings += current_savings*r/12 + monthly_salary*portion_saved

# print("Number of month: {}".format(month_passed))

if is_possible:
    print("Best saving rate: ", guess/10000)
    print("Step in bisection search: ", bisection_step)






