nomes = []
medias = []

def calcular_media(n1, n2, n3):
    # Validação das notas (Desafio Extra)
    if not (0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10):
        print("Atenção: Alguma nota é inválida (menor que 0 ou maior que 10).")
        return -1

    media = (n1 + n2 + n3) / 3   
    return round(media, 1)

def verificar_status(media):
    if media == 1:
        return "Erro de Digitação"
    
    if media >= 6.0:
        return "Aprovado"
    elif media >= 4.0:
        return "Recuperação"
    else:
        return "Reprovado"

print("--- SISTEMA DE COLETA DE NOTAS ---")

for i in range(3):
    nome = input(f"\nDigite o nome {i+1}º aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media_calculada = calcular_media(nota1, nota2, nota3)

    nomes.append(nome)
    medias.append(media_calculada)

print("\nTodos os dados foram processados com sucesso!")
print("-" * 40)

print("\n--- RELATÓRIO DE DESEMPENHO ---")

for i in range(len(nomes)):
    # Resgatando os dados
    aluno = nomes[i]
    media_final = medias[i]

    #  Chamando a 2ª função
    status_final = verificar_status(media_final)

    print(f"Aluno(a): {aluno} | Média: {media_final} | Status: {status_final}")

