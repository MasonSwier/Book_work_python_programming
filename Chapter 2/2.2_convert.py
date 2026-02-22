# convert.py
#   A program to convert Celsius temperatures to Farenheit

def main():
    print("This program will convert a temperature from Celsius to Farenheit.")
    celsius = eval(input("What is the Celsius temperature? "))
    farenheit = 9/5 * celsius + 32
    print("The temperature is ", farenheit, " degrees Farenheit.")
    input("Press any key to quit.")
    
main()