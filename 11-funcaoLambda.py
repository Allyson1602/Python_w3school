frutas = lambda maca: maca + 10
print(frutas(5))

print('\n')

calculo = lambda num1, num2: num1*num2
print(calculo(5, 4))

print('\n')

soma = lambda num1, num2, num3: num1+num2+num3
print(soma(3, 6, 0))

print('\n')


def my_funcao(n):
    return lambda a: a*n


resu = my_funcao(4)
print(resu(7))

print('\n')


def my_func(m):
    return lambda b: b*m


dobro = my_func(2)
triplo = my_func(3)

print('O dobro é {}.\n'.format(dobro(7)))
print('O triplo é de {}.'.format(triplo(7)))

print('\n')


