print("⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆")
print("⭒ ✿ Bem-vindo ao jogo do bicho ✿ ⭒")
print("⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆")

numeroSecreto = 7
totalDeTentativas = 3
rodada = 1


while(rodada <= totalDeTentativas):
    print("tentativa:", rodada, "de", totalDeTentativas)
    chute = int(input("Qual seu chute? "))
    if chute== numeroSecreto:
        print("uhul, parabéns vc acertou")
    else:
        if chute > numeroSecreto:
            print("oh no! seu chute foi acima do numero secreto")
        elif chute < numeroSecreto:
            print("ops, seu chute foi a baixo do numero secreto")
    rodada = rodada + 1  
print("fim do jogo!")

   

