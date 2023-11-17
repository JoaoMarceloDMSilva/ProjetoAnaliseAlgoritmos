import sys
MAX_INT = sys.maxsize

def criar_matriz(tamanho: int) -> list:
    return [[0 for _ in range (tamanho)] for _ in range(tamanho)]


def subtrair_valor_coluna(matriz: list, coluna: int, valor: int) -> list:
    x = len(matriz)
    y = len(matriz[0])
    
    if coluna < 0 or coluna > y:
        return matriz
    
    for i in range(x):
        if matriz[i][coluna] != MAX_INT:
            matriz[i][coluna] -= valor
    return matriz

def subtrair_valor_linha(linha: list, valor: int) -> list:
    return [elem - valor if elem != MAX_INT else elem for elem in linha]

def sum_menores_valores_linhas(matriz: list) -> int:
    menores_valores = []
    for linha in matriz:
        menores_valores.append(min(linha))
    return sum(menores_valores)

def sum_menores_valores_colunas(matriz: list) -> int:
    x = len(matriz)
    y = len(matriz[0])
    menores_valores = [min(matriz[x][y] for i in range(x)) for j in range(y)]
    return sum(menores_valores)

def menor_custo(matriz: list) -> int:
    linhas = sum_menores_valores_linhas(matriz)
    colunas  = sum_menores_valores_colunas(matriz)
    return linhas + colunas