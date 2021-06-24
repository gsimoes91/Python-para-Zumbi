'Exercício 3 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos'
dias = 5
horas = 17
minutos = 45
segundos = 32

total = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos

print (f'{dias} dias, 'f'{horas} horas, 'f'{minutos} minutos',f'e {segundos} segundos tem:',f'{total} segundos')