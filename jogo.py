from funcoes.definicoes import verificanome, verificachave, verificadicaeletra, confere, vencedor, arquivar, mostrapartidas
from funcoes.tela import limpatela
import sys
import time

while True:

    limpatela()
    print("              Jogo da forca!")
    print(" Para confirmar lembre-se de precionar 'ENTER'.")
    print(" Não é permitido deixar em branco nenhum dos formulários e nem usar números.")
    print(" A não ser que o número faça parte do nome ou da palavra chave ou das dicas.")
    print("")
    while True:
        desafiante = input("Informe o desafiante: ")
        competidor = input("Informe o competidor: ")
        try:
            desafiante = int(desafiante)
            competidor = int(competidor)
            limpatela()
            print("Você preencheu algo incorretamente.")
        except:
            aceitanome = verificanome(desafiante, competidor)
            if aceitanome == False:
                limpatela()
                print("Você preencheu algo incorretamente.")
            else:
                break

    limpatela()
    print("       Para o desafiante apenas")

    while True:
        chave = input("Insira a palavra chave: ")
        dica1 = input("Insira a primeira dica: ")
        dica2 = input("Insira a segunda dica: ")
        dica3 = input("Insira a terceira dica: ")
        try:
            dica1 = int(dica1)
            dica2 = int(dica2)
            dica3 = int(dica3)
            limpatela()
            print("Você preencheu algo incorretamente.")
        except:
            aceitachave = verificachave(dica1, dica2, dica3, chave)
            if aceitachave == False:
                limpatela()
                print("Você preencheu algo incorretamente.")
            else:
                break

    limpatela()
    numeroletras = 0
    for i in chave:
        numeroletras = numeroletras + 1

    mostrar = []
    contador = 0

    while contador != numeroletras:
        mostrar.append(' _ ')
        contador = contador+1

    print("Número de letras da palavra : ",numeroletras)
    print(" _ "*numeroletras)

    udica1 = False
    udica2 = False
    udica3 = False
    escolha = ""
    contadica = 0
    Nerros = 0

    while True:

        if Nerros == 5 or ' _ ' not in mostrar:
            if Nerros == 5:

                print("               VOCÊ PERDEU")
                print(">>>>>", desafiante, "é o vencedor.")
                print(">>>>> Mais sorte na proxima ", competidor,".")
                vencedor = desafiante
            else:

                print("               VOCÊ VENCEU")
                print(">>>>>", competidor, "é o vencedor.")
                print(">>>>> Mais sorte na proxima ", desafiante,".")
                vencedor = competidor
            time.sleep(3)
            limpatela()
            break
        elif contadica > 2:
            
            limpatela()
            print("Primeira dica: ", dica1)
            print("Segunda dica: ", dica2)
            print("Terceira dica: ", dica3)
            print(' '.join(mostrar))
            letra = verificadicaeletra(dica1,udica1,dica2,udica2,dica3,udica3,contadica)
            if len(letra) == False:
                print("Resposta invalida.")
            else:
                Nerros = confere(chave,letra,mostrar,numeroletras,Nerros)
                print(' '.join(mostrar))
                print('----------------------------------------------')
        else:
        
            escolha = input("Precione 0 para Jogar ou 1 para Solicitar dica: ")
            print('----------------------------------------------')
            if escolha == "0":
                limpatela()
                print(' '.join(mostrar))
                letra = input("Qual o seu palpite de letra? ")
                if len(letra) == False:
                    print("Resposta invalida.")
                else:
                    Nerros = confere(chave,letra,mostrar,numeroletras,Nerros)
                    print(' '.join(mostrar))
                    print('----------------------------------------------')

            elif escolha == "1":
                limpatela()
                print(' '.join(mostrar))
                letra = verificadicaeletra(dica1,udica1,dica2,udica2,dica3,udica3,contadica)
                if letra != False:
                    contadica = contadica + 1
                    Nerros = confere(chave,letra,mostrar,numeroletras,Nerros)
                    print(' '.join(mostrar))
                    print('----------------------------------------------')

            else:

                print("               Valor invalido.")
                print(' '.join(mostrar))
                print('----------------------------------------------')
    if vencedor == desafiante or vencedor == competidor:

        arquivar(desafiante,competidor,vencedor,chave)
        limpatela()
        print("               HISTÓRICO DE PARTIDAS")
        mostrarlog = mostrapartidas()
        print(mostrarlog)
        print("Você quer jogar novamente?")
        print("(1)Sim (0)Não")
        jogar = input()
        if jogar == "0":
            limpatela()
            sys.exit(0)