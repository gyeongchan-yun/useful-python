a = ['1', '123', '12', '12345', '1234', '123456']
a.sort(key=lambda x: len(x))

print(a)
