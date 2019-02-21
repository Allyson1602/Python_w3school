print('\n')


def primeira():
    print('Minha primeira função!')


primeira()

print('\n')


def segunda(nome='Pedro'):
    print('Bem vindo, {}'.format(nome))


segunda()
segunda('Allyson')
segunda('Bruno')

print('\n')


def calculo(pri=1, seg=2):
    return pri + seg


print(calculo())
print(calculo(5, 2))
print(calculo(3, 7))

print('\n')


def recursao(k):
    if k > 0:
        resultado = k + recursao(k-1)
        print(resultado)
    else:
        resultado = 0
    return resultado


print(recursao(6))

print('\n')

