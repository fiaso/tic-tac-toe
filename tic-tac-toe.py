cols = 'a', 'b', 'c', 'd', 'e'
tokens = 'X', 'O'

def draw_board(board: []):
    """Draw board NxN"""
    line = '   '
    endline = '\t'
    for i in range(N):
        line = ''.join([line, '\t  ', cols[i]])
        endline = endline + '----'
    print(line)
    for i in range(N):
        line = str(i+1) + '\t'
        for j in range(N):
            if board[i][j] not in tokens: line = ''.join([line, '\t', '|'])
            else: line = ''.join([line, ' ', board[i][j], '\t', '|'])
        line = line[0:-1]
        print(line)
        if i != N-1: print(endline)

def take_answer(N: int)->(int, int):
    """Take answer from player"""
    print('Введите букву столбца и номер строки ячейки:')
    answer = input()
    if len(answer) != 2:
        return take_answer(N)
    elif answer[0] not in cols:
        return take_answer(N)
    elif int(answer[1])-1 not in range(N):
        return take_answer(N)
    raw = int(answer[1])-1
    col = -1
    for i in range(N):
        if answer[0] == cols[i]:
            col = i
            break
    return raw, col

def player_move(board: [], token: str, N: int):
    """Take answer and try put it in array"""
    raw, col = take_answer(N)
    if str(board[raw][col]) not in tokens:
        board[raw][col] = token
        return
    else:
        print('Эта клетка занята')
        return player_move(board, token, N)

def print_win(win: bool, token: str)->bool:
    """Print message if win"""
    if win:
        if token == 'X':
            print('Игрок 1 выиграл')
        elif token == 'O':
            print('Игрок 2 выиграл')
        else: return False
        return True
    else: return False

def check_win(board: [], N: int)->bool:
    """Check win somebody or not"""
    # raws
    for i in range(N):
        win = True
        token = board[i][0]
        for j in range(1,N):
            if board[i][j] != token:
                win = False
                break
            else: win = True
        if print_win(win, token): return True
    # cols
    for i in range(N):
        win = True
        token = board[0][i]
        for j in range(1,N):
            if board[j][i] != token:
                win = False
                break
        if print_win(win, token): return True
    # diagonal l-r
    win = True
    token = board[0][0]
    for i in range(1, N):
        if board[i][i] != token:
            win = False
            break
        else: win = True
    if print_win(win, token): return True
    # diagonal r-l
    win = True
    token = board[0][N - 1]
    for i in range(1, N):
        if board[i][N - 1 - i] != token:
            win = False
            break
        else: win = True
    if print_win(win, token): return True
    return False

if __name__ == '__main__':
    N = 0
    while N not in range(3, 6):
        print('\nВыберите размер поля от 3 до 5:\n')
        N = int(input())
    board = []
    for i in range(N):
        board.append([])
        for j in range(N):
            board[i].append(i + j)
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            print('Ход игрока 1')
            player_move(board, 'X', N)
        else:
            print('Ход игрока 2')
            player_move(board, 'O', N)
        if counter >= N*2-2:
            win = check_win(board, N)
            if win: break
        if counter == N*N-1:
            print("Ничья")
            break
        counter += 1
    draw_board(board)
