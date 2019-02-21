lista = ['maçã', 'banana', 'pêra', 'jaca', 'melância']
print(lista[1])

print('alterando o valor na lista')
lista[1] = 'uva'
print(lista[1])

print('\n\n')

print('percorre a lista e verifica se a fruta está nela')
for fruta in lista:
    if fruta in lista:
        print('A {} está na lista.'.format(fruta))

print('\n')

print('Existem {} itens na lista.'.format(len(lista)))

print('\n')

print('adicionar item na lista')
lista.append('laranja')
print(lista)

print('\n')

print('adiciona um item em uma posição específica')
lista.insert(2, 'cagaita')
print(lista)

print('\n')

print('remove o item expecificado')
lista.remove('cagaita')
print(lista)

print('\n')

print('remove o elemento com o indice indicado, se nenhum for indicado, o ultimo será removido')
lista.pop(0)
print(lista)

print('\n')

print(' a palavra chave DEL remove o elemento com o indice indicado')
del lista[2]
print(lista)

print('\n')

print('quantas vezes o item respecificado aparece')
qtd = lista.count('uva')
print(qtd)

print('\n')

print('que indice o item indicado possui')
onde = lista.index('melância')
print(onde)

print('\n')

print('Inverte a lista')
lista.reverse()
print(lista)

print('\n')

print('ordena a lista em ordem alfabética')
lista.sort()
print(lista)

print('\n')

print('esvazia a lista')
lista.clear()
print(lista)

