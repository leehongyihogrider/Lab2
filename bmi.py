def calculate_bmi(height, weight): 
    result = []
    print("Height = " + str(height)) 
    print("Weight = " + str(weight)) 

#Add code here to calculate BMI 
    bmi=(weight/(height**2))
#Add code here to display calculate BMI 
    print("BMI =" +str(bmi)) 
    if bmi < 18.5:
        print("User is underweight")
        return -1
    elif bmi >= 18.5 and bmi <= 25.0:
        print("User is normal weight")
        return 0
    else:
        print("User is overweight")
        return 1
calculate_bmi(weight=57, height=1.73)
