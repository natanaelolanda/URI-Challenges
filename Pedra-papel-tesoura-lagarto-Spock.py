# Titulo: Pedra-papel-tesoura-lagarto-Spock
# Código: 1873

regras = {
    "pedra": ["lagarto", "tesoura"],
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "spock"],
    "lagarto": ["papel", "spock"],
    "spock": ["tesoura", "pedra"]
}

qtd = int(input())
for x in range(qtd):
    escolhas = input().split(' ')
    rajesh = escolhas[0]
    sheldon = escolhas[1]

    if rajesh == sheldon:
        print("empate")
    elif sheldon in regras[rajesh]:
        print("rajesh")
    else:
        print("sheldon")