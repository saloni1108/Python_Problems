"""
This file contains a python script to simulate a gambling scenario that starts with a $stake and bets untill he/she loses or wins
"""
import random
def gamble(stake, goal, trials):
    bets, wins = 0, 0
    for _ in range (trials):
        while stake >= 0 and stake <= goal :
            bets += 1
            if random.random() > 0.5:
                stake += 1
                wins += 1
            else: 
                stake -= 1
    return wins,bets

def main():
    try:
        stake = int(input("Enter the initial stake amount: $ "))
        goal = int(input("Enter the goal amount: $ "))
        num_trials = int(input("Enter the trials: "))
        wins, bets = gamble(stake, goal, num_trials)
        print("After the trials:", num_trials, " Total wins are: ", wins, " and bets are: ", bets)
        win_percent = (wins/bets)*100
        print("win percent is: {:.2f}".format(win_percent))
        print("loss percent is: {:.2f}".format(1-win_percent))
    except ValueError:
        print("Invalid input")
        return main()

if __name__ == "__main__":
    main()