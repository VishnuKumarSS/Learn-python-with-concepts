# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a=round(weight/height**2)
if a<18.5:
    print(f"Your BMI is {a}, you are underweight.")
elif a>=18.5 and a<25:
    print(f"Your BMI is {a}, you have a normal weight.")
elif a>=25 and a<30:
    print(f"Your BMI is {a}, you are slightly overweight.")
elif a>=30 and a<35:
    print(f"Your BMI is {a}, you are obese.")
elif a>=35:
    print(f"Your BMI is {a}, you are clinically obese.")