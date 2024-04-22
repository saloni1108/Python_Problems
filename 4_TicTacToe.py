"""
this file contains a python script for a cross game or a tic tac tor game
"""

import random

def print_board(board):
    for row in board:
        print(" - "*5)
        print("  |  ".join(row))
    print(" - "*5)

def winner(board, player):
    for i in range(3):
        if any(all(cell == player for cell in row)for row in board) or \
            any(all(row[i]== player for row in board) for i in range(3)):
            return True
        
        diag_1 = [board[i][i] for i in range (3)]
        diag_2 = [board[i][2 - i] for i in range(3)]
        if all(cell == player for cell in diag_1) or all(cell == player for cell in diag_2):
            return True
    return False

def draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2) to place 'X': "))
            col = int(input("Enter the column (0, 1, or 2) to place 'X': "))
            if board[row][col] != ' ':
                print("Cell already occupied. Try again.")
                continue
            board[row][col] = 'X'
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 2.")
    print_board(board)
        
def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', and the computer is 'O'.")
    print_board(board)

    while True:
        move(board)
        if winner(board, 'X'):
            print("Congratulations! You win!")
            break

        if draw(board):
            print("It's a draw!")
            break

        print("Computer's move:")
        row, col = computer_move(board)
        print(f"Computer placed 'O' at row {row} and column {col}.")
        print_board(board)

        if winner(board, 'O'):
            print("Computer wins! Better luck next time.")
            break

        if draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()