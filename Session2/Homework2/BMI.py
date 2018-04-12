m = int(input("Input your weight (kg): "))

n = int(input("Input your height (cm): "))

a = float(n / 100)

BMI = m / (a * a)

if BMI < 16:
    print("Your BMI is: ", BMI," - which means you are severely underweight")
elif 16 <= BMI < 18.5:
    print("Your BMI is: ", BMI," - which means you are underweight")
elif 18.5 <= BMI < 25:
    print("Your BMI is: ", BMI," - which means you are normal")
elif 25 <= BMI < 30:
    print("Your BMI is: ", BMI," - which means you are overweight")
elif BMI > 30:
    print("Your BMI is: ", BMI," - which means you are obese")
else:
    print("There is an error with your input")
