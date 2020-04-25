# TITULO: Decifrando a Carta Criptografada
# CÓDIGO: 2502

while True:
    try:
        dados = input().split()
        tamanho_cifras = int(dados[0])
        qtd_textos_criptografados = int(dados[1])

        chave1 = input().lower()
        chave2 = input().lower()

        for x in range(qtd_textos_criptografados):
            texto_criptografado = input()
            texto_descriptografado = ""

            for letra1 in texto_criptografado:
                letra2 = letra1.lower()

                if letra2 in chave1:
                    posicao = chave1.find(letra2)
                    letra2 = chave2[posicao]

                elif letra2 in chave2:
                    posicao = chave2.find(letra2)
                    letra2 = chave1[posicao]

                if letra1.isupper():
                    letra2 = letra2.upper()

                texto_descriptografado += letra2

            print(texto_descriptografado)
        print()
    except EOFError:
        break