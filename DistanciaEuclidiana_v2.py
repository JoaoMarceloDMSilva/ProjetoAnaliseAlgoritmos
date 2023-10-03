import math
import sys
import random


NUM_POINTS = 10
MAX_INT = sys.maxsize


# Dois pontos estarão próximos quanto menor a razão entre X e Y
# O ponto mais próximo é aquele que tiver menor distância em X e Y
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.nextPoint_X = None
        self.nextPoint_Y = None
        self.range_X = 0
        self.range_Y = 0


#   Calcula a Hipotenusa
def hypotenuse(side_1: Point, side_2: Point) -> float:
    return math.sqrt(abs(side_1.x - side_2.x)**2 + abs(side_1.y - side_2.y)**2)


#   Números Int Aleatórios   
def generateRandomPoints() -> Point:
    return Point(random.randint(0, 100), random.randint(0, 100))


def quicksort_X(listPoints: list) -> list:
    if len(listPoints) <= 1:
        return listPoints
    else:
        pivot = listPoints[0]
        smaller = [item for item in listPoints[1:] if item.x <= pivot.x]
        larger = [item for item in listPoints[1:] if item.x > pivot.x]
        return quicksort_X(smaller) + [pivot] + quicksort_X(larger)
    
def quicksort_Y(listPoints: list) -> list:
    if len(listPoints) <= 1:
        return listPoints
    else:
        pivot = listPoints[0]
        smaller = [item for item in listPoints[1:] if item.y <= pivot.y]
        larger = [item for item in listPoints[1:] if item.y > pivot.y]
        return quicksort_Y(smaller) + [pivot] + quicksort_Y(larger)



def whoIsNext_X(listPoints_X: list) -> None:
    i = 0
    while (i < (len(listPoints_X) -1)):
        listPoints_X[i].nextPoint_X = listPoints_X[i+1]
        i += 1
    listPoints_X[-1] = listPoints_X[i]

def whoIsNext_Y(listPoints_Y: list) -> None:
    i = 0
    while (i < (len(listPoints_Y) -1)):
        listPoints_Y[i].nextPoint_Y = listPoints_Y[i+1]
        i += 1
    listPoints_Y[-1] = listPoints_Y[i]

def calcRanges_XY(listPoints: list) -> None:
    for point in listPoints:
        point.range_X = abs(point.x - point.nextPoint_X.x)
        point.range_Y = abs(point.y - point.nextPoint_Y.y)

def reduceQuantPoints(listPoints: list) -> Point:
    shortRange = MAX_INT
    getPoint = None

    for point in listPoints:
        if abs(point.range_X - point.range_Y) < shortRange:
            getPoint = point
    return getPoint

def shortestEuclidianDistance(point: Point) -> tuple:
    shortestDistance = hypotenuse(point, point.nextPoint_X)
    if shortestDistance <= hypotenuse(point, point.nextPoint_Y):
        return (point, point.nextPoint_X, shortestDistance)
    else:
        return (point, point.nextPoint_Y, shortestDistance, hypotenuse(point, point.nextPoint_Y))


ponto_01= Point(53, 10)
ponto_02= Point(25, 99)
ponto_03= Point(98, 52)
ponto_04= Point(52, 97)
ponto_05= Point(16, 76)
ponto_06= Point(23, 25)
ponto_07= Point(71, 12)
ponto_08= Point(19, 27)
ponto_09= Point(9, 26)
ponto_10= Point(20, 17)

# listWithPoints = [generateRandomPoints() for _ in range (NUM_POINTS)]
listWithPoints = [ponto_01, ponto_02, ponto_03, ponto_04, ponto_05, ponto_06, ponto_07, ponto_08, ponto_09, ponto_10]

ord_X = quicksort_X(listWithPoints)
ord_Y = quicksort_Y(listWithPoints)

print("-"*10)
for i in ord_X:
    print(f"({i.x, i.y})")
print("-"*10)
for i in ord_Y:
    print(f"({i.x, i.y})")
print("-"*10)

whoIsNext_X(ord_X)
whoIsNext_Y(ord_Y)

result = shortestEuclidianDistance(reduceQuantPoints(listWithPoints))
print(f"\nPonto I: ({result[0].x}, {result[0].y})")
print(f"Ponto II: ({result[1].x}, {result[1].y})")
print(f"Distância: {result[2]}")

prox_Y = result[1].nextPoint_Y
print(f"{(prox_Y.x , prox_Y.y)}")
# ponto_01= Point(53, 10)
# ponto_02= Point(25, 99)
# ponto_03= Point(98, 52)
# ponto_04= Point(52, 97)
# ponto_05= Point(16, 76)
# ponto_06= Point(23, 25)
# ponto_07= Point(71, 12)
# ponto_08= Point(19, 27)
# ponto_09= Point(9, 26)
# ponto_10= Point(20, 17)
# ----------

# Ponto I: (23, 25)
# Ponto II: (19, 27)
# Distância: 4.47213595499958