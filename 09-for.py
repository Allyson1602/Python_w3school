frutas = ['maçã', 'banana', 'morango', 'goiaba']
verduras = ['pepino', 'chuchu', 'espinafre']

for fruta in frutas:
    print(fruta)

print('\n')

print('mostra os caracteres da palavra \'banana\'')
for string in 'banana':
    print(string)

print('\n')

print('para se encontrar a string \'morango\'')
for fruta in frutas:
    if fruta == 'morango':
        break
    print(fruta)

print('\n')

print('pula a string \'banana\'')
for fruta in frutas:
    if fruta == 'banana':
        continue
    print(fruta)

print('\n')

print('looping de 2 até 10')
for x in range(2, 11):
    print(x)

print('\n')

print('looping de 2 até 10 pulando de 2 em 2')
for y in range(2, 11, 2):
    print(y)

print('\n')

print('ao fim do range, é gerada uma mensagem')
for contagem in range(1, 11, 3):
    print(contagem)
else:
    print('Contagem terminada')

print('\n')

for fruta in frutas:
    for verdura in verduras:
        print(fruta, verdura)
