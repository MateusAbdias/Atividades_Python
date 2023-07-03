print("Bem vindo a calculadora de Coodernadas no plano cartesiano")
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

if x == 0 and y == 0:
    print("O ponto está na origem")
elif x == 0:
    print("O ponto está na linha do eixo y")
elif y == 0:
    print("O ponto está na linha do eixo x")
elif x > 0 and y > 0:
    print("O ponto está no primeiro quadrante")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante")
else:
    print("Foi triste")