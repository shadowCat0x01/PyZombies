a = int(input('Insira um número: '))
b = int(input('Insira um número: '))
c = int(input('Insira um número: '))

if a > b and a > c:
    print(f'Maior: {a}')
elif b > a and b > c:
    print(f'Maior: {b}')
else:
    print(f'Maior: {c}')

if a < b and a < c:
    print(f'Menor: {a}')
elif b < a and b < c:
    print(f'Menor: {b}')
else:
    print(f'Menor: {c}')