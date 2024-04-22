def display_main_menu(): 
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    user_input = user_input.split()
    mylist = [user_input]
    return mylist

def calc_average():
    list = [get_user_input]
    total = sum(list)
    average = total/ len(list)
    print("average")
    
def find_min_max():
    print("find_min_max")
def sort_temperature():
    print("sort_temperature")
def calc_median_temperature():
    print("calc_median_temperature")
