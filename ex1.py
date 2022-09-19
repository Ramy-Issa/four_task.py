input1 = input("Enter your name: ")
name = input1.isdigit()
if name:
    print("Wrong entry")
    exit()
input2 = input("Enter your age: ")
age = input2.isdigit()
if age:
    pass
else:
    print("Wrong entry")
    exit()
input3 = input("Enter your address: ")
print(f"Hello Mr/Ms {input1} age {input2} located in {input3}.thanks for beening one of our community,Enjoy")
