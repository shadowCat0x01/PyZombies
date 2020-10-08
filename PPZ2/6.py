ganhaHora = float(input('Quanto você ganha por hora: '))
horasTrabalha = int(input('Quantas horas você trabalha por mês: '))

salarioBruto = ganhaHora * horasTrabalha
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss - sindicato

print(f'+Salário bruto:\t R${salarioBruto:.2f}')
print(f'-IR:\t R${ir:.2f}')
print(f'-INSS:\t R${inss:.2f}')
print(f'-Sindicato:\t R${sindicato:.2f}')
print(f'+Salário líquido:\t R${salarioLiquido:.2f}')