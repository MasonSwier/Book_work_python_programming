# sphere.py
#
# Program calculates the volume and surface area of a sphere

import math

def main():
    print("This program will use the radius of a sphere to calculate its volume and surface area.")
    radius = int(input("Please provide the radius of your sphere: "))
    
    volume = (4/3) * math.pi * (radius ** 3)
    surface_area = 4 * math.pi * (radius ** 2)
    
    print("The volume of the sphere is", volume)
    print("The surface area of the sphere is", surface_area)
    input("Press any key to quit.")

main()
