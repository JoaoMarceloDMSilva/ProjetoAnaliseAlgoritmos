nodoNum = 1
class Nodo:
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
        self.left = None
        self.right = None
    def add_Left(self, nodo: object):
        self.left = nodo
    def add_Right(self, nodo: object):
        self.right = nodo

class Leaf(Nodo):
    def __init__(self, name: str, value: int) -> None:
        super().__init__(name, value)

#   Remove caracteres repetidos:
def remove_duplicates(string: str):
    return list(set(string))

#   Criar as Folhas da Árvore:
def create_Leaves(phrase: str):
    listWithoutDuplicates = remove_duplicates(phrase)
    listWithLeaves = []
    for char in listWithoutDuplicates:
        aux = Leaf(char, phrase.count(char))
        listWithLeaves.append(aux)
    return listWithLeaves

#   Organiza uma lista de Objetos Nodo em ordem decrescente
def quicksort_decreasing(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x.value > pivot.value]  # Elementos maiores que o pivô
    middle = [x for x in lista if x.value == pivot.value]  # Elementos iguais ao pivô
    right = [x for x in lista if x.value < pivot.value]  # Elementos menores que o pivô

    return quicksort_decreasing(left) + middle + quicksort_decreasing(right)

#   Ordena e Exclui os dois últimos itens da lista
def rearrange(list_to_rearrange: list) -> list:
    auxList = quicksort_decreasing(list_to_rearrange)
    for i in range(2):
        auxList.pop(-1)
    return auxList

def create_Tree(leaves: list):
    if len(leaves) == 1:
        return leaves
    else:
        global nodoNum
        left_leaf = leaves[-1]
        right_leaf = leaves[-2]

        newNodo = Nodo(f"N{nodoNum}", left_leaf.value + right_leaf.value)
        nodoNum += 1

        newNodo.add_Left(left_leaf)
        newNodo.add_Right(right_leaf)

        leaves.append(newNodo)
        newList = rearrange(leaves)

        return create_Tree(newList)

def huffman_codes(root: Nodo) -> dict:
    codes = {}

    def traverse(node, code):
        if node.name is not None and isinstance(node, Leaf):
            codes[node.name] = code
        if node.left is not None:
            traverse(node.left, code + '0')
        if node.right is not None:
            traverse(node.right, code + '1')
    
    traverse(root, '')
    return codes


#   EXECUTAR
lista_Folhas_Organizadas = quicksort_decreasing(create_Leaves("Joao Marcelo"))

raiz_Arvore = create_Tree(lista_Folhas_Organizadas)[0]
dicionario = huffman_codes(raiz_Arvore)
print(dicionario)
# print(len(raiz_Arvore))
# for item in lista_Folhas_Organizadas:
#     print(f"{item.name}: {item.value}")
# print(f"{raiz_Arvore.name}: {raiz_Arvore.value}")
