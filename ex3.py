n = int(input("Enter number of values: "))
arr =[]
for i in range(n):
    numbers = int(input(f"number{i+1} = "))
    arr.append(numbers)
print(arr)
print(max(arr))
print(min(arr))
