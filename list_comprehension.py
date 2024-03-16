numbers = [4, 6, 7, 8, 8, 13, 53, 31]

doubleNum = [num * 2 for num in numbers]

evenNum = []
oddNum = []
for num in numbers:
    if num % 2 == 0:
        evenNum.append(num)
    else:
        oddNum.append(num)
print("Even Numbers: ", evenNum)
print("Odd Numbers : ", oddNum)
print("Even Numbers are : ", evenNum)
print(doubleNum)