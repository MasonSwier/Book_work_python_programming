# futval.py
#   A program to compute the value of an investment
#   carried any number of years into the future

def main():
    print("This program calculates the future value")
    print("of an investment")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    length = eval(input("Enter the number of years for your investment: "))
    
    for i in range(length):
        principal = principal * (1 + apr)
    
    print("The value in ", length, " years is: ", principal)

main()