dia = int(input('Dias: '))
hora = int(input('Horas: '))
minuto = int(input('Minutos: '))
segundo = int(input('Segundos: '))

total = dia*24*60*60 + hora*60*60 + minuto*60 + segundo
print(total)
