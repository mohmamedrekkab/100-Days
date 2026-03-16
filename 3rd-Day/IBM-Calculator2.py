#Enter your height in meters e.g., 1.55
height = float(input())
#Enter your weight in kg e.g., 72
weight = float(input())
bmi =weight /height ** 2

if bmi < 18.28678:
    print(f"your BMI is {bmi}, you are underweight")
elif bmi < 22.0:
    print(f"your BMI is {bmi}, you habe a normal weight")
elif bmi <28.50752:
    print(f"your BMI is {bmi}, you are slightly overweight")
elif bmi < 32.56189:
    print(f"your BMI is {bmi}, you are obese")
elif bmi >= 37.50000:
    print(f"your BMI is {bmi}, you are clinically obese")