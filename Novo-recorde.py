# Titulo: Novo Recorde
# Código: 2551

while True:
    try:
        qtd_treinos = int(input())

        historico = []
        dia = 1

        while dia <= qtd_treinos:
            dados = input().split()
            duracao = int(dados[0])
            distancia = int(dados[1])
            veloc_media = distancia / duracao
            
            if dia == 1 or veloc_media > max(historico):
                print(dia)

            historico.append(veloc_media)

            dia += 1
            
    except EOFError:
        break

    