print('Dados da primeira pessoa: ')
print('__'*10)
nomePessoa1 = input('Nome: ')
idadePessoa1 = int(input('Idade: '))
print('__'*10)
print('Dados da segunda pessoa: ')
nomePessoa2 = input('Nome: ')
idadePessoa2 = int(input('Idade: '))
print('__'*10)
mediaIdade = (idadePessoa1 + idadePessoa2) / 2

print(f'A média de {nomePessoa1} e {nomePessoa2} é de {mediaIdade} anos')
