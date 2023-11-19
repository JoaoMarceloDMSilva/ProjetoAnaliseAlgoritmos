import sys

def caixeiro_viajante(grafo: list, visitados: list, posicao_atual: int, quant_cidades: int, num_cidades_visitadas: int, custos: list, solucao_otima: list, caminho_atual: int):
    if num_cidades_visitadas == quant_cidades:
        if grafo[posicao_atual][0] != 0:
            solucao_otima.append(custos + grafo[posicao_atual][0])
            return caminho_atual + [0]

    melhor_caminho = None
    melhor_custo = sys.maxsize

    for i in range(quant_cidades):
        if not visitados[i] and grafo[posicao_atual][i]:
            visitados[i] = True
            caminho = caixeiro_viajante(grafo, visitados, i, quant_cidades, num_cidades_visitadas + 1, custos + grafo[posicao_atual][i], solucao_otima, caminho_atual + [i])
            visitados[i] = False

            if caminho[-1] == 0 and custos + grafo[posicao_atual][i] < melhor_custo:
                melhor_caminho = caminho
                melhor_custo = custos + grafo[posicao_atual][i]

    return melhor_caminho

def branch_and_bound(grafo: list, quant_cidades: int):
    visitados = [False for _ in range(quant_cidades)]
    visitados[0] = True
    solucao_otima = []
    caminho_otimo = caixeiro_viajante(grafo, visitados, 0, quant_cidades, 1, 0, solucao_otima, [0])
    return caminho_otimo

def print_caminho(caminho: list):
    for i in range(len(caminho) - 1):
        print(caminho[i], end=" -> ")
    print(caminho[-1])

grafo = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

caminho_otimo = branch_and_bound(grafo, len(grafo))
custo_otimo = sum(grafo[caminho_otimo[i]][caminho_otimo[i + 1]] for i in range(len(caminho_otimo) - 1))

print(f"A menor distância possível para o problema TSP com 4 cidades é: {custo_otimo}")
print("O caminho ótimo é:")
print_caminho(caminho_otimo)
