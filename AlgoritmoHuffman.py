nodoNumber = 1  #   Identificar os "Nodo" gerados por "createNodoByTuple"

#   ALTERAR
class Nodo:
    def __init__(self, name: str) -> None:  #   <-- Aqui
        self.name = name
        self.value = None   # <-- Aqui
        self.left = None
        self.right = None

    def addLeft(self, nodo: object):
        self.left = nodo
    
    def addRight(self, nodo: object):
        self.right = nodo

def head(stringList: list):
    return stringList[0] if len(stringList) > 0 else []

def tail(stringList: list):
    return stringList[1:] if len(stringList) > 0 else []

#   Deleta todas a aparições de um Char;
def deleteChar(character: str, phrase: list) -> list:
    while character in phrase:
        phrase.remove(character)
    return phrase

#   Cria uma lista sem Char repetidos;
def listWhitoutRepetition(phrase: list) -> list:
    if len(phrase) == 0:
        return []
    else:
        return [head(phrase)] + listWhitoutRepetition(deleteChar(head(phrase), tail(phrase)))

#   Tranforma uma lista de Char em um Dicionário;
def listToDict(phrase: list) -> dict:
    auxDict = dict()
    for key in listWhitoutRepetition(phrase):   #   Chaves únicas
        auxDict[key] = phrase.count(key)        #   Conta as aparições desse Char 
    return auxDict

#   Organiza o Dicionário em Ordem Decrescente;
def quicksortDict(initialDictionary: dict) -> dict:
    if len(initialDictionary) <= 1:
        return initialDictionary
    else:
        pivotKey = list(initialDictionary.keys())[0]    #   Pega a primeira chave do Dicionário
        pivotValue = initialDictionary[pivotKey]        #   Pega o valor daquela chave

        smaller = {key: value for key, value in initialDictionary.items() if value < pivotValue}
        equals = {key: value for key, value in initialDictionary.items() if value == pivotValue}
        larger = {key: value for key, value in initialDictionary.items() if value > pivotValue}

        #   Desempacotar (**) os dicionários. Semelhante a um [] + []
        return {**quicksortDict(larger), **equals, **quicksortDict(smaller)}

#   Transforma Dict >> List(Dict);
def dictToList(dictionary: dict) -> list:
    auxList = []
    for key in dictionary.keys():
        auxList.append({key: dictionary[key]})
    return auxList

#   Cria uma Tupla de Nodo para utilizar em "createNodoByTuple";
def createNodoByList(listOfDict: list) -> tuple:
    nodoLeft = Nodo(list(listOfDict[-1].keys())[0])
    nodoRight = Nodo(list(listOfDict[-2].keys())[0])
    return (nodoLeft, nodoRight)

#   Cria um "Nodo" Pai cujos filhos são os elementos da Tupla
def createNodoByTuple(tupleWithObj: tuple) -> Nodo:
    global nodoNumber
    auxNodo = Nodo(f"N{nodoNumber}")
    nodoNumber += 1
    auxNodo.addRight(tupleWithObj[0])
    auxNodo.addLeft(tupleWithObj[1])
    return auxNodo

#   List(Dict) >> Dict para poder reorganizar em "quicksortDict"
def dictToSort(listDict: list) -> dict:
    return {key: value  for i in listDict for key, value in i.items()}

#   Adiciona um dict(Nodo) na List(Dict)
def addNodoToListofDict(nodo: Nodo, listWithDict: list)-> list:
    listWithDict.append({nodo.name: 1})
    return listWithDict

#   Organiza a nova List(Dict)
def newOrganizedDict(listWithDict: list) -> dict:
    auxDict = dictToSort(listWithDict)
    return quicksortDict(auxDict)

#   O.B.S.: 
#   I :: Precisa de um dicionário Auxiliar [remover os dois últimos elementos sempre que criar um Nodo] e um Original
#   II :: O valor de um nodo deve ser igual a somo de seus filhos

#def huffmanAlgorithm(phrase: str) -> dict:...


# userText: str = "Joao Marcelo"

# listaDicio =(dictToList(quicksortDict(listToDict(list(userText)))))
# print(dictToSort(listaDicio))
# nodoTuple = createNodoByList(dictToList(quicksortDict(listToDict(list(userText)))))
# newNodo = createNodoByTuple(nodoTuple)

# addNodo = addNodoToListofDict(newNodo, listaDicio)
# print(f"Novo Dicionário:\n{newOrganizedDict(addNodo)}")
# print(f"Nome: {newNodo.name}, Esquerda: {newNodo.left.name}, Direita: {newNodo.right.name}")
# for i in nodoTuple:
#     print(i.name)
