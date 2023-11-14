import copy

class Nodo:
    def __init__(self, tabuleiro: list, x: int, y: int, num_mov: int) -> None:
        self.tabuleiro = tabuleiro
        self.x = x
        self.y = y
        self.num_mov = num_mov
        self.mov_x = 1, -1, -2, -2, -1, 1, 2, 2
        self.mov_y = 2, 2, 1, -1, -2,-2, 1, -1
        self.prox_mov = []
    
    def e_valido(self, prox_x: int, prox_y: int) -> bool:
        return 0 <= prox_x < len(self.tabuleiro) and 0 <= prox_y < len(self.tabuleiro)
    
    def resolver_passeio_cavaleiro(self) -> bool:
        if self.num_mov == (pow(len(self.tabuleiro), 2) + 1):
            imprimir_tabuleiro(self.tabuleiro)
            return True
        for movimentos in range(8):
            prox_mov_x = self.x + self.mov_x[movimentos]
            prox_mov_y = self.y + self.mov_y[movimentos]
            if self.e_valido(prox_mov_x, prox_mov_y):
                if self.tabuleiro[prox_mov_x][prox_mov_y] == -1:
                    tabuleiro_copia = copy.deepcopy(self.tabuleiro)
                    tabuleiro_copia[prox_mov_x][prox_mov_y] = self.num_mov
                    self.prox_mov.append(Nodo(tabuleiro_copia, prox_mov_x, prox_mov_y, self.num_mov + 1))
        
        for movimentos in self.prox_mov:
            if movimentos.resolver_passeio_cavaleiro():
                return True
        return False
        

def criar_tubuleiro(tamanho_tabuleiro: int) -> list:
    return [[-1 for _ in range(tamanho_tabuleiro)] for _ in range(tamanho_tabuleiro)]

def imprimir_tabuleiro(tabuleiro: list) -> None:
    for linha in tabuleiro:
        print(linha)
        # print(" ".join(linha))
    print("\n---------\n")

def validar_posicao_inicial(tamanho_tabuleiro: int, valor: int) -> int:
    while (valor < 0) or (valor >= tamanho_tabuleiro):
        valor = int(input("Informe um valor válido na posição: "))
    return valor

def passeio_cavaleiro(tamanho_tabuleiro: int, pos_init_x: int, pos_init_y: int) -> bool:
    tabuleiro = criar_tubuleiro(tamanho_tabuleiro)
    tabuleiro[pos_init_x][pos_init_y] = 1
    raiz = Nodo(tabuleiro, pos_init_x, pos_init_y, 2)
    return raiz.resolver_passeio_cavaleiro()

#   EXECUTAR
tamanho_tabuleiro = int(input("INFORME O TAMANHO DO LADO DO TABULEIRO: "))
pos_x = validar_posicao_inicial(tamanho_tabuleiro, int(input("POSICAO EM X: ")))
pos_y = validar_posicao_inicial(tamanho_tabuleiro, int(input("POSICAO EM Y: ")))

resultado = passeio_cavaleiro(tamanho_tabuleiro, pos_x, pos_y)
if not resultado:
    print("NÃO HÁ SOLUÇÃO")