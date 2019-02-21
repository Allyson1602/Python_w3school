a = 33
b = 200

if a < b:
    print('{} é menor que {}.'.format(a, b))

print('\n')

c = 44
d = 44

if c > d:
    print('{} é maior que {}.'.format(c, d))
elif c == d:
    print('{} é igual a {}'.format(c, d))

print('\n')

e = 200
f = 33

if e < f:
    print('{} é maior que {}'.format(e, f))
elif e == f:
    print('{} é igual a {}'.format(e, f))
else:
    print('{} é menor que {}'.format(e, f))

print('\n')

if a < b: print('a é menor que b')

print('\n')

print('A') if a < b else print('b')

print('\n')

if a < b and a == f:
    print('{} é menor que {} e igual a {}.'.format(a, b, f))
