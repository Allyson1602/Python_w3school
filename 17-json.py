import json

print('Convertido de json para pyton'.upper())

dados = '{"name": "Allyson", "age": 19, "city": "Brasília"}'
convert = json.loads(dados)
print(convert['name'])

print('\n')

print('Convertido de python para json'.upper())

dados2 = {
    'especie': 'macaco',
    'idade': 7,
    'local': 'São Paulo'
}
convert2 = json.dumps(dados2)
print(convert2)

print('\n')

print(json.dumps({"name": "Allyson", "age": 19, "city": "Brasília", "food": "massa"}, indent=3, separators=(". ", " = "), sort_keys=True))
print(json.dumps({"name": "Allyson", "age": 19, "city": "Brasília", "food": "massa"}))

print('\n')

print(json.dumps(["apple", "banana"]))
print(json.dumps("Hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print('\n')
