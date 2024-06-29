numbers = [12,42,54,7,6]
numbers.append(99) #number add
print(numbers)

numbers.insert(0,69)  # 0 no index e 69 
numbers.insert(2,9)  # 2 no index e 9 
print(numbers)

numbers.remove(12)
print(numbers)

last = numbers.pop()  
print(last, numbers)

index = numbers.index(7)
print(index)