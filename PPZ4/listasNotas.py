notas = []
contador = 1

while contador <= 4:
    notas.append(float(input('Nota: ')))
    contador = contador + 1
soma = contador = 0

while contador < 3:
    soma = soma + notas[contador]
    contador = contador + 1
print(f'Média {notas} é {soma/4:.1f}')