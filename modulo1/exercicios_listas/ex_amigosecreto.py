# preciso de: 1. um sorteador de nome   2. vincular um nome sorteado a cada nome 3. nao pode repetir o nome
import random

#pedindo os nomes

participantes = []  #criou a lista de participantes

print ('Bem vindo ao cadastro de amigo secreto!')  
while True:  #um laço para adicionar quantos nomes o usuário quer
    nome = str(input('Digite o nome do participante (ou digite "fim" para terminar): ')) #pedindo os nomes
    if nome.lower() == 'fim': #caso o usuario digite fim, quebra o laço --- o Lower serve para deixar tudo minusculo, pra caso o usuario digite FIM ou Fim etc, o programa funcionaria igual, sem o lower, o programa só pararia se o usuario digitasse fim com todas as letras minusculas
        break
    if nome.strip(): #coloca cada nome que o usuario escrever na lista de participantes
        participantes.append(nome.strip()) #o strip serve para tirar quaisquer espaços em brancos que o usuario digitar
        print (f'nome {nome.strip()} foi adicionado') #diz qual nome foi adicionado
    else: 
        print ('esse nome não é valido')

print (f'nomes adicionados à lista de participantes: {participantes}')

# lógica do sorteio

if len(participantes) < 2: #verifica o minimo de participantes
    print ('O minimo de participantes é 2')
else:
    print ('Iniciando amigo secreto!!!')

doador = participantes
recebedor = participantes[:] #o [:] cria uma cópia da lista original

random.shuffle(recebedor) # embaralha a lista copiada

while doador[0] == recebedor[0]:
    random.shuffle(recebedor) #caso alguém pegue seu próprio nome (mesma posição nas listas) ele embaralha de novo

sorteioFinal = list(zip(doador, recebedor)) # coloca as listas juntas, para saber quem pegou tal nome

for doar, receber in sorteioFinal:
    print (f'O amigo secreto de {doar} é a/o {receber}!') 
