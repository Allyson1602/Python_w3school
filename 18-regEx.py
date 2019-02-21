import re

texto = "O arco-íris é bastante colorido"


print("Verifica se começa com 'O' e termina com 'colorido'".upper())
veri1 = re.search("^O.*colorido$", texto)

if veri1:
    print('Requisitos constando.')
else:
    print('Requisitos não atendidos.')

print('\n')

print("Mostra todas as letra entre 'a' e 'm'".upper())
veri2 = re.findall('[a-m]', texto)
print(veri2)

print('\n')

texto2 = "Hoje é 2/5/2019"

print("Pega todos os números".upper())
veri3 = re.findall('\d', texto2)
print(veri3)

print('\n')

print('Procura pelo caracter que comece com \'a\', termine com \'s\' e entre os dois, possua 7 caracteres.'.upper())
veri4 = re.findall('a.......s', texto)
print(veri4)

print('\n')

print("Verifica se começa com a letre 'O'".upper())
veri5 = re.findall('^O', texto)
print(veri5)

print('\n')

print('Verifica se termina com \'colorido\''.upper())
veri6 = re.findall('colorido$', texto)
print(veri6)

print('\n')
