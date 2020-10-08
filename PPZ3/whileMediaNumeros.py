numero = 1
soma  = 0

while numero <= 10:
    x = int(input(f'{numero} número: '))
    soma = soma + x
    numero = numero + 1
print(f'Média: {soma/10:.1f}')