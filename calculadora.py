import math

print("Bem vindo ao Calculadora")
print("Aqui fazemos calculos de adição, subtração, multiplicação e divisão")
print("Digite o primeiro número:")

def main():
    num1 = float(input())
    print("Digite o segundo número:")
    num2 = float(input())
    print("Qual é a operação que você quer fazer?")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Raiz quadrada, iremos calcular apenas o primeiro valor")
    operador = input("Digite a operação que deseja realizar: ")
    
    def soma():
        print(num1 + num2)
    def subtracao():
        print(num1 - num2)
    def multiplicacao():
        print(num1 * num2)
    def divisao():
        print(num1 / num2)
    def raizquad():
        print(math.sqrt(num1))

    if operador == '1' or operador == 'adição':
        soma()
    elif operador == '2' or operador == 'subtração':
        subtracao()
    elif operador == '3' or operador == 'multiplicação':
        multiplicacao()
    elif operador == '4' or operador == 'divisão':
        divisao()
    elif operador == '5' or operador == 'Raiz':
        raizquad()
    else:
        print("operador inválido")

main()

#aplicando a recursiva para reniciar ou não 
restart = input("Deseja continuar Sim ou Não?")
if restart == "sim":
    main()
else:
    print("fim do programa")
