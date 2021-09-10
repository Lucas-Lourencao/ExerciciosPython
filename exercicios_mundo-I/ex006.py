n = int(input('Digite um número: '))
print('O dobro de {} é igual a {}'.format(n, (n*2)))
print('O triplo de {} é igual a {}.\nA raiz quadrada de {} é igual a {:.2f}'.format(
    n, (n*3), n, (n**(1/2))))
print('{} elevado a 5 potencia é igual a {}.'.format(n, pow(n, (5))))
print('A raiz de quinta potência de {} é igual a {:.3f}.'.format(n, pow(n, (1/5))))
# Lembrar que o comando \n é para pular linha;
# Lembrar que o comando ':.2f' é para formatar o número de casas decimais após a vírgula, neste caso apenas 2 algarismos;
# Outro modo de fazer exponenciação é fazendo o comando pow, veja:
# pow(n,a) = n**a, no caso de raízes pow(n,(1/a)) = n**(1/a);
