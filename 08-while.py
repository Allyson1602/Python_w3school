cont = 1
while cont <= 10:
    print(cont)
    cont += 1

print('\n')

print('com break')
cont = 1
while cont <= 10:
    print(cont)
    if cont == 5:
        break
    cont += 1

print('\n')

cont = 0
print('com continue')
while cont < 10:
    cont += 1
    if cont == 5:
        continue
    if cont == 8:
        continue
    print(cont)
