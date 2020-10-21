string = 'um tigre, dois tigres, três tigres'
print(string)
print(string.find('tigre'))
print(string.find('tigre', 4))
print(string.find('tigre', 16))
print(string.replace('tigre', 'gato'))
print(string)
string = string.replace('tigre', 'gato')
print(string)