"""
This file contains  pythno script to identify whether the given year is a leap year or not
"""

def leap_year(year):
    if len(str(year)) == 4:
        try:
            if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
                print("The given year ", year, " is a leap year")
            else: 
                print("The yeat ", year, " is not a leap year")
        except Exception as e:
            return e
    else:
        print("Enter the valid year")
        return main()
        
def main():
    year_to_check = int(input("Enter the year: "))
    leap_year(year_to_check)

if __name__ == "__main__":
    main()
        