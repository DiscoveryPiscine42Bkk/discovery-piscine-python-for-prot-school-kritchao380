
num = input("Give me a number: ")


if '.' in num:
 
        float_num = float(num)
        if float_num.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")

        print("Invalid input. Please enter a valid number.")
else:
    print("This number is an integer.")
