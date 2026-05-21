import time
print("Welcome to my calculator")
time.sleep(1)
while True:
    number = input("What is youre first number?")
    try:
        number1 = int(number)
        if number1 == 0:
            print("The number 0 is not allowed, please try again!")
            time.sleep(2)
            continue
        print("Youre first number is %s" %number)
        break
    except ValueError:
        print("This is not a number, choose a valid number!")
        time.sleep(2)
time.sleep(2)
while True:
    number = input("What is youre second number?")
    try:
        number2 = int(number)
        if number2 == 0:
            print("The number 0 is not allowed, please try again!")
            time.sleep(2)
            continue
        print("Youre second number is %s" %number)
        break
    except ValueError:
        print("This is not a number, choose a valid number!")
        time.sleep(2)
time.sleep(2)
allowedlist = ["addition", "subtraction", "multiplication", "division","Addition", "Subtraction", "Multiplication", "Division", "+", "-", "*", "/"]
while True:
    option = input("How to you wanna make the calculation? (Addition, Subtraction, Multiplication, Division)")
    if option in allowedlist:
        print"Youre Calculation will now be calculated with", option
        break
    else:
        print("This is not an option, choose a valid option!")
        time.sleep(2)
time.sleep(2)
print("Result:")
time.sleep(3)
if option == "addition" or option == "Addition" or option == "+":
    print(number1 + number2)
if option == "subtraction" or option == "Subtraction" or option == "-":
    print(number1 - number2)
if option == "multiplication" or option == "Multiplication" or option == "*":
    print(number1 * number2)
if option == "division" or option == "Division" or option == "/":
    print(number1 / number2)
