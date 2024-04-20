"""
This file contains  pythno script to identify whether the given year is a leap year or not
"""

def leap_year(year):
        if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
            print("The given year ", year, " is a leap year")
        else:
            print("Year is not a leap year")
        
def main():
    year_to_check = int(input("Enter the year: "))
    try:
        if len(str(year_to_check)) != 4:
            raise ValueError("Enter a valid year")
    except Exception as e:
         print("The Exception occured is: ", e) 
         return main()
    leap_year(year_to_check)

if __name__ == "__main__":
    main()
        