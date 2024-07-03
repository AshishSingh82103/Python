# Q:1
# age = input("Provide me an age: ")
# ageInInt = int(age)
age = 25;

if age < 13:
    print("Child");
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")  
else:
    print("Senior")   


# Q2:
age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8
if day == "Wednesday":
    # price = price - 2
    price -= 2
    print("Ticket price is $:",price)

# Q3;

score = 85

if score >= 101:
    print("Please verify your grade again")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade);

# Q4:
fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")

else:
    print("there is no information about the fruit")


# Q5:
weather = "Sunny"
if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read abook"
elif weather == "Snowy":
    activity = "Build a snowman"

print(activity)

# Q6:
speed = 85

if speed < 3:
    transport = "Walk"
elif speed <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends you the transport of:",transport)

# Q7:
order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"
print("Order:", coffee)

# Q8:
password = "Secure3P@ss"

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"
print("Password strength is:", strength)


# Q9
year = 2024
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "Leap year")

else:
    print(year, "is not a leap year")
    PermissionError()

 



















