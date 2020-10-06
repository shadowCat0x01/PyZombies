user = float(input('Informe a quantidade percorrida com o veículo em KM: '))
dias = int(input('Informe a quantidade de dias que o Sr(a). utilizou o veiculo: '))

total = 60*dias + 0.15*user

print(f'O preço a ser pago é de: R${total: .2f}')
