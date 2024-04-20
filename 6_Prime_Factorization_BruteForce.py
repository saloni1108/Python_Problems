"""
this file contains a python script to compute the prime factoization of a given number using Brute Force
"""

def prime_factorization(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
        while divisor * divisor <= number:
            if number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            else:
                break
    return factors

def main():
    number_to_factorize = int(input("Enter the number: "))
    try:
        if number_to_factorize < 1:
            raise ValueError("Do check the Value you entered again..")
        else:
            print("the prime factorization of the given number ", number_to_factorize, " is ", prime_factorization(number_to_factorize))
    except Exception as e:
        print("an exception occured: ", e)
        return main()

if __name__ == "__main__":
    main()