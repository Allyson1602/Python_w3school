mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print('\n')

mystr = 'banana'
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print('\n')


class Numbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        x = self.num
        self.num += 1
        return x


myclass = Numbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('\n')


class Number2:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 20:
            y = self.num
            self.num += 1
            return y
        else:
            raise StopIteration


myclass = Number2()
myiter = iter(myclass)

for y in myiter:
    print(y)
