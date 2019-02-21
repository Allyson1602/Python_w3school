import datetime

data = datetime.datetime.now()

print(data.year)
print(data.strftime("%A"))

data2 = datetime.datetime(2020, 5, 17)
print(data2.strftime('%p'))
print(data2.strftime('%w'))
print(data2.strftime('%A'))
