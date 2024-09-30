# equation = bytes((207,155,244,198,5))
equation = b'\xcf\x9b\xf4\xc6\x05'
print(equation)
print(type(equation))
print(len(equation))

for b in equation:
    print(b, end=',')
print()
print(equation.decode('utf-8'))