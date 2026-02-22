# convert.py
#   A program to convert Celsius temperatures to Farenheit

def main():
    print("This program generates a range temperature conversions from Celsius to Farenheit.")
    for i in range(0, 101, 10):
        celsius = i
        farenheit = 9/5 * celsius + 32
        print(celsius, " - ", farenheit)
    input("Press any key to quit.")
    
main()