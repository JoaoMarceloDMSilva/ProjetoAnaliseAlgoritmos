#[derive(Clone)]
struct Nodo {
    tabuleiro: Vec<Vec<i32>>,
    x: usize,
    y: usize,
    num_mov: i32,
    mov_x: [i32; 8],
    mov_y: [i32; 8],
    prox_mov: Vec<Nodo>,
}

impl Nodo {
    fn new(tabuleiro: Vec<Vec<i32>>, x: usize, y: usize, num_mov: i32) -> Nodo {
        let mov_x = [1, -1, -2, -2, -1, 1, 2, 2];
        let mov_y = [2, 2, 1, -1, -2, -2, 1, -1];
        let prox_mov = Vec::new();
        Nodo {
            tabuleiro,
            x,
            y,
            num_mov,
            mov_x,
            mov_y,
            prox_mov,
        }
    }

    fn e_valido(&self, prox_x: i32, prox_y: i32) -> bool {
        (prox_x >= 0) && (prox_x < self.tabuleiro.len() as i32) && (prox_y >= 0) && (prox_y < self.tabuleiro.len() as i32)
    }

    fn imprimir_tabuleiro(&self) {
        for linha in &self.tabuleiro {
            println!("{:?}", linha);
        }
        println!("\n---------\n");
    }

    fn resolver_passeio_caveleiro(&mut self) -> bool {
        if self.num_mov == (self.tabuleiro.len() as i32).pow(2) + 1 {
            self.imprimir_tabuleiro();
            return true;
        }

        for movimentos in 0..8 {
            let prox_mov_x = self.x as i32 + self.mov_x[movimentos];
            let prox_mov_y = self.y as i32 + self.mov_y[movimentos];

            if self.e_valido(prox_mov_x, prox_mov_y) {
                if self.tabuleiro[prox_mov_x as usize][prox_mov_y as usize] == -1 {
                    let mut tabuleiro_copia = self.tabuleiro.clone();
                    tabuleiro_copia[prox_mov_x as usize][prox_mov_y as usize] = self.num_mov;
                    let novo_movimento = Nodo::new(tabuleiro_copia, prox_mov_x as usize, prox_mov_y as usize, self.num_mov + 1);
                    self.prox_mov.push(novo_movimento);
                }
            }
        }

        for movimento in &mut self.prox_mov {
            if movimento.resolver_passeio_caveleiro() {
                return true;
            }
        }

        false
    }
}

fn criar_tabuleiro(size: usize) -> Vec<Vec<i32>> {
    vec![vec![-1; size]; size]
}

fn validar_posicao_inicial(tamanho_tabuleiro: usize, valor: i32) -> i32 {
    let mut val = valor;

    while val < 0 || val >= tamanho_tabuleiro as i32 {
        println!("Informe um valor válido na posição:");

        let mut input = String::new();
        std::io::stdin().read_line(&mut input).expect("Failed to read line");

        val = input.trim().parse().unwrap_or(0);
    }

    val
}


fn passeio_cavaleiro(tamanho_tabuleiro: usize, pos_init_x: usize, pos_init_y: usize) -> bool {
    let mut tabuleiro = criar_tabuleiro(tamanho_tabuleiro);
    tabuleiro[pos_init_x][pos_init_y] = 1;
    let mut raiz = Nodo::new(tabuleiro, pos_init_x, pos_init_y, 2);
    raiz.resolver_passeio_caveleiro()
}

fn main() {
    println!("INFORME O TAMANHO DO LADO DO TABULEIRO: ");
    let mut tamanho_tabuleiro = String::new();
    std::io::stdin().read_line(&mut tamanho_tabuleiro).expect("Failed to read line");
    let tamanho_tabuleiro: usize = tamanho_tabuleiro.trim().parse().expect("Invalid input");

    println!("POSICAO EM X: ");
    let mut pos_x = String::new();
    std::io::stdin().read_line(&mut pos_x).expect("Failed to read line");
    let pos_x: usize = validar_posicao_inicial(tamanho_tabuleiro, pos_x.trim().parse().unwrap_or(0)) as usize;

    println!("POSICAO EM Y: ");
    let mut pos_y = String::new();
    std::io::stdin().read_line(&mut pos_y).expect("Failed to read line");
    let pos_y: usize = validar_posicao_inicial(tamanho_tabuleiro, pos_y.trim().parse().unwrap_or(0)) as usize;

    let resultado = passeio_cavaleiro(tamanho_tabuleiro, pos_x, pos_y);
    if !resultado {
        println!("NÃO HÁ SOLUÇÃO");
    }
}
