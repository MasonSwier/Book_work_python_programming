# calculator.py
# An interactive calculator

def main():
    print("This is a simple program that lets you run some calculations")
    calc_count = eval(input("How many calculations should we do? "))
    
    for i in range(calc_count):
        expression = eval(input("Enter the expression to be calculated: "))
        print(expression)
    
main()