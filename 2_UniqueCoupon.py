"""
This file contains a python script to randomly generate unique coupon numbers
"""
import random

class CouponGenerator:
    @staticmethod
    def generate_coupon(num):
        return random.randint(1, num)
    
    @staticmethod
    def coupon(num):
        distinct_coupun = set()
        total_coupon = 0
        while len(distinct_coupun)< num:
            coupon = CouponGenerator.generate_coupon(num)
            total_coupon += 1
            distinct_coupun.add(coupon)
        return total_coupon
    
def main():
    try:
        number = int(input("Enter the number of distinct coupon number: "))
        if number <= 0:
            print("Please enter a positive number")
            return
        total_coupon = CouponGenerator.coupon(number)
        print("Total random numbers needed to have all distinct numbers:", total_coupon)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()