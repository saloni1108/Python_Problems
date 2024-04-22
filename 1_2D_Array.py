"""
This file contains a python scrip to Read a 2D array from the standard input and print the array as output
"""
import numpy as np
import random
def array_2D(arr, rows, columns):
    two_d_array = np.resize(arr, [rows, columns])
    return two_d_array

def main():
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of Columns: "))
    elements = []
    try:
        for i in range(0, (row*col)):
            element = random.randrange(0,100)
            elements.append(element)
    except ValueError as e:
        print("There is a Exception wherein you have used the wrong datatype")
        return main()
    print("The 2D array is as follows: \n", array_2D(elements, row, col))

if __name__ == "__main__":
    main()