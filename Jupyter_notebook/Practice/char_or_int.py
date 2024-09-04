# Take input from the user
user_input = input("Enter a character: ")

# Check if the input is a single character
if len(user_input) == 1:
    # Check if the input is a digit
    if user_input.isdigit():
        print("Digit")
    # Check if the input is an alphabetic character
    elif user_input.isalpha():
        print("Character")
    else:
        print("None")
else:
    print("None")