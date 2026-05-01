# pizza_cost.py
#
# This program calculates the cost per square inch of pizza.

import math

def main():
    print("This program will calculate a pizza's cost per square inch.")
    diameter = int(input("Please provide the diameter in inches of your pizza: "))
    price = float(input("Please provide the price of your pizza: "))
    
    radius = diameter / 2
    
    area = math.pi * (radius ** 2)
    
    cost_per_inch = price / area
    
    print("Your pizza costs $", round(cost_per_inch,2), "per square inch.")
    input("Press any key to quit")

main()