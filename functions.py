def findEvenNumbers(arr):
    even = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
    return even

print(findEvenNumbers([4, 6, 7, 8, 8, 13, 53, 31]))

def sumOfNumbers(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(sumOfNumbers(3,4,5,5,8,9))
print(sumOfNumbers(3,4,5,8, 556,66))

def addAges(**ages):
    total_age = 0
    for age in ages.values():
        total_age += age
    return total_age

def addMoney(**monies):
    total_money = 0
    for k, v in monies.items():
        print(f"{k} has ${v}")
        total_money += v
    return f"Total money is ${total_money}"

print(addMoney(John=23,Jane=35,Tom=18))
print(addAges(John=23,Jane=35,Tom=18))





list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]
sum = 0
sum1 = 0

for elem in list1:
    if (elem % 2 == 0):
        sum = sum + elem
        continue
    if (elem % 3 == 0):
        sum1 = sum1 + elem

print(sum , end=" ")