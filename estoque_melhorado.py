def main():
    # listagem dos produtos
    produtos = [(101, "Girassol", "teste"),
                (102, "Gardênia", "teste"),
                (103, "Amarilis", "teste"),
                (104, "Coroa de Frade", "teste"),
                (105, "Azevinho", "teste"),
                (106, "Orquídea", "teste"),
                (107, "Petúnia", "teste"),
                (108, "Margarida", "teste"),
                (109, "Lavanda", "teste"),
                (110, "Lírio", "teste")]
    estoque_produtos = [1, 20, 5, 10, 33, 12, 3, 2, 11, 2]
    lista_clientes = []
    vendas_totais = []

    print("Bem vindo à floricultura!")

    # Compreensão de lista que lê o estoque dos produtos e guarda os que estão abaixo de 3
    repor_produtos = [produto for produto in estoque_produtos if produto < 3]
    # Imprime os produtos que estão abaixo de 3 no estoque
    if repor_produtos:
        print("Alerta: Os seguintes produtos estão com baixa quantidade no estoque:")
        for produto in repor_produtos:
            posicao = estoque_produtos.index(produto)
            print(f"Código: {produtos[posicao][0]} | Produto: {produtos[posicao][1]} | Estoque: {estoque_produtos[posicao]}")
    else:
        print("Todos os produtos estão com quantidade adequada no estoque.")

    print("_______________________________________________________________________")

    nome_cliente = input("Digite o nome do cliente: ")
    codigo_cliente = int(input("Digite o código do cliente: "))

    # bloco principal, capta a compra do cliente
    if codigo_cliente == 0: # encerra o programa
        print("Obrigado pela preferência " + nome_cliente + ", volte sempre!")
    else:
        # Bloco while para repetição do programa
        continua_programa = 'sim'  # Inicializa a variável
        while continua_programa == 'sim':
            codigo_compra = int(input("Digite o código do produto que você quer comprar: "))
            produto_encontrado = False  # Variável de controle para verificar se o produto foi encontrado
            for produto in produtos:
                if produto[0] == codigo_compra:
                    produto_encontrado = True
                    break

            # Continuação do programa
            if produto_encontrado:
                print("Você escolheu a flor:", produto[1])

                # Pergunta a quantidade do produto que o cliente quer
                quantidade_compra = int(input("Digite a quantidade do produto que você quer comprar: "))
                index_produto = produtos.index(produto)
                # valida se tem no estoque e processa a compra
                if estoque_produtos[index_produto] >= quantidade_compra:
                    print("Temos estoque suficiente para sua compra :)")
                    print("Processando pedido...")
                    print(f"Você comprou {quantidade_compra} quantidades de {produto[1]}")
                    print("Pedido realizado!")
                    # Cadastro do cliente no Banco de Compras
                    lista_clientes.append((codigo_cliente, nome_cliente))
                    # Atualiza o total em estoque
                    estoque_produtos[index_produto] = estoque_produtos[index_produto] - quantidade_compra
                    # Atualiza o total das vendas
                    vendas_totais.append((produto[0], codigo_cliente, quantidade_compra))
                else:
                    print("Não temos essa quantidade de flores, tente um valor mais baixo!") 

                # Depois de processar o pedido, pergunta se deseja reiniciar o programa
                continua_programa = input("Deseja continuar (digite sim ou não)? ")
                if continua_programa == 'sim':
                    print("Faça seu novo pedido:")
                else:
                    print("Fim da execução do programa!")
            
            # Se não achar o código do pronduto dentro da lista, pergunta se deseja reiniciar
            else:
                print("Produto não encontrado, digite novamente!")
                continua_programa = input("Deseja continuar (digite sim ou não)? ")
                if continua_programa != 'sim':
                    print("Fim da execução do programa!")

    print("_______________________________________________________________________")
    venda_diaria = [ venda for venda in vendas_totais if vendas_totais[2] >= 2]
    if venda_diaria:
        print("Vendas onde o cliente comprou mais de 2 produtos:")
        for venda in venda_diaria:
            codigo_cliente = venda[0]
            codigo_produto = venda[1]
            quantidade = venda[2]
            print(f"Código do Cliente: {codigo_cliente} | Código do Produto: {codigo_produto} | Quantidade: {quantidade}")
    else:
        print("Não houve vendas onde o cliente comprou mais de 2 produtos.")
    
    print("_______________________________________________________________________")
    print(f"Nossos clientes cadastrados: {lista_clientes}")
    print("_______________________________________________________________________")
    print(f"Nosso total de venda: {vendas_totais}")
    print("_______________________________________________________________________")
    print("Programa finalizado!")

main()
