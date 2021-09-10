n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
s = n1 + n2
# print(s) A soma pode ser demonstrada desse modo ou
#print('A soma entre', n1, 'e', n2, 'é igual a', s,'!')
# ou da forma mais atual que é utilizando o .format

print('O valor da soma de {} e {} é igual a {}!'.format(n1, n2, s))
