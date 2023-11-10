def validar_movimento(tabuleiro: list, x: int, y: int) -> bool:
    return 0 <= x < len(tabuleiro) and 0 <= y < len(tabuleiro)

def imprimir_tabuleiro(tabuleiro: list)-> None:
    for linha in tabuleiro:
        print(linha)
    print("\n")

def resolver_passeio_cavaleiro(tabuleiro: list, x:int, y:int, movimento: int, mov_x: tuple, mov_y: tuple, e_valido: bool = False) -> bool:
    if movimento == (pow(len(tabuleiro), 2)+1):
        imprimir_tabuleiro(tabuleiro)
        return True
    for prox_movimento in range(8):
        prox_x = x + mov_x[prox_movimento]
        prox_y = y + mov_y[prox_movimento]
        if validar_movimento(tabuleiro, prox_x, prox_y):
            if tabuleiro[prox_x][prox_y] == -1:
                tabuleiro[prox_x][prox_y] = movimento
                e_valido = resolver_passeio_cavaleiro(tabuleiro, prox_x, prox_y, movimento + 1, mov_x, mov_y)
                if not e_valido:
                    tabuleiro[prox_x][prox_y] = -1
                else:
                    e_valido = True
    return False
    
    # if not e_valido:
    #     print("\nBacktracking\n")
    #return e_valido
                
def passeio_cavaleiro(tamanho_tabuleiro: int, init_x: int, init_y: int) -> list:
    tabuleiro = [[-1 for _ in range(tamanho_tabuleiro)] for _ in range(tamanho_tabuleiro)]
    movimentos_X = 1, -1, -2, -2, -1, 1, 2, 2
    movimentos_Y = 2, 2, 1, -1, -2,-2, 1, -1
    tabuleiro[init_x][init_y] = 1
    return resolver_passeio_cavaleiro(tabuleiro, init_x, init_y, 2, movimentos_X, movimentos_Y)

def validar_posicao_inicial(tamanho_tabuleiro: int, valor: int) -> int:
    while (valor < 0) or (valor >= tamanho_tabuleiro):
        valor = int(input("Informe um valor válido na posição: "))
    return valor

#   EXECUTAR
tamanho_tabuleiro = int(input("Informe o tamanho do Tabuleiro: "))
init_x = validar_posicao_inicial(tamanho_tabuleiro, int(input("Informe o valor na posição X: ")))
init_y = validar_posicao_inicial(tamanho_tabuleiro, int(input("Informe o valor na posição Y: ")))

resultado = passeio_cavaleiro(tamanho_tabuleiro, init_x, init_y)
print(resultado)
if not resultado:
    print("NÃO HÁ SOLUÇÕES")
