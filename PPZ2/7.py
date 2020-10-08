areaPintada = int(input('Insira os metros quadrados da área a ser pintada: '))

if areaPintada % 54 == 0:
    latas = areaPintada / 54
else:
    latas = int(areaPintada / 54) + 1

valor = latas * 80
print(f'{latas} latas')
print(f'Total:\t R${valor:.2f}')