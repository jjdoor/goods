for i in range(1,9):
    print(i)
r = range(1, 9)
print(r)

numbers = [12,37,5,42,8,3]
temp = numbers[:]
even = []
odd  = []
while len(numbers)>0:
    number = numbers.pop()
    if(number%2 == 0):
        even.append(number)
    else:
        odd.append(number)
print(temp)
print(numbers)
print(even)
print(odd)
