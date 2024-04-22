"""
this file contains a python script to simulate a stopwatch
"""
import time

import time

def start_stopwatch():
    start_time = time.time()
    print("Stopwatch started...")
    input("Press Enter to stop the stopwatch.")
    end_time = time.time()
    elapsed = end_time - start_time
    HH = int(elapsed // 3600)
    MM = int((elapsed % 3600) // 60)
    SS = int(elapsed % 60)
    print(f"{HH}hrs :{MM} mins :{SS} sec")

def main():
    while True:
        print("\n1. Start Stopwatch\n2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            elapsed_time = start_stopwatch()
            print("Elapsed time:", elapsed_time)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

