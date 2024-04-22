

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()  # Prompt user for input
    user_input = user_input.split(',')  # Split input string by commas
    mylist = [float(x) for x in user_input]  # Convert split values to floats
    return mylist

def calc_average():
    numbers = get_user_input()  # Get list of numbers from user input
    total = sum(numbers)  # Calculate sum of numbers
    average = total / len(numbers)  # Calculate average
    print("Average is:", average)

# Call functions to display menu, get user input, and calculate average
display_main_menu()
calc_average()