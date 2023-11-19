import sys

def caixeiro_viajante(grafo: list, visitados: list, posicao_atual: int, quant_cidades: int, num_cidades_visitadas: int, custos: list, solucao_otima: list):
    if (num_cidades_visitadas == quant_cidades) and grafo[posicao_atual][0]:
        solucao_otima.append(custos + grafo[posicao_atual][0])
        return
    
    for i in range(quant_cidades):
        if (visitados[i] == False) and grafo[posicao_atual][i]:
            visitados[i] = True
            caixeiro_viajante(grafo, visitados, i, quant_cidades, num_cidades_visitadas+1, custos + grafo[posicao_atual][i], solucao_otima)
            visitados[i] = False

def branch_and_bound(grafo: list, quant_cidades: int):
    visitados = [False for _ in range(quant_cidades)]
    visitados[0] = True
    solucao_otima = []
    caixeiro_viajante (grafo, visitados, 0, quant_cidades, 1,  0, solucao_otima)
    return min(solucao_otima)

grafo = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print(f"A menor distância possível para o problema TSP com 4 cidades é: {branch_and_bound(grafo, len(grafo)}")
