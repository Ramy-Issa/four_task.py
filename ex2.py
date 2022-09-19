from math import *
input1 = input("Enter first number: ")
first_num = input1.isdigit()
if first_num:
    number1 = int(input1)

print("1_+\n2_-\n3_*\n4_/\n5_^\n6_%\n")
input3 = input("Choose the prosses: ")

input2 = input("Enter second number: ")
second_num = input2.isdigit()
if second_num:
    number2 = int(input2)

if input3 == "1" or input3 == "+":
    result=number1 + number2
    print(f"{number1} + {number2} = {result}")
    print("1-Round\n2-Biggest value\n3-Smallest value\n4-Exit")
    input4 = input("Choose: ")
    if input4 == "1":
        end_result = round(result)
        print(end_result)
    elif input4 == "2":
        end_result = ceil(result)
        print(end_result)
    elif input4 == "3":
        end_result = floor(result)
        print(end_result)
    else:
        SystemExit


elif input3 == "2" or input3 == "-":
    result=number1 - number2
    print(f"{number1} - {number2} = {result}")
    print("1-Round\n2-Biggest value\n3-Smallest value\n4-Exit")
    input4 = input("Choose: ")
    if input4 == "1":
        end_result = round(result)
        print(end_result)
    elif input4 == "2":
        end_result = ceil(result)
        print(end_result)
    elif input4 == "3":
        end_result = floor(result)
        print(end_result)
    else:
        SystemExit
elif input3 == "3" or input3 == "*":
    result=number1 * number2
    print(f"{number1} * {number2} = {result}")
    print("1-Round\n2-Biggest value\n3-Smallest value\n4-Exit")
    input4 = input("Choose: ")
    if input4 == "1":
        end_result = round(result)
        print(end_result)
    elif input4 == "2":
        end_result = ceil(result)
        print(end_result)
    elif input4 == "3":
        end_result = floor(result)
        print(end_result)
    else:
        SystemExit
elif input3 == "4" or input3 == "/":
    result=number1 / number2
    print(f"{number1} / {number2} = {result}")
    print("1-Round\n2-Biggest value\n3-Smallest value\n4-Exit")
    input4 = input("Choose: ")
    if input4 == "1":
        end_result = round(result)
        print(end_result)
    elif input4 == "2":
        end_result = ceil(result)
        print(end_result)
    elif input4 == "3":
        end_result = floor(result)
        print(end_result)
    else:
        SystemExit
elif input3 == "5" or input3 == "^":
    result=number1 ** number2
    print(f"{number1} ^ {number2} = {result}")
    print("1-Round\n2-Biggest value\n3-Smallest value\n4-Exit")
    input4 = input("Choose: ")
    if input4 == "1":
        end_result = round(result)
        print(end_result)
    elif input4 == "2":
        end_result = ceil(result)
        print(end_result)
    elif input4 == "3":
        end_result = floor(result)
        print(end_result)
    else:
        SystemExit
elif input3 == "6" or input3 == "%":
    result=number1 % number2
    print(f"{number1} % {number2} = {result}")
    print("1-Round\n2-Biggest value\n3-Smallest value\n4-Exit")
    input4 = input("Choose: ")
    if input4 == "1":
        end_result = round(result)
        print(end_result)
    elif input4 == "2":
        end_result = ceil(result)
        print(end_result)
    elif input4 == "3":
        end_result = floor(result)
        print(end_result)
    else:
        SystemExit
