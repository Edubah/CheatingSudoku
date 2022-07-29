
def find_next_empty(puzzle):
    # encontra a próxima linha, coluna no quebra-cabeça que ainda não está preenchido
    # --> nós representamos estes com -1
    # retorna uma linha, col tuple (ou (Nenhum, Nenhum) se não houver nenhuma)

    #Deixando ESCURO que uso 0-8 para os índices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None #Se nenhum dos espaços estiverem vazios

def is_valid(puzzle, guess, row, col):
    # descobre se o palpite na linha/col do quebra-cabeça é um palpite válido
    # retorna Verdadeiro ou Falso

    #Começando pela linha:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #Agora as colunas:
    # col_vals = []
    # for i in range(9):
    # col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #Agora os quadrados
    # Esta parte é complicada, mas é preciso pegar onde o quadrado começa 3x3
    # retornar se existe uma solução
    row_start = (row // 3) * 3 #1 // 3 = 0, 5 // 3 = 1, ....
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # se chegarmos aqui, esses cheques passam
    return True

def solve_sudoku(puzzle):
    #Resolve o sudoku utilizando uma tecnica chamada Backtracking
    #nosso quebra-cabeça é uma lista de listas,
    #onde cada lista interna é uma linha em nosso quebra-cabeça sudoku
    #Retorna a solução

    # passo 1: escolha em algum lugar no quebra-cabeça para dar um palpite
    row, col = find_next_empty(puzzle)

    # passo 1.1: se não há mais nenhum, então estamos feitos porque só permitimos entradas válidas
    if row is None:
        return True

    #  passo 2: se há um lugar para colocar um número, em seguida, fazer um palpite entre 1 e 9
    for guess in range(1, 10):
        # passo 3: confira se este é um palpite válido
        if is_valid(puzzle, guess, row, col):
            # passo 3.1: se este é um palpite válido, em seguida, colocá-lo naquele ponto no quebra-cabeça
            puzzle[row][col] = guess
            # passo 4: então chamamos recursivamente nosso solucionador!
            if solve_sudoku(puzzle):
                return True


        # passo 5: não é válido ou se nada é devolvido verdadeiro, então precisamos voltar atrás e tentar um novo número
        puzzle[row][col] = -1 #Reseta o guess

    # passo 6: se nenhum dos números que tentamos trabalhar, então este quebra-cabeça é INSOLÚVEL!!
    return False



if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
