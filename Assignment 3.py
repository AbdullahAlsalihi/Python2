


#input
weight_input = input("Enter your weight in Kilograms: ")
height_input = input("Enter your height in meters: ")

#Convert Input
weight = float(weight_input)
height = float(height_input)

#processing
bmi = weight / (height ** 2)

#Output
print("Your BMI is: ", bmi)