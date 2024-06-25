def full_name(first, last):
    name = f'{first} {last}'
    return name

# take peramiters in order(sirial wise)
# name = full_name('Mr', 'Mofiz')

name = full_name(last='Mr', first='Mofiz')
print(name)



# der famous(**kargs)

def famous_name(firsst, lasr, **addition):
    name = f'{first} {last}'
    print(addition)
    return name

name = famous_name(first='Taheri ', last='Ali', title ='Hujur', addition=Waz) 
print(name)
