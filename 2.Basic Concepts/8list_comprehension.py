numbers = [3, 5, 11, 16, 22,27, 32, 65, 87,99, 70]
odds =[]
for num in numbers:
    if num % 2 == 1 and num % 5 ==0:  # kono number k 2 diye vag korle vag sesh jodi 1 er soman hoi, taile bijor. and 5 diye vag jabe but bijor o houya lagbe
        odds.append(num)
print(odds)



players = ['sakib', 'riyad', 'mash']
ages = [ 35, 40, 44]

age_comb =[]
for player in players:
    print('player:', player)
    for age in ages:
        print(player, age)
        age_comb.append([player, age])
print(age_comb)