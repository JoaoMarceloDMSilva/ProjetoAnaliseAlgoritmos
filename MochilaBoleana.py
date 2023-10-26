class Item:
    def __init__(self, name: str, value: int, weight: int) -> None:
        self.name = name
        self.value = value
        self.weight = weight

def knapsack(items: list, capacity: int) -> tuple:
    quantityItems = len(items)
    #   GERAR UMA MATRIZ NxM
    matrix = [ [0 for _ in range(capacity+1)] for _ in range(quantityItems + 1)]
    # "+1" para ir de 0 a N, pois 'range()' vai de 0 a N-1

    for indexItem in range(1, quantityItems + 1):
        for temporaryCapacity in range(1, capacity + 1):
            if items[indexItem - 1].weight > temporaryCapacity:
                matrix[indexItem][temporaryCapacity] = matrix[indexItem - 1][temporaryCapacity]
            else:
                matrix[indexItem][temporaryCapacity] = max(matrix[indexItem - 1][temporaryCapacity], matrix[indexItem - 1][temporaryCapacity - items[indexItem - 1].weight] + items[indexItem - 1].value)
    maxValue = matrix[quantityItems][capacity]

    chosenItems = []
    quantItens_AUX = quantityItems
    capacity_AUX = capacity
    
    while quantItens_AUX > 0 and capacity_AUX > 0:
        if matrix[quantItens_AUX][capacity_AUX] != matrix[quantItens_AUX - 1][capacity_AUX]:
            chosenItems.append(items[quantItens_AUX - 1].name)
            capacity_AUX -= items[quantItens_AUX - 1].weight
        quantItens_AUX -= 1
    
    return (chosenItems, maxValue, matrix)

#   EXECUTAR
item_01 = Item("Joia", 2, 3)
item_02 = Item("Celular", 2, 1)
item_03 = Item("Tablet", 4, 3)
item_04 = Item("Notebook", 5, 4)
item_05 = Item("Som", 3, 2)

lista_itens = [item_01, item_02, item_03, item_04, item_05]
capacidadeMAX = 7

tupla = knapsack(lista_itens, capacidadeMAX)

print("Itens escolhidos: ")
for item in tupla[0]:
    print(f"{item}")
print(f"\nValor máximo: {tupla[1]}\n")
for linha in tupla[2]:
    print(linha)