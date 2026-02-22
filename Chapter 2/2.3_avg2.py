# avg2.py
# A simple program to average three exam scores
# Illustrates use of multiple input

def main():
    print("This program computes the average of three exam scores.")
    
    score_1, score_2, score_3 = eval(input("Enter three scores seperated commas: "))
    average = (score_1 + score_2 + score_3) / 3
    
    print("The average of the three scores is: ", average)

main()