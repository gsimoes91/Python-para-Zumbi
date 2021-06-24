'Exercício 11 - Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão'
digitos = len(str(2 ** 1000000))

print(f'2 elevado a 1 milhão tem {digitos} digitos')