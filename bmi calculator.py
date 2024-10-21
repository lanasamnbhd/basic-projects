def bmiCounter(weight, height):
    bmi = weight / (height ** 2)
    return bmi
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = bmiCounter(weight, height)
print(f"Your bmi is {bmi:.2f}")

if bmi<18.5:
    print("You are underweight")
elif 18.5 <= bmi < 24.9:
    print("You are middle weight")
elif 24.9 <= bmi <29.9:
    print("You are overweight")
else:
    print("You are obese")
