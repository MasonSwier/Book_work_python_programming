# convert.py
#   A program to convert Farenheit temperatures to Celsius

def main():
    farenheit = eval(input("What is the Farenheit temperature? "))
    celsius = (farenheit - 32) * 5/9
    print("The temperature is ", celsius, " degrees Celsius.")
    
main()