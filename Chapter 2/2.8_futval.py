# futval.py
#   A program to compute the value of an investment
#   carried 10 years into the future given a 

def main():
    print("This program calculates the future value")
    print("of an investment")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    compound_freq = eval(input("Enter the number of times per year that interest is compounded: "))
    
    for i in range(10):
        for i in range(compound_freq):
            principal = principal * (1 + (apr/compound_freq))
    print("The value in 10 years is: ", principal)

main()