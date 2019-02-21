# TUPLAS SÃO IMUTÁVEIS

tupla = ('estojo', 'caderno', 'borracha', 'lápis', 'caderno')
print(tupla[2])

print('\n')

for objeto in tupla:
    print(objeto)

if 'régua' not in tupla:
    print('Não possui {}.'.format('régua'))

print('\n')

print('Quantidade de elementos na tupla')
qtd = len(tupla)
print(qtd)

print('\n')

print('retorna a quantidade de vezes que o caderno aparece')
qtd = tupla.count('caderno')
print(qtd)

print('\n')

print('procura a primeira ocorrencia do item indicado')
ocorrencia = tupla.index('lápis')
print(ocorrencia)
