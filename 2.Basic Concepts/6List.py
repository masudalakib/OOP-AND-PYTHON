#list, array, collection is same(simple terms)

# index =  0  1   2   3   4   5   6    7 
numbers =[45, 54, 12, 43, 89, 32, 66, 90]
# index =  -8  -7  -6  -5  -4 -3   -2   -1  py teiemne o kam kore

print(numbers[3], numbers[-3])


#list (start : end)  #start from the start index and stops before the end index
print(numbers[2:6])
print(numbers[1:7])



#list (start : end: step)  
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[1:7:-1])
print(numbers[7:2:-1])
print(numbers[2:])
print(numbers[:2])
print(numbers[:]) #short cut to copy list
print(numbers[::-1])  # shortcut to reverst a list

