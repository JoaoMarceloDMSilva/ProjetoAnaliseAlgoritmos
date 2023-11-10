#   MOVIMENTO CAVALO         https://www.youtube.com/watch?v=xwLEzqkKCDU

    # 0   x   0   x   0

    # x   0   0   0   x

    # 0   0   §   0   0     movimentos_X = [1, -1, -2, -2, -1, 1, 2] || movimentos_Y = [2, 2, 1, -1, -2,-2, 1, -1]

    # x   0   0   0   X

    # 0   x   0   x   0

def validar_movimento(tabuleiro: list, x: int, y: int) -> bool:
    return (x >= 0 and x < len(tabuleiro)) and (y >= 0 and y < len(tabuleiro)) and (tabuleiro[x][y] == -1)

def resolver_Passeio_Cavaleiro(tabuleiro: list, x: int, y: int, movimento: int, movimentos_X: list, movimentos_Y: list) -> list:
    if movimento == (len(tabuleiro) * len(tabuleiro)):
        return tabuleiro
    else:
        movimentos_visitados = set()
        for proximo_movimento in range(8):
            proximo_X = x + movimentos_X[proximo_movimento]
            proximo_Y = y + movimentos_Y[proximo_movimento]
            if proximo_X not in movimentos_visitados and proximo_Y not in movimentos_visitados:
                tabuleiro[proximo_X][proximo_Y] = movimento
                movimentos_visitados.add(proximo_X)
                movimentos_visitados.add(proximo_Y)
                resolver_Passeio_Cavaleiro(tabuleiro, proximo_X, proximo_Y, movimento + 1, movimentos_X, movimentos_Y)
                tabuleiro[proximo_X][proximo_Y] = -1
    return None

# def resolver_Passeio_Cavaleiro(tabuleiro: list, x: int, y: int, movimento: int, movimentos_X: list, movimentos_Y: list) -> list:
#     if movimento == (len(tabuleiro) * len(tabuleiro)):
#         return tabuleiro
#     else:
#         for proximo_movimento in range(8):
#             proximo_X = x + movimentos_X[proximo_movimento]
#             proximo_Y = y + movimentos_Y[proximo_movimento]
#             if validar_movimento(tabuleiro, proximo_X, proximo_Y):
#                 tabuleiro[proximo_X][proximo_Y] = movimento
#                 resolver_Passeio_Cavaleiro(tabuleiro, proximo_X, proximo_Y, movimento + 1, movimentos_X, movimentos_Y)
#                 tabuleiro[proximo_X][proximo_Y] = -1
#     return None

def passeio_Cavaleiro(tamanho_tabuleiro: int, init_x: int, init_y: int) -> list:
    tabuleiro = [[-1 for _ in range(tamanho_tabuleiro)] for _ in range(tamanho_tabuleiro)]
    movimentos_X = [1, -1, -2, -2, -1, 1, 2, 2]
    movimentos_Y = [2, 2, 1, -1, -2,-2, 1, -1]

    tabuleiro[init_x][init_y] = 0
    return resolver_Passeio_Cavaleiro(tabuleiro, init_x, init_y, 1, movimentos_X, movimentos_Y)

def validar_Posicao_Inicial(tamanho_tabuleiro: int, valor: int) -> int:
    while (valor < 0) and (valor >= tamanho_tabuleiro):
        valor = int(input("Informe um valor válido na posição: "))
    return valor

#   EXECUTAR
tamanho_tabuleiro = int(input("Informe o tamanho do Tabuleiro: "))
init_x = validar_Posicao_Inicial(tamanho_tabuleiro, int(input("Informe o valor na posição X: ")))
init_y = validar_Posicao_Inicial(tamanho_tabuleiro, int(input("Informe o valor na posição Y: ")))

resultado = passeio_Cavaleiro(tamanho_tabuleiro, init_x, init_y)
print(resultado)
if resultado is not None:
    for linha in resultado:
        print(linha)
else:
    print("NÃO HÁ SOLUÇÕES")