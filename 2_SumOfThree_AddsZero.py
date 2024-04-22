"""
This file contains a Python file to find the sum of 3 integers that sum up to zero
"""
import random
def find_triplet(list):
    triple = []
    count = 0
    for i in range(0, len(list) - 2):
        for j in range(i+1, len(list) - 1):
            for k in range(j+1, len(list)):
                if list[i] + list[j] + list[k] == 0:
                    triplet = sorted([list[i], list[j], list[k]])
                    if triplet not in triple:
                        triple.append(triplet)
                        count += 1
    return count, triple

def main():
    try:
        num = int(input("Enter the number of integers: "))
        if num < 3:
            print("Cannot find the triplets as the input of integers doesnt match")
            return
        lst = []
        for i in range(num):
            element = random.randrange(-10, 10)
            lst.append(element)
        count, triple = find_triplet(lst)
        print("the number of triplets found are: ", count, "\n The Triplets found are : \n", triple)
    except ValueError:
        print("Iinvalid input")
        return main()
    
if __name__ == "__main__":
    main()
