"""
this file contains the python script to 
"""

def power_of_2(number):
    for i in range(0, number):
        power_value = 2 ** number
    print("The powe value of 2 for the value '", number, "' is : ",power_value)


def main():
    power = int(input("Enter the Power Value: "))
    try:
        if power < 0 or power > 31:
            raise ValueError("Enter the value between 0 and 31")
        else:
            power_of_2(power)
    except Exception as e:
        print("there is some Exception: ", e)
        return main()

if __name__ == "__main__":
    main()