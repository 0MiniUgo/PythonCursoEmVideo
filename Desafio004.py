n1 = input('Digite algo: ')
print(type(n1))
print('Pode ser um numero: ', n1.isnumeric())
print('Pode ser uma letra: ', n1.isalpha() )
print('Pode ser um ASCII: ', n1.isascii())
print('Pode ser um digito: ', n1.isdigit())
print('Está em casa baixa: ', n1.islower())