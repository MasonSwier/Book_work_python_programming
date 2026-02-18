# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:"))
    a = x
    b = x
    c = x
    for i in range(100):
        a = 3.9 * a * (1-a)
        b = 3.9 * (b - b * b)
        c = 3.9 * c - 3.9 * c * c
        print(a, b, c)

main()