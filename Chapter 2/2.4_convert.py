# convert.py
#   A program to convert Celsius temperatures to Farenheit

def main():
    print("This program will convert 5 temperatures from Celsius to Farenheit.")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        farenheit = 9/5 * celsius + 32
        print("The temperature is ", farenheit, " degrees Farenheit.")
    input("Press any key to quit.")
    
main()