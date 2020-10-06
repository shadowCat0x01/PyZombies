firstNumber = int(input('Insira um número: '))
secondNumber = int(input('Insira um número: '))
thirdNumber = int(input('Insira um número: '))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print(f'O maior número é: {firstNumber}')
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print(f'O maior número é: {secondNumber}')
else:
    print(f'O maior número é: {thirdNumber}')
