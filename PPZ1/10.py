cigarros = int(input('Informe quantos cigarros por dia são fumados: '))
anos = int(input('Informe a quantos anos fuma-se: '))

total_cigarros = anos * 365 * cigarros
dias = total_cigarros / 144

print(f'Você perdeu {dias: .1f} dias de vida')
