import math

print('Bem vindo! Este programa calcula a hipotenusa de um triangulo retangulo.\nPara descobrir a hipotenusa, eu preciso do cateto oposto e do cateto adjacente, que você sabe quais são.')
CtOposto = int(input('Primeiro, me diga o cateto oposto: '))
CtAdjacente = int(input('e agora, o cateto adjacente: '))

#calculo 

conta = math.sqrt( CtOposto ** 2 + CtAdjacente ** 2 )

print(f'A hipotenusa é {int(conta)}')