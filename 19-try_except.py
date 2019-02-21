try:
    print(teste)
except:
    print('Em caso de erro, mostre isso')

print('\n')

try:
    print(teste)
except NameError:
    print('Variável teste não foi definida')
except:
    print('Alguma coisa está errada')

print('\n')

try:
    print('hello')
except:
    print('Alguma coisa deu errado')
else:
    print('nada de errado')

print('\n')

try:
    print(teste)
except:
    print('alguma coisa deu errado')
finally:
    print('the \'try except\' foi finalizado')
