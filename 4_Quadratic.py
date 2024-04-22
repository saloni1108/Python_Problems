"""
This file contains the python scrip to calculate the roots of a quadratic equation a*x*x + b*x + c
"""
import math
def quadratic_roots(a, b, c):
    delta = b*b - 4*a*c
    root_1 = (-b + math.sqrt(delta)) / (2*a)
    root_2 = (-b - math.sqrt(delta)) / (2*a)
    print("The roots for given quadratic equation: ", " are \n : root 1:\t", root_1, "and root 2:\t", root_2)

def main():
    try:
        a = int(input("Enter the coefficients: "))
        b = int(input("Enter the coefficients: "))
        c = int(input("Enter the coefficients: "))

    except Exception as e:
        print("Invalid input")
        return main()
    quadratic_roots(a, b, c)
if __name__ == "__main__":
    main()