
print('**' * 20)
print('**' * 5 ,'Jogo de Advinha','**' * 5)
print('**' * 20)

numero_secreto = 42
chute = int (input('Qual eh o numero da sorte: '))
print('Voce digitou: ', chute)

if(numero_secreto == chute):
    print('Voce Acertou') 
#else: 
    #print('Voce Errou!')
elif ( chute > numero_secreto):
    print('Voce errou! O seu chute foi maior que o numero secreto')
elif(chute < numero_secreto):
        print('Voce errou! O seu chute foi menor que o numero secreto')

#Querendo dar mas oportunidade ao jogador, usaremos o comando WHILE
#Iremos repetir o codigo, fzendo um laco ou um loop, que deve repetir a instrucao dentro de bloco "WHILE " for verdade
numero_secreto = 42
total_de_tentativas = 3
#esta variavel indica numero de rodadas
#rodada = 1


#while (total_de_tentativas > 0):
    #Usar o comdando "FOR" para criar o LOOP
for rodada in range(1, total_de_tentativas + 1 ):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    
    chute = int(input('Digite o seu numero: '))
    print('Voce digitou: ', chute)
    
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('Voce Acertou')
        #Este comando para executaco do codigo, caso o usuario acerte
        break
    elif(maior):
        print('Voce errou! O seu chute foi maior que o numero secreto')
    elif(menor):
        print('Voce errou! O Seu chute foi menor que o numero secreto')

    #    rodada = rodada + 1
        total_de_tentativas = total_de_tentativas - 1

while(rodada <= total_de_tentativas):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute_str = input('Digite o seu numero: ')

print('Fim de Jogo')
    




