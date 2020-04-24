
dados = input().split()
c = int(dados[0])
n = int(dados[1])

chave1 = input().lower()
chave2 = input().lower()

for x in range(n):
    texto_criptografado = input()
    texto_descriptografado = ""

    for letra in texto_criptografado:
        letra2 = letra.lower()

        if letra2 in chave1:
            posicao = chave1.find(letra2)
            letra2 = chave2[posicao]

        elif letra2 in chave2:
            posicao = chave2.find(letra2)
            letra2 = chave1[posicao]

        if letra.isupper():
            letra2 = letra2.upper()

        texto_descriptografado += letra2

    print(texto_descriptografado)
