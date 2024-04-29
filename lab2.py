def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()  
    user_input = user_input.split(',')  
    mylist = [float(x.strip()) for x in user_input]  
    return mylist

def calc_average(numbers):
    total = sum(numbers)  
    average = total / len(numbers)  
    print("Average is:", average)
    return [average]
def find_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    print("Minimum value:", min_value)
    print("Maximum value:", max_value)
    return [min_value,max_value]
def sort_temperature(numbers):
    sorted_floats = numbers.sort()
    print("Sorted floats:", sorted_floats)
    return [sorted_floats]
def calc_median_temperature(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        middle1 = sorted_numbers[length // 2 - 1]
        middle2 = sorted_numbers[length // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_numbers[length // 2]
    
    print("Median temperature is" , median )
    return [median]
def main():
    display_main_menu()
    numbers = get_user_input()
    
    calc_average(numbers)
    find_min_max(numbers)
    sort_temperature(numbers)
    calc_median_temperature(numbers)

if __name__ == "__main__":
    main()