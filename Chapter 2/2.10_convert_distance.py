# convert_distance.py
#   A program to convert kilometers to miles

def main():
    kilometers = eval(input("What is the distance in kilometers? "))
    miles = kilometers * 0.62
    print("The distance is ", miles, " miles.")
    
main()