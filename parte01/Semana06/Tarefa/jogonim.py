def main():
    opcao = 0
    while opcao < 1 or opcao > 2:
        opcao = int(input("Bem-vindo ao jogo do NIM! Escolha:\n\n"
        "1 - para jogar uma partida isolada\n"
        "2 - para jogar um campeonato\n"))

    if opcao == 1: 
        print("\nVocê escolheu uma partida!\n")
        partida()

    else: 
        print("\nVoce escolheu um campeonato!\n")
        campeonato()        

def partida():
    totalDePecas = 0
    limitePecasporJogada = 0
    pecasTiradas = 0
    
    while totalDePecas < 1: 
        totalDePecas = int(input("Quantas peças? "))
        
    while limitePecasporJogada < 1:
        limitePecasporJogada = int(input("Limite de peças por jogada? "))

    if totalDePecas % (limitePecasporJogada+1) == 0:
        print("\nVoce começa!")
        primeiro = "usuario"
        pecasTiradas = usuario_escolhe_jogada(totalDePecas, limitePecasporJogada)
        totalDePecas -= pecasTiradas
        if totalDePecas == 0:
            print("Fim do jogo! Você ganhou!\n")
            return

    else:
        print("\nComputador começa!")
        primeiro = "computador"
        pecasTiradas = computador_escolhe_jogada(totalDePecas, limitePecasporJogada)
        totalDePecas -= pecasTiradas
        if totalDePecas == 0:
            print("Fim do jogo! O computador ganhou!\n")
            return

    while totalDePecas >= 0:       
        if primeiro == "usuario":
            pecasTiradas = computador_escolhe_jogada(totalDePecas, limitePecasporJogada)
            totalDePecas -= pecasTiradas
            if totalDePecas == 0: 
                print("Fim do jogo! O computador ganhou!\n")
                return 
            pecasTiradas = usuario_escolhe_jogada(totalDePecas, limitePecasporJogada)
            totalDePecas -= pecasTiradas
            if totalDePecas == 0: 
                print("Fim do jogo! Você ganhou!\n")
        else: 
            pecasTiradas = usuario_escolhe_jogada(totalDePecas, limitePecasporJogada)
            totalDePecas -= pecasTiradas
            if totalDePecas == 0: 
                print("Fim do jogo! Você ganhou!\n")
                return     
            pecasTiradas = computador_escolhe_jogada(totalDePecas, limitePecasporJogada)
            totalDePecas -= pecasTiradas
            if totalDePecas == 0: 
                print("Fim do jogo! O computador ganhou!\n")
                return
                

    
def usuario_escolhe_jogada(n,m):
    pecasTiradas = int(input("Quantas peças você vai tirar? "))
    
    while pecasTiradas > m or pecasTiradas < 1 or pecasTiradas > n:
        print("\nOops! Jogada inválida! Tente de novo.\n")
        pecasTiradas = int(input("Quantas peças você vai tirar? "))
    
    print("Você tirou uma peça." if pecasTiradas == 1 else f"Você tirou {pecasTiradas} peças.")
    
    if n - pecasTiradas > 0:
            print("Agora resta apenas uma peça no tabuleiro\n" if n-pecasTiradas == 1 else f"Agora restam {n-pecasTiradas} peças no tabuleiro.\n")    
    
    return pecasTiradas
    
def computador_escolhe_jogada(n,m):
    totalDePecas = n
    pecasTiradas = m

    while pecasTiradas > 0 :
        if (totalDePecas - pecasTiradas) % (m+1)  == 0:
            print("O computador tirou uma peça." if pecasTiradas == 1 else f"O computador tirou {pecasTiradas} peças.")
            if totalDePecas - pecasTiradas > 0:
                print("Agora resta apenas uma peça no tabuleiro\n" if totalDePecas == 1 else f"Agora restam {totalDePecas-pecasTiradas} peças no tabuleiro.\n")            

            return pecasTiradas

        elif pecasTiradas != 0: 
            pecasTiradas -= 1

    pecasTiradas = m
    if totalDePecas - pecasTiradas > 0:
        print("Agora resta apenas uma peça no tabuleiro\n" if totalDePecas == 1 else f"Agora restam {totalDePecas-pecasTiradas} peças no tabuleiro.\n")            
    return pecasTiradas

    
def campeonato():
    print("**** Rodada 1 ****\n")
    partida()
    print("**** Rodada 2 ****\n")
    partida()
    print("**** Rodada 3 ****\n")
    partida()
    print("**** Final do campeonato! ****\n")
    print("Placar: Você 0 X 3 Computador")

main()

# usuario_escolhe_jogada(3,5)