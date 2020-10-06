a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if a > b + c or b > a + c or c > a + b:
        print('Isso não pode ser um triangulo')
        print('Um dos lados é maior que a soma')
elif a == b == c:
        print('Equilatero')
elif a == b or b == c or a == c:
        print('Isósceles')
