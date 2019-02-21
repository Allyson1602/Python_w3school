file = open('demofile.txt', 'r')
print(file.read(5))

print('\n')

print(file.readline())
print(file.readline())

print('\n')

file2 = open('demofile.txt', 'r')
for linha in file2:
    print(linha)

print('\n')

file2 = open('demofile.txt', 'w')
file2.write('Woops! Eu deletei o conteudo!')
