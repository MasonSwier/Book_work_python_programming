# convert.py
#   A program to converts temperatures between Celsius and Farenheit. An expansion of the program presented in the text.

def main():
    print("This program will convert temperatures to and from Celsius and Farenheit.")
    while True:
        starting_method = input("Which temperature scale are you converting FROM? - Choose one: C or F? ")
        starting_method = starting_method.upper()
        if starting_method == "C":
            celsius = eval(input("What is the Celsius temperature? "))
            farenheit = 9/5 * celsius + 32
            print("The temperature is ", farenheit, " degrees Farenheit.")
        elif starting_method == "F":
                farenheit = eval(input("What is the Farenheit temperature? "))
                celsius = (farenheit - 32) * 5/9
                print("The temperature is ", celsius, " degrees Celsius.")
        else:
            print("Error: Please try again with correct temperature scale selection.")
        user_continue = input("Would you like to convert another temperature? (Y/N) ")
        user_continue = user_continue.upper()
        if user_continue == "Y":
            1 == 1
        elif user_continue == "N":
            input("Goodbye! Press any key to quit.")
            quit()
        else:
            input("Error: Quitting program. Goodbye! Press any key to quit.")
            quit()
main()