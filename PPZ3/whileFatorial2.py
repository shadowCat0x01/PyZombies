numero = int(input('Insira um número: '))

contador = 1
fatorial = 1
while contador <= numero:
    fatorial = fatorial * contador
    contador = contador + 1
print(f'fatorial({numero}) = {fatorial}')