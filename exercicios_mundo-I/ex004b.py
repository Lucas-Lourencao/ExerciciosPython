# Dissecando uma variável:
# Exercício para testar tipos primitivos e informações sobre o que for digitado.
a = input('Digite algo: ')
print(type(a))
print('O valor digitado só tem espaços?', a.isspace())
print('O valor digitado é número?', a.isnumeric())
print('O valor digitado é alfanumérico?', a.isalnum())
print('O valor digitado está em minúsculo?', a.islower())
print('O valor digitado está em maiúsculo', a.isupper())
print('O valor digitado está capitalizado?', a.istitle())
print('O valor digitado pertence ao código ascii?', a.isascii())
print('O valor digitado é imprimível?', a.isprintable())
print('O valor digitado é um dígito?', a.isdigit())
