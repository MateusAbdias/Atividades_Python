import time
import json

def encerrar():
    global ctr
    comando = input("Deseja encerrar o programa? (s/n) ")
    if comando == 's' or comando == "S" or comando == "sim":
        print("Programa encerrado!")
        ctr = 1

def disciplinas():
    disciplinas_ofertadas = set()  # Conjunto para armazenar as disciplinas ofertadas

    for aluno in alunos:
        disciplinas = aluno["Disciplinas"] 
            
        # Adiciona as disciplinas ao conjunto de disciplinas ofertadas
        for disciplina in disciplinas:
            nome_disciplina = disciplina["Nome_Disciplina"]
            disciplinas_ofertadas.add(nome_disciplina)

    # Imprime todas as disciplinas ofertadas
    print("Disciplinas:")
    for disciplina in disciplinas_ofertadas:
        print(disciplina)

print("Olá, bem vindo ao SIGAA! \nO que deseja fazer?")
ctr = 0

alunos = [{"cpf": "000",
           "Nome": "José de Arimatheia",
           "Data_Nascimento": "11/10/1994",
           "Entrada": "2022.1",
           "Disciplinas":[
               {
                   "Codigo": 1120,
                   "Nome_Disciplina": "UX Strategy",
                   "Semestre_Cursado": 2022.1
               },
               {
                   "Codigo": 1130,
                   "Nome_Disciplina": "UI Design 1",
                   "Semestre_Cursado": 2022.1
               },
               {
                   "Codigo": 1140,
                   "Nome_Disciplina": "UX Research 1",
                   "Semestre_Cursado": 2022.2
               }
           ]
        },
        {"cpf": "001",
           "Nome": "Raphaela de Labbat",
           "Data_Nascimento": "11/07/1997",
           "Entrada": 2022.2,
           "Disciplinas":[
               {
                   "Codigo": 1120,
                   "Nome_Disciplina": "UX Strategy",
                   "Semestre_Cursado": 2022.2
               },
               {
                   "Codigo": 1130,
                   "Nome_Disciplina": "UI Design 1",
                   "Semestre_Cursado": 2022.2
               },
               {
                   "Codigo": 1140,
                   "Nome_Disciplina": "UX Research 1",
                   "Semestre_Cursado": 2023.1
               },
               {
                   "Codigo": 1150,
                   "Nome_Disciplina": "Metricas de Avaliação",
                   "Semestre_Cursado": 2022.2
               },
           ]
        }
]


while ctr != 1:
    menu = int(input
               ("O que você deseja fazer hoje? \n1. Ver alunos" 
                "\n2. Cadastrar novo aluno \n3. Ver aluno específico \n4. Remover aluno"
                "\n5. Cadastrar aluno em uma matéria \n6. Ver matéria específica \n7. Ver todas as matérias"
                "\n8. Encerrar programa \nDigite sua resposta: "))
    
    if menu == 1: # Visualiza todos os alunos
        print("Exibindo a lista de alunos com seus respectivos dados:")
        for aluno in alunos: # Itera e imprime aluno por aluno cadastrado no Banco de Dados
            print(json.dumps(aluno, indent=4)) # O método json.dumps e o indent=4 é para a formatação no terminal 
            time.sleep(0.5)  # Atraso de 0.5 segundo
        encerrar()
        time.sleep(1) # Atraso de 1 segundo

    elif menu == 2: # Cadastra um novo aluno no Banco de dados
        cpf_aluno_novo = input("Digite o cpf: ")
        encontrar_cpf = [cpf_aluno for cpf_aluno in alunos if cpf_aluno["cpf"] == cpf_aluno_novo] # Compreensão de lista que verifica se existe um cpf já na base
        print("Vamos verificar no sistema se o aluno já faz parte de nossa instituição. Aguarde!")
        time.sleep(1) # Atraso de 1 segundo
        
        if len(encontrar_cpf) > 0: # se existir o cpf na base vai ser empresso os dados do aluno correspondente
            print("Esse CPF já está cadastrado no sistema!")
            time.sleep(1) # Atraso de 1 segundo
            print(json.dumps(encontrar_cpf, indent=4)) # O método json.dumps e o indent=4 é para a formatação no terminal 
            time.sleep(0.5)  # Atraso de 0.5 segundo
            encerrar()

        else:
           # Solicita informações sobre o novo aluno
            nome_novo_aluno = input("Digite o nome completo no novo aluno: ")
            nascimento_novo_aluno = input("Digite a data de nascimento do novo aluno: ")
            semestre_entrada_novo_aluno = input("Digite o semestre de entrada do novo aluno: ")
            total_disciplinas_novo_aluno = int(input("Quantas disciplinas ele vai cursar esse semestre? "))

            lista_disciplinas_novo_aluno = [] # Lista vazia que irá armazenar as disciplinas

            # Loop para capturar os dados de cada disciplina, o loop irá repetir dependendo da quantidade de disciplinas do aluno
            for x in range(total_disciplinas_novo_aluno):
                print("Informe os dados da disciplina: ")
                codigo_disciplina = int(input("Digite o código da disciplina: "))
                nome_disciplina = input("Digite o nome da disciplina: ")
                time.sleep(0.5)  # Atraso de 0.5 segundo
                # Cria um dicionário com os dados da disciplina atual
                disciplina = {
                    "Codigo": codigo_disciplina,
                    "Nome_Disciplina": nome_disciplina,
                    "Semestre_Cursado": semestre_entrada_novo_aluno
                }
                # Adiciona a disciplina à lista de disciplinas do novo aluno
                lista_disciplinas_novo_aluno.append(disciplina)

            # Cria um objeto dentro da lista alunos para representar o novo aluno, contendo todas as informações coletadas
            alunos.append({
                "Nome": nome_novo_aluno,
                "Data_Nascimento": nascimento_novo_aluno,
                "Entrada": semestre_entrada_novo_aluno,
                "Disciplinas": lista_disciplinas_novo_aluno
            })
            print("Aluno cadastrado com sucesso!")
            print(json.dumps(alunos, indent=4))
            encerrar()

    elif menu == 3:
        print("Consultar aluno específico")
        cpf_consultar = input("Digite o cpf do aluno a ser consultado: ")
        encontrar_cpf = [cpf_aluno for cpf_aluno in alunos if cpf_aluno["cpf"] == cpf_consultar] # Compreensão de lista que verifica se existe um cpf já na base
        print("Vamos verificar no sistema se o aluno já faz parte de nossa instituição. Aguarde!")
        time.sleep(1) # Atraso de 1 segundo
        
        if len(encontrar_cpf) > 0: # se existir o cpf na base vai ser empresso os dados do aluno correspondente
            print("Esse CPF está cadastrado no sistema!")
            time.sleep(1) # Atraso de 1 segundo
            print(json.dumps(encontrar_cpf, indent=4)) # O método json.dumps e o indent=4 é para a formatação no terminal 
            time.sleep(0.5)  # Atraso de 0.5 segundo
            encerrar()

        else:
            print("CPF não encontrado no nosso banco de dados!")
            encerrar()

    elif menu == 4:
        print("Remover um aluno específico do nosso banco de dados")
        cpf_consultar = input("Digite o cpf do aluno a ser removido: ")
        print("Vamos verificar no sistema se o aluno faz parte de nossa instituição. Aguarde!")
        time.sleep(1) # Atraso de 1 segundo
        
        # Variável para armazenar o índice do aluno encontrado
        indice = 0

        # Procura o aluno com base no CPF digitado
        for i, aluno in enumerate(alunos):
            if aluno["cpf"] == cpf_consultar:
                indice = i
                break

        if indice is not 0: # Se existir esse CPF no sistema:
            print("Esse CPF está cadastrado no sistema!")
            time.sleep(1)  # Atraso de 1 segundo
            print(json.dumps(alunos[indice], indent=4))
            confirmar = input("Você tem certeza que deseja remover esse aluno? (s/n) ")
            # Remover aluno
            if confirmar.lower() in ["s", "sim"]:
                del alunos[indice]
                print("Aluno removido com sucesso!")
                time.sleep(1) # Atraso de 1 segundo
                print(alunos)
                time.sleep(1) # Atraso de 1 segundo
                encerrar()
        else:
            print("CPF não encontrado no nosso banco de dados!")
            encerrar()
        
    elif menu == 5:
        print("Vamos cadastrar um aluno em uma nova disciplina")
        cpf_aluno_verificar = input("Digite o cpf: ")
        encontrar_cpf = [cpf_aluno for cpf_aluno in alunos if cpf_aluno["cpf"] == cpf_aluno_verificar]
        print("Vamos verificar no sistema se o aluno faz parte de nossa instituição. Aguarde!")
        time.sleep(1)

        if len(encontrar_cpf) > 0:
            print("Aluno cadastrado no sistema!")
            time.sleep(1)
            total_disciplinas_aluno = int(input("Quantas disciplinas ele vai cursar esse semestre? "))

            novas_disciplinas_aluno = []  # Coleção vazia que irá armazenar as disciplinas

            for x in range(total_disciplinas_aluno):
                print("Informe os dados da disciplina: ")
                codigo_disciplina = int(input("Digite o código da disciplina: "))
                nome_disciplina = input("Digite o nome da disciplina: ")
                semestre_disciplina = int(input("Digite o semestre vigente: "))
                time.sleep(0.5)
                disciplina = {
                    "Codigo": codigo_disciplina,
                    "Nome_Disciplina": nome_disciplina,
                    "Semestre_Cursado": semestre_disciplina
                }
                novas_disciplinas_aluno.append(disciplina)

            # Atualiza a lista de disciplinas do aluno
            encontrar_cpf[0]["Disciplinas"].extend(novas_disciplinas_aluno)
            print(json.dumps(encontrar_cpf, indent=4))

            time.sleep(0.5)
            encerrar()

    elif menu == 6:
        print("Consultar todos os alunos cadastrados em uma Disciplina específica")
        materia_consultar = int(input("Digite o código da disciplina que quer consultar: "))  

        # Percorre aluno por aluno e verifica as disciplinas de todos os alunos no banco de dados
        for aluno in alunos:
            disciplinas_aluno = aluno["Disciplinas"]  # Obtém a lista de disciplinas do aluno
            
            # Verifica se o aluno está matriculado na Disciplina a consultar
            for disciplina in disciplinas_aluno:
                if disciplina["Codigo"] == materia_consultar:
                    time.sleep(1) # Atraso de 1 segundo
                    print("Aluno:", aluno["Nome"])
                    print("Disciplina:", disciplina)
                    time.sleep(1) # Atraso de 1 segundo
                    encerrar()
                else:
                    print("Não existe Disciplina com esse código no sistema!")
                    time.sleep(1) # Atraso de 1 segundo
                    encerrar()

    elif menu == 7:
        time.sleep(1) # Atraso de 1 segundo
        disciplinas()
        time.sleep(1) # Atraso de 1 segundo
        encerrar()

    else:
        break
