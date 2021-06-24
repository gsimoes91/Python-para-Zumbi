'Exercício 4 - Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário'
salario = float(input('Digite o salário em R$: '))
aumento = float(input('Digite o percentual do aumento: '))

aumento = salario * (aumento / 100)
novosalario = salario + aumento

print(f'Aumento: R$ {aumento:.2f}', f'Novo salario: R$ {novosalario:.2f}')