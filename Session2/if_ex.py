yob = int(input("Your yob: "))
age = 2018 - yob

if age < 10:
    print("Baby")

elif age < 18:
    print("Teenager")

else:
    print("Adult")
