def main():

    print("Bem vindo a floricultura!")
    nome_cliente = input("Digite o seu nome: ")
    codigo_cliente = int(input("Digite o seu código: "))

    #listagem dos produtos
    codigo_produtos = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
    estoque_produtos = [30, 20, 5, 50, 33, 12, 8, 2, 11, 10]
    nome_produto = ["Girassol", "Gardênia", "Amarilis", "Coroa de Frade", "Azevinho", 
                    "Orquídea", "Petúnia", "Margarida", "Lavanda", "Lírio"]
    vendas_totais = []

    controle_while = 0
    
    #bloco principal, capta a compra do cliente
    #encerra o programa
    if codigo_cliente == 0:
        print("Obrigado pela preferência " + nome_cliente + ", volte sempre!")

    #verifica o produto
    else:
        # Bloco while para repetição automática do programa
        while controle_while == 0:
            codigo_compra = int(input("Digite o cógido do produto que você quer comprar: "))
            index_produto = codigo_produtos.index(codigo_compra)
            if index_produto == codigo_produtos.index(codigo_compra):
                # print(index_produto) 
                print("Você escolheu a flor", nome_produto[index_produto])
            else:
                print("Produto não encontrado!")

            # Pergunta a quantidade do produto que o cliente quer e valida se tem no estoque
            quantidade_compra = int(input("Digite a quantidade do produto que você quer comprar: "))

            if quantidade_compra <= estoque_produtos[index_produto]:
                print("Temos estoque suficiente para sua compra :)")
                print("Processando pedido...")
                print("Pedido realizado!")
                estoque_produtos[index_produto] = estoque_produtos[index_produto] - quantidade_compra
                vendas_totais.append(quantidade_compra)

                # Continuação do programa
                continuar = input("Deseja continuar (digite sim ou não)? ")
                if continuar == 'sim':
                    controle_while = 0
                elif continuar == "não":
                    controle_while = 1
                else:
                    print("Comando inválido, fim da execução do programa!")

            else:
                print("Não temos essa quantidade de flores, tente um valor mais baixo!")

        print("Obrigado pela preferência " + nome_cliente + ", volte sempre!")

        for indice, codigo in enumerate(codigo_produtos):
            print("O código", codigo, "é a flor:", nome_produto[indice], 
                  "e temos", estoque_produtos[indice], "no estoque!")

        print("Nosso estoque final é:", estoque_produtos)
        print("Nossa venda diária foi de:", vendas_totais)

main()