#   Aluno:: João Marcelo Diniz Mendes da Silva | Projeto e Análise de Algoritmos [PAA]
import math
import sys
import random

#   CONSTANTES
MAX_FLOAT = sys.float_info.max
NUM_POINTS = 10

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

#   Primeiro Elemento da Lista
def head(point_list: list) -> object:
    return point_list[0] if len(point_list) >=1 else []

#   Tudo, exceto o Primeiro Elemento da Lista
def tail(point_list: list) -> list:
    return point_list[1:] if len(point_list) >= 1 else []

#   Calcula a Hipotenusa
def hypotenuse(side_1: Point, side_2: Point) -> float:
    return math.sqrt(abs(side_1.x - side_2.x)**2 + abs(side_1.y - side_2.y)**2)

#  Procura a Menor Distância Euclidiana 
def shortestEuclidianDistance (copy_point_list: list , actual_point: Point, other_points: list, min_distance: float = MAX_FLOAT, point_1: Point = Point(0,0), point_2: Point = Point(0,0)) -> tuple:
    if (len(copy_point_list) == 0) and (len(other_points) == 0):
        #   Não há mais elementos totais para calcular -->  Resultado Final
        return (point_1, point_2, min_distance)
    elif len(other_points) == 0:
        #   Não há elementos parciaias para calcular --> Atualizar 'copy_point_list', 'actual_point' e 'other_points'
        return shortestEuclidianDistance(tail(copy_point_list), head(copy_point_list), tail(copy_point_list), min_distance, point_1, point_2)
    elif min_distance >= hypotenuse(actual_point, head(other_points)):
        #   Distância Menor --> Atualizar 'other_points' 'min_distance', 'point_1' e 'point_2'
        return shortestEuclidianDistance(copy_point_list, actual_point, tail(other_points), hypotenuse(actual_point, head(other_points)), actual_point, head(other_points))   
    else:
        # not(Distância Menor) --> Atualizar 'other_points'
        return shortestEuclidianDistance(copy_point_list, actual_point, tail(other_points), min_distance, point_1, point_2)

#   Némeros Int Aleatórios   
def generateRandomPoints() -> Point:
    return Point(random.randint(0, 100), random.randint(0, 100))

def printCoordinates(coord_list: list) -> None:
    for i in range(NUM_POINTS):
        print(f"Ponto 0{i+1}: ({coord_list[i].x}, {coord_list[i].y})")

#   Cria uma list(Point)
coord_list = [generateRandomPoints() for _ in range (NUM_POINTS)]

#   Resultado Final
result = shortestEuclidianDistance(tail(coord_list), head(coord_list), tail(coord_list))

#   Imprimir Pontos
print("-"*10)
printCoordinates(coord_list)
print("-"*10)

#   Imprimir Resultado Final
print(f"\nPonto I: ({result[0].x}, {result[0].y})")
print(f"Ponto II: ({result[1].x}, {result[1].y})")
print(f"Distância: {result[2]}")