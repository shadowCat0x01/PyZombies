usuario = input('Insira seu usuário: ')
senha = input('Insira sua senha: ')

while usuario == senha:
    print('Erro! O usuario deve ser diferente da senha.')
    usuario = input('Insira seu usuário: ')
    senha = input('Insira sua senha: ')