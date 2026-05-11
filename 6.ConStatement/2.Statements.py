# BASIC PYTHON CONDITIONAL STATEMENTS


age = 18

# if
if age >= 18:
    print("You are an adult")

# if-else
marks = 30
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# if-elif-else
number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# nested if
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")