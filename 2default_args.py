def sum(num1, num2, num3=0, num4=0):
    result = num1 + num2 + num3 + num4
    return result

total = sum(99, 11, 10)
# print('total', total)


# args
def all_sum(*numbers):
    print(numbers)
    sum =0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum

total = all_sum(45,44,11, 20, 50)
print('all sum: ', total)
