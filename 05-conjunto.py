print('Os valores serão apresentados aleatoriamente \n'.upper())

conjunto = {'lasanha', 'pizza', 'batata frita', 'refrigerante', 'salgadinho'}
print(conjunto)

print('\n')

for comida in conjunto:
    print(comida)

print('\n')

print('verifica se banana está no conjunto')
print('banana' in conjunto)

print('\n')

print('adiciona um item no conjunto')
conjunto.add('frango assado')
print(conjunto)

print('\n')

print('adiciona mais de um item no conjunto')
conjunto.update(['arroz e feijão', 'hamburguer', 'bolinho'])
print(conjunto)

print('\n')

print('comprimento do conjunto')
qtd = len(conjunto)
print(qtd)

print('\n')

print('remove um item(se não existir, terá um erro.')
conjunto.remove('arroz e feijão')
print(conjunto)

print('\n')

print('remove um item(se não existir, terá um erro.')
conjunto.discard('frango assado')
print(conjunto)

print('\n')

print('esvazia o conjunto')
conjunto.clear()
print(conjunto)

print('\n')

print('irá apagar o conjunto inteiro')
del conjunto
