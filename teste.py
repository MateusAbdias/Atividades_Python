def adivinhar_numero():
    menor = 0
    maior = 100
    resposta = 0
    
    print("Pense em um número entre 0 e 100. Vou tentar adivinhar qual é!")
    print("Pensou?")
    print("Iniciando em...")
    print("3...")
    print("2...")
    print("1...")
    print("Responda 'sim' e 'não'.")
    
    while resposta != 'c':
        palpite = (menor + maior) // 2
        resposta = input(f"O número que você pensou é {palpite}? (sim/não/c): ").lower()
        
        if resposta == 'sim':
            print("Eu adivinhei o número!")
            break
        elif resposta == 'não':
            resposta = input("O número que você pensou é maior ou menor? (maior/menor): ").lower()
            
            if resposta == 'maior':
                menor = palpite + 1
            elif resposta == 'menor':
                maior = palpite - 1
            else:
                print("Desculpe, não entendi sua resposta. Por favor, responda novamente.")
        else:
            print("Desculpe, não entendi sua resposta. Por favor, responda novamente.")

adivinhar_numero()
