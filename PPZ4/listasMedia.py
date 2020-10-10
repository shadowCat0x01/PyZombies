notas = [6, 7, 8, 9, 10]
soma = 0
contador = 0

while contador < len(notas):
    soma = soma + notas[contador]
    contador = contador + 1

print(soma)
print(soma/len(notas))