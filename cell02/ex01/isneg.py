#!/usr/bin/env python3

def is_negative():
    """Prompts the user for a number and checks if it's negative, positive, or zero."""
    try:
        user_input = int(input("Enter a number: "))
        if user_input < 0:
            print("This number is negative.")
        elif user_input > 0:
            print("This number is positive.")
        else:
            print("This number is both positive and negative.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    is_negative()