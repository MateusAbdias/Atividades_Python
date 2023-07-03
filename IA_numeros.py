print("Pense em um número entre 0 a 100")
print("Pensou?")
print("Iniciando em...")
print("3...")
print("2...")
print("1...")

contador = 0
minimo = 0
maximo = 100

while contador==0:
    palpite = (maximo + minimo) / 2
    print("O número que você pensou é maior ou igual a", palpite, "?")
    resposta = input("Digite sim ou não: ")
    if resposta == "pare":
        break

    elif resposta == "sim":
        resposta_2 = input("Ele é", maximo, "?")
        if resposta_2 == "sim":
            print("Acertei o seu número!!!")
            
        elif resposta_2 == "não":
            resposta_3 = input("Ele é maior ou menor?")
            if resposta_3 == "maior":
                minimo = palpite + 1
            elif resposta_3 == "menor":
                maximo == palpite - 1
            else:
                print("Desculpe, não entendi sua resposta. Por favor, responda novamente.")
        else:
            print("Desculpe, não entendi sua resposta. Por favor, responda novamente.")

        print
        break
