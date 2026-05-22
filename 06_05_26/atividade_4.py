idade = int(input("Digite sua idade: "))

classificacao = None

if idade <= 12 :
    classificacao = "criança"
    print(classificacao)
elif idade > 12 & idade <= 17:
    classificacao = "adolescente"
    print(classificacao)
elif idade > 17 & idade <= 64:
    classificacao = "adulto"
    print(classificacao)
elif idade > 64:
    