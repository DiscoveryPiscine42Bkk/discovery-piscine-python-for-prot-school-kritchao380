#!/usr/bin/env python3

def is_zero():
    """Prompts the user for a number and checks if it's zero."""
    try:
        user_input = int(input("Enter a number: "))
        if user_input == 0:
            print("This number is equal to zero.")
        else:
            print("This number is different from zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    is_zero()