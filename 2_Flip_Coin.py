'''
A Python Script to take the user input to flip a coin and calculate the percentage of the appearances of heads and tails
'''
import random

def flip_coin(num_of_toss):
    if num_of_toss >=0:
        try:
            tail, heads = 0, 0
            for i in range(0, num_of_toss):
                toss = random.randint(0,1)
                if toss == 0:
                    tail += 1
                else:
                    heads += 1
            heads_percent = ((heads / num_of_toss)*100)
            tail_percent = ((tail / num_of_toss)*100)
            print("The occurence of heads is ", heads_percent, "%")
            print("The occurence of tails is ", tail_percent, "%")
        finally:
            print("done")
    else:
        try:
            print("Enter a positive integer")
        except Exception as e:
            return e

def main():
    number = int(input("Enter how many tosses you want: "))
    flip_coin(number)

if __name__ == "__main__":
    main()