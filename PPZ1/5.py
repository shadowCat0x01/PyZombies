s = float(input('Salário: '))
p = float(input('Desconto%: '))
desconto = s * p / 100
novo = s - desconto
print(f'Aumento: R$ {desconto: .2f}')
print(f'Novo salário: RS {novo: .22}')
