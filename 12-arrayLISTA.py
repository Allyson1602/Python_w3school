cars = ['ford', 'volvo', 'bmw']

cars[1] = 'toyota'
print(cars[1])

print('\n')

print(len(cars))

print('\n')

for car in cars:
    print(car)


print('\n')

cars.append('honda')
print(cars)

print('\n')

cars.pop(2)
print(cars)
