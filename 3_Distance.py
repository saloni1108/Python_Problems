"""
This python script consist of a code that can be used to calculate the eucledian distance od the points taken as input to the origin
"""

import math

def distance(point):
    eucledian_distance = math.sqrt((point[0]**2) + (point[1]**2))
    return eucledian_distance

def main():
    try:
        x = int(input("Enter the x-coordinate for the point: "))
        y = int(input("Enter the y-coordinate of the point: "))
        user_point = [x, y]
        print("The Eucledian Distance id: ", distance(user_point))
    except TypeError:
        print("Invalid Input")
        return main()
    
if __name__ == "__main__":
    main()