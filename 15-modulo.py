import modulo as mx

mx.parabens('pedro'.capitalize())

print('{} possui {} anos de idade e mora na {}.'.format(mx.cad['name'], mx.cad['age'], mx.cad['country']))

print('\n')

import platform

x = platform.system()
print(x)

y = dir(platform)
print(y)
