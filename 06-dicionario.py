dicionario = {
    'filme': 'Os vingadores',
    'anime': 'Boku no hero',
    'desenho': 'bob esponja',
    'serie': 'Supernatural'
}
print(dicionario)
print(dicionario['anime'])
print(dicionario['serie'])
print(dicionario.get('desenho'))

print('\n')

print('alterar valor')
dicionario['serie'] = 'the 100'
print(dicionario['serie'])

print('\n')

print('mostra as chaves')
for programas in dicionario:
    print(programas)

print('\n')

print('mostra os valores das chaves')
for programas in dicionario.values():
    print(programas)

print('\n')

print('mostra as chaves e os valores')
for tipo, elemento in dicionario.items():
    print(tipo, elemento)

print('\n')

print('verifica se serie é uma chave')
if 'serie' in dicionario:
    print('O dicionario possui series')

print('\n')

print('qtd elementos')
qtd = len(dicionario)
print(qtd)

print('\n')

print('adicionar item')
dicionario['novela'] = 'Maria do bairro'
print(dicionario)

print('\n')

print('remove itens(o popitem() remove o ultimo)')
dicionario.pop('filme')
print(dicionario)

print('\n')

print('remove o item')
del dicionario['desenho']
print(dicionario)

print('\n')

print('esvazia o dicionario')
dicionario.clear()
print(dicionario)
