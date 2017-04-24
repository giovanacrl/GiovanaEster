import json
from random import randint

#função insperdex exibindo o nome do adversário organizadamente
def insperdex_bonito (insperdex):
    for i in range(len(insperdex)):
        print("O seu insperdex é:\n{0} : {1} poder = {2}, vida = {3}, defesa = {4}"
                  .format(i,insperdex[i]["nome"],insperdex[i]["poder"],insperdex[i]["vida"], insperdex[i]["defesa"]))
#função batalha 
def batalha (vida_jogador, poder_jogador, defesa_jogador,
             vida_oponente, poder_oponente, defesa_oponente,experiencia):
    
    while vida_jogador >0 and vida_oponente>0:
        fugir=int(input("Batalha em andamento...você deseja:\n 1-continuar\n2-fugir"))
        if fugir == 2:
            if poder_jogador > poder_oponente:
                print("Você não conseguiu fugir...")
            elif poder_jogador <= poder_oponente:
                print("empate")
                return 
        #função sorte         
        esferas=input("Escolha uma das esferas:\n Ouro\n Prata\n Bronze")
        esferas=esferas.lower()
            
        if esferas in ["ouro", "prata", "bronze"]:
            sorte = 5*randint(0,20)
        else:
            print("Nem escolher moeda voce sabe, toma azar!")
            sorte = -10
        print("Seu valor da sorte é {0}." .format(sorte))
            
                
        vida_oponente= vida_oponente - ( poder_jogador  - (defesa_oponente-sorte))
        if vida_oponente <0:
            vida_oponente = 0
        elif (experiencia % 2) == 0 :
            vida_oponente= vida_oponente - ( poder_jogador + experiencia  - (defesa_oponente-sorte))
        print("A vida do seu oponente é: {0}".format(vida_oponente))
        print("A sua vida é: {0}".format(vida_jogador))
        if vida_oponente>0:
            if (experiencia % 2) == 0 : 
                vida_jogador= (vida_jogador - (poder_oponente - (defesa_jogador + experiencia)))+ sorte + experiencia
                print("SEU INSPERMON EVOLUIU,PARABÉNS!!! VOCÊ ACABA DE GANHAR {0} PONTOS DE EXPERIÊNCIA!".format(experiencia))
            else:
                vida_jogador= (vida_jogador - (poder_oponente - defesa_jogador))+ sorte
                
        
        
        experiencia= experiencia + 1 
        if vida_oponente <= 0:
            return "ganhou"
        elif vida_jogador<=0:
            return "perdeu"



# Le a lista de tipos de Inspermon.
with open('inspermons.json') as arquivo:
     inspermons = json.load(arquivo)
     
# Le o arquivo Insperdex de outras batalhas (salvando o jogo)
try:
    with open ('insperdex.json') as arquivo:
        insperdex= json.load(arquivo)
except Exception as inst:
    print("Você ainda não batalhou para ter adversários!")
    insperdex = []
    
experiencia=1
while True:
    #Todas as opções para o jogador escolher
    opcoes = int(input("Escolha uma das opções:\n 1-Dormir\n 2-Passear\n 3-Exibir Inspèrdex"))
    if opcoes==1:
        print("zZzZzZzZzZz")
        break
    elif opcoes == 3:
        insperdex_bonito(insperdex)
    elif opcoes == 2:
        print("Escolha um Inspermon para voce:")
        for i in range(len(inspermons)):
            print("{0} : {1} poder = {2}, vida = {3}, defesa = {4}"
                  .format(i,
                          inspermons[i]["nome"],
                          inspermons[i]["poder"],
                          inspermons[i]["vida"], 
                          inspermons[i]["defesa"]))
        escolha = int(input("Qual a sua escolha?"))
        
        #Gerando um adversário aleatório
        i = randint(0,28)
        
        #Adicionando o adverário na lista insperdex
        if inspermons[i] not in insperdex:
            insperdex.append(inspermons[i])
            
        #Mostrando os atributos do adversário    
        print("O seu adversário será: \n{0}".format(inspermons[i]["nome"]))
        print("poder = {0}".format(inspermons[i]["poder"]))
        print("vida = {0}".format(inspermons[i]["vida"]))
        print("defesa = {0}\n".format(inspermons[i]["defesa"]))

        #Atribuindo os valores para executar a função batalha
        print("Travada a batalha!")
        vida_jogador= inspermons[escolha]["vida"]
        poder_jogador= inspermons[escolha]["poder"]
        defesa_jogador= inspermons[escolha]["defesa"]

        vida_oponente= inspermons[i]["vida"]
        poder_oponente= inspermons[i]["poder"]
        defesa_oponente= inspermons[i]["defesa"]

        #Chamando a função batalha
        resultado = batalha (vida_jogador, poder_jogador, defesa_jogador,
             vida_oponente, poder_oponente, defesa_oponente,experiencia)
            
        #estamos considerando como experiencia o fato de que o inspermon ganhou a batalha e assim é acrescentado 1 ao poder.
        if resultado == "ganhou":
            print("Você ganhou!")
            inspermons[escolha]["poder"]+= 1
            
        elif resultado == "perdeu":
            print("Você perdeu!")
    
    # Cria um arquivo para salvar as informações.
    with open('inspermons.json','w') as arquivo:
        json.dump(inspermons, arquivo)
    with open('insperdex.json','w') as arquivo:
        json.dump(insperdex, arquivo)
    
