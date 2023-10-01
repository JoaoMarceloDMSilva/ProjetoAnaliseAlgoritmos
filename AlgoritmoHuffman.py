class Nodo:
    def __init__(self, name: str) -> None:
        self.name = name
        self.left = None
        self.right = None

    def addLeft(self, nodo: object):
        self.addLeft = nodo
    
    def addRight(self, nodo: object):
        self.addRight = nodo

def head(stringList: list):
    return stringList[0] if len(stringList) > 0 else []

def tail(stringList: list):
    return stringList[1:] if len(stringList) > 0 else []

def deleteChar(character: str, phrase: list) -> list:
    while character in phrase:
        phrase.remove(character)
    return phrase

def listWhitoutRepetition(phrase: list) -> list:
    if len(phrase) == 0:
        return []
    else:
        return [head(phrase)] + listWhitoutRepetition(deleteChar(head(phrase), tail(phrase)))

def listToDict(phrase: list) -> dict:
    auxDict = dict()
    for key in listWhitoutRepetition(phrase):
        auxDict[key] = phrase.count(key)
    return auxDict

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

def dictToList(dictionary: dict) -> list:
    auxList = []
    for key in dictionary.keys():
        auxList.append({key: dictionary[key]})
    return auxList

def createNodo(listOfDict: list) -> tuple:
    nodoLeft = Nodo(list(listOfDict[-1].keys())[0])
    nodoRight = Nodo(list(listOfDict[-2].keys())[0])
    return (nodoLeft, nodoRight)
def huffmanAlgorithm(phrase: str) -> dict:...


# userText: str = "Joao Marcelo"

# print(dictToList(quicksortDict(listToDict(list(userText)))))
# nodoTuple = createNodo(dictToList(quicksortDict(listToDict(list(userText)))))
# for i in nodoTuple:
#     print(i.name)