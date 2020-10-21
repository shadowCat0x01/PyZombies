'''Faça um programa que leia uma palavra
e troque as vogais por "*"
'''

palavra = input('Palavra: ')
k = 0
troca = ''

while k < len(palavra):
    if palavra[k] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[k]
    k = k + 1
print(troca)