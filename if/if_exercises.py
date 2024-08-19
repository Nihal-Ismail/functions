height = float(input("Height in Meter:"))
weight = float(input("Weight in Meter:"))
bmi = weight / (height ** 2)
if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")
