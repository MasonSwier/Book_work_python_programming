# futval.py
#   A program to compute the value of an investment
#   carried any number of years into the future

def main():
    print("This program calculates the future value")
    print("of a an investment")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    length = eval(input("Enter the number of years for your investment: "))
    compound_freq = eval(input("Enter the number of times per year that interest is compounded: "))
    investment = eval(input("Enter the total of additional annual investment amounts: "))
    
    for i in range(length):
        principal = (principal + investment)
        for i in range(compound_freq):
            principal = principal * (1 + (apr/compound_freq))
        print("The value in ", length, " years is: ", principal)

main()print