#Helen Kressin RA 1131995

from funcoes.definicoes import verificaNome, verificaChave, verificaDicaeLetra, confere, vencedor, arquivar,mostrarPartida
from funcoes.tela import limpaTela
import sys
import time

while True:

    limpaTela()
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
            limpaTela()
            print("Você preencheu algo incorretamente.")
        except:
            aceitaNome = verificaNome(desafiante, competidor)
            if aceitaNome == False:
                limpaTela()
                print("Você preencheu algo incorretamente.")
            else:
                break

    limpaTela()
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
            limpaTela()
            print("Você preencheu algo incorretamente.")
        except:
            aceitaChave= verificaChave(dica1, dica2, dica3, chave)
            if aceitaChave== False:
                limpaTela()
                print("Você preencheu algo incorretamente.")
            else:
                break

    limpaTela()
    numeroLetras = 0
    for i in chave:
        numeroLetras = numeroLetras + 1

    mostrar = []
    contador = 0

    while contador != numeroLetras:
        mostrar.append(' _ ')
        contador = contador+1

    print("Número de letras da palavra : ",numeroLetras)
    print(" _ "*numeroLetras)

    udica1 = False
    udica2 = False
    udica3 = False
    escolha = ""
    contaDica= 0
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
            limpaTela()
            break
            elifcontaDica> 2
            
            limpaTela()
            print("Primeira dica: ", dica1)
            print("Segunda dica: ", dica2)
            print("Terceira dica: ", dica3)
            print(' '.join(mostrar))
            letra = verificaDicaeLetra(dica1,udica1,dica2,udica2,dica3,udica3,contaDica)
            if len(letra) == False:
                print("Resposta invalida.")
            else:
                Nerros = confere(chave,letra,mostrar,numeroLetras,Nerros)
                print(' '.join(mostrar))
                print('----------------------------------------------')
        else:
        
            escolha = input("Precione 0 para Jogar ou 1 para Solicitar dica: ")
            print('----------------------------------------------')
            if escolha == "0":
                limpaTela()
                print(' '.join(mostrar))
                letra = input("Qual o seu palpite de letra? ")
                if len(letra) == False:
                    print("Resposta invalida.")
                else:
                    Nerros = confere(chave,letra,mostrar,numeroLetras,Nerros)
                    print(' '.join(mostrar))
                    print('----------------------------------------------')

            elif escolha == "1":
                limpaTela()
                print(' '.join(mostrar))
                letra = verificaDicaeLetra(dica1,udica1,dica2,udica2,dica3,udica3,contaDica)
                if letra != False:
                   contaDica=contaDica+ 1
                Nerros = confere(chave,letra,mostrar,numeroLetras,Nerros)
                print(' '.join(mostrar))
                print('----------------------------------------------')

            else:

                print("               Valor invalido.")
                print(' '.join(mostrar))
                print('----------------------------------------------')
    if vencedor == desafiante or vencedor == competidor:

        arquivar(desafiante,competidor,vencedor,chave)
        limpaTela()
        print("               HISTÓRICO DE PARTIDAS")
        mostrarlog =mostrarPartida()
        print(mostrarlog)
        print("Você quer jogar novamente?")
        print("(1)Sim (0)Não")
        jogar = input()
        if jogar == "0":
            limpaTela()
            sys.exit(0)