balance = 3000  

def buy_things(item, price):
    #local scope variable
    #i can access global variable without using the global keyword
    global balance
    #if i want to modify a global variable, i have  yo use the global keyword
    print(f'Previous balance value', balance)
    balance = balance - price
    
    print(f'Balance After Buying{item}', balance)

buy_things('sunglass', 1000)
print('Global balance after buy', balance)
