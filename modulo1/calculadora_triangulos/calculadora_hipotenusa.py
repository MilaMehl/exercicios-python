import math

print('Bem vindo! Este programa calcula a hipotenusa de um triangulo retangulo.\nPara descobrir a hipotenusa, eu preciso do cateto oposto e do cateto adjacente.')
CtOposto = float(input('Primeiro, me diga o cateto oposto: '))
CtAdjacente = float(input('e agora, o cateto adjacente: '))

#calculo 

conta = math.hypot(CtOposto, CtAdjacente)

#usando a fórmula: conta = math.sqrt( CtOposto ** 2 + CtAdjacente ** 2 )

print(f'A hipotenusa é {conta}')