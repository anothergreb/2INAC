def soma(x,y): return x + y
def subtracao(x,y): return x - y
def multiplicacao(x,y): return x * y
def divisao(x,y): return x / y

while True:
    print('-' * 50)
    user_input = int(input("""Digite o numero de qual operador deseja usar:
          1. Soma
          2. Subtração
          3. Multiplicação
          4. Divisão
          5. Sair\n"""))
    if user_input == 1:
        x = float(input("Digite o 1º numero: "))
        y = float(input("Digite o 2º numero: "))
        print(f"A soma de {x} e {y} é = {soma(x,y)}")
    elif user_input == 2:
        x = float(input("Digite o 1º numero: "))
        y = float(input("Digite o 2º numero: "))
        print(f"A subtração de {x} e {y} é = {subtracao(x,y)}")
    elif user_input == 3:
        x = float(input("Digite o 1º numero: "))
        y = float(input("Digite o 2º numero: "))
        print(f"A multiplicação de {x} e {y} é = {multiplicacao(x,y)}")
    elif user_input == 4:
        x = float(input("Digite o 1º numero: "))
        y = float(input("Digite o 2º numero: "))
        print(f"A divisão de {x} e {y} é = {divisao(x,y)}")
    elif user_input == 5:
        break
    else:
        print("Digite um numero válido!")
    