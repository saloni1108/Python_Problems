"""
this file contains the python script to compute the sum of nth harmonic number 
"""

def harmonic_num(number):
    total = 0.0
    for i in range(1, number + 1):
        total += 1/i
    return total

def main():
    num = int(input("Enter a number: "))
    try:
        if num < 1:
            raise ValueError("Entered value is incorrect")
        else:
            print("The Nth harmonic value for the number N = ", num, " is ", harmonic_num(num))
    except Exception as e:
        print("The Exception occured says: ", e)
        return main()

if __name__ == "__main__":
    main()