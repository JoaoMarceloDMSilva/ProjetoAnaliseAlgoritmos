nodoNumber = 1  #   Identificar os "Nodo" gerados por "createNodoByTuple"

class Nodo:
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
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
def listToDict(phrase: list) -> dict:   #   Usado apenas para criar o Dicionário Original
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

#   Separa um Dicionário em uma Lista de Dicionários;
def dictToList(dictionary: dict) -> list:
    auxList = []
    for key in dictionary.keys():
        auxList.append({key: dictionary[key]})
    return auxList

#   Cria uma Tupla de Nodo para utilizar em "createNodoByTuple";
def createNodoByList(listOfDict: list) -> tuple:
    nodoLeft = Nodo(list(listOfDict[-1].keys())[0], list(listOfDict[-1].values())[0])
    nodoRight = Nodo(list(listOfDict[-2].keys())[0], list(listOfDict[-2].values())[0])
    return (nodoLeft, nodoRight)

#   Cria um "Nodo" Pai cujos filhos são os elementos da Tupla
def createNodoByTuple(tupleWithObj: tuple) -> Nodo:
    global nodoNumber
    auxNodo = Nodo(f"N{nodoNumber}", tupleWithObj[0].value + tupleWithObj[1].value)
    nodoNumber += 1
    auxNodo.addRight(tupleWithObj[0])
    auxNodo.addLeft(tupleWithObj[1])
    return auxNodo

#   List(Dict) >> Dict para poder reorganizar em "quicksortDict"
def createDictToSort(listDict: list) -> dict:
    return {key: value  for i in listDict for key, value in i.items()}

#   Adiciona um dict(Nodo) na List(Dict)
def addNodoToListofDict(nodo: Nodo, listWithDict: list)-> list:
    listWithDict.append({nodo.name: nodo.value})
    return listWithDict

def cleanListOfDict(listOfDictAfterAddNodo: list) -> list:
    listAux = listOfDictAfterAddNodo.copy()
    while len(listOfDictAfterAddNodo) != (len(listAux)-2):
        del listOfDictAfterAddNodo[-1]
    return listOfDictAfterAddNodo

#   Organiza a Nova List(Dict)
def newOrganizedDict(listWithDict: list) -> dict:
    auxDict = createDictToSort(listWithDict)
    return quicksortDict(auxDict)


#   O.B.S.: 
#   I :: Precisa de um dicionário Auxiliar [remover os dois últimos elementos sempre que criar um Nodo] e um Original

#def huffmanAlgorithm(phrase: str) -> dict:...

# userText: str = "Joao Marcelo"

# passo01 = list(userText)
# passo02 = listToDict(passo01)   # Transforma uma Lista em Dicionário
# passo03 = quicksortDict(passo02) #  Dicionário Organizado Crescente
# passo04 = dictToList(passo03)   # Transforma o Dicionário Organizado em uma Lista de Dicionários Organizado
# #   LOOP
# passo05 = createNodoByList(passo04) # Tranforma os dois últimos elementos em um Tupla de Nodo
# passo06 = createNodoByTuple(passo05) # Cria um Nodo pai para a Tupla de Nodo
# passo07 = addNodoToListofDict(passo06, passo04) # Adiciona o Nodo Pai no final da Lista de Dicionários Organizado
# passo08 = createDictToSort(passo07) # Transforma a lista em Dicionário
# passo09 = quicksortDict(passo08) # Organiza o novo Nodo
# passo10 = dictToList(passo09)   # Transforma o Dicionário em Lista 
# passo11 = cleanListOfDict(passo10) # Elimina os dois últimos elementos da lista
# print(passo11)
# #   END LOOP
