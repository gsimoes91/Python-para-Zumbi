'Exercício 6 - Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem'
d = float(input('Digite a distância em km: '))
vm = float(input('A velocidade média em km/h esperada é de: '))

tempo = d / vm

print(f'O tempo da viagem será de: {tempo:.1f} horas')