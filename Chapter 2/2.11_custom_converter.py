# custom_converter.py
#   A program to convert height into crazy dip candys

def main():
    print("This converter converts your height in inches to a classic candy my wife loves.")
    
    height = eval(input("How many inches tall are you? "))
    crazy_dip_height = height/2.46
    
    print("Wow! That's ", crazy_dip_height, ' Crazy Dip candies high! Remember those things?')
    input("Press any key to quit")

main()