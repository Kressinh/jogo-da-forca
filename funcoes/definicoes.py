import time
def verificaNome(desafiante,competidor):
    if desafiante == "" or competidor ==  "":
        return False
    elif desafiante == " " or competidor ==  " ":
        return False

def verificaChave(dica1,dica2,dica3,chave):
    if dica1 == "" or dica2 ==  "" or dica3 == "":
        return False
    elif dica1 == " " or dica2 ==  " " or dica3 == " ":
        return False
    elif chave == "":
        return False

def vencedor(desafiante,competidor,numero_de_erros):
    if numero_de_erros == 5:

        print("               Você Perdeu!")
        print(">>>>>", desafiante, "é o vencedor!")
        print(">>>>> Mais sorte na próxima ", competidor,".")
        return False
    else:

        print("               Você Venceu!")
        print(">>>>>", competidor, "é o vencedor.")
        print(">>>>> Mais sorte na proxima ", desafiante,".")
        return True

def verificaDicaeLetra(dica1,udica1,dica2,udica2,dica3,udica3,contaDica):
    if contaDica == 0:
        
        print("               Primeira dica:")
        print("Primeira dica: ", dica1)
        udica1 = True
        letra = input("Qual é o seu palpite de letra? ")
        if len(letra) > 1 :
            print("Resposta inválida")
            udica1 = False
            return False
        else:
            return letra

    elif contaDica == 1:

        print("               Segunda dica:")
        print("Primeira dica: ", dica1)
        print("Segunda dica: ", dica2)
        udica2 = True
        letra = input("Qual é o seu palpite de letra? ")
        if len(letra) > 1 :
            print("Resposta invalida")
            udica2 = False
            return False
        else:
            return letra

    elif contaDica == 2:

        print("               Terceira dica:")
        print("Primeira dica: ", dica1)
        print("Segunda dica: ", dica2)
        print("Terceira dica: ", dica3)
        udica3 = True
        print("                 Não há mais dicas")
        letra = input("Qual é o seu palpite de letra? ")
        if len(letra) > 1 :
            print("Resposta inválida")
            return False
        else:
            return letra
    else:
        letra = input("Qual é o seu palpite de letra? ")
        if len(letra) > 1 :
            print("Resposta inválida")
            return False
        else:
            return letra

        
def confere(palavra_chave,letra,lista_a_mostrar, numero_de_letras,numero_de_erros):
    contador2 = -1
    erro = True
    while True:

        if contador2 == numero_de_letras-1:

            break
        else:

            contador2 = contador2 + 1
            for i in palavra_chave:

                if letra in palavra_chave:
                    
                    if palavra_chave[contador2] == letra:
                        lista_a_mostrar[contador2] = letra
                        erro = False
                       
    if erro == False:
        print("               Certo")
    else:
        numero_de_erros = numero_de_erros + 1
        if numero_de_erros == 1:
            print("Você já errou 1 vez.")
        elif numero_de_erros > 1:
            print("Você já errou ", numero_de_erros," vezes.")
        time.sleep(1)
    return numero_de_erros
    
def arquivar(desafiante,competidor,vencedor,resposta):
    arquivo = open("registro_de_partidas.txt", "a")
    arquivo.write('----------------------------------------------\n')
    arquivo.write("Desafiante: ")
    arquivo.write(desafiante)
    arquivo.write(".\n")
    arquivo.write("Competidor: ")
    arquivo.write(competidor)
    arquivo.write(".\n")
    arquivo.write("O vencedor foi ")
    arquivo.write(vencedor)
    arquivo.write(".\n")
    arquivo.write("Palavra: ")
    arquivo.write(resposta)
    arquivo.write(".\n")

def mostrarPartida():
    arquivo = open("registro_de_partidas.txt", "r")
    conteudo = arquivo.read()
    return conteudo