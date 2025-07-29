board = [' '] * 9

def print_board():
    print()
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print()

def check_winner(player):
    win_positions = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8],  
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8],  
        [0, 4, 8],  
        [2, 4, 6]   
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def jogar():
    # Pedir nomes dos jogadores
    nome_jogador_X = input("Digite o nome do jogador que será 'X': ")
    nome_jogador_O = input("Digite o nome do jogador que será 'O': ")
    
    current_player = 'X'  
    for turn in range(9):  
        print_board()

        while True:
            try:
                if current_player == 'X':
                    move = int(input(f'{nome_jogador_X} ({current_player}), escolha uma posição (1-9): ')) - 1
                else:
                    move = int(input(f'{nome_jogador_O} ({current_player}), escolha uma posição (1-9): ')) - 1
                
                if 0 <= move <= 8 and board[move] == ' ':
                    board[move] = current_player
                    break
                else:
                    print("Posição inválida ou ocupada. Tente de novo.")
            except ValueError:
                print("Digite um número de 1 a 9.")

        if check_winner(current_player):
            print_board()
            if current_player == 'X':
                print(f'🎉 Parabéns, {nome_jogador_X}! Você venceu!')
            else:
                print(f'🎉 Parabéns, {nome_jogador_O}! Você venceu!')
            return

        current_player = 'O' if current_player == 'X' else 'X'

    print_board()
    print("😐 Empate!")

jogar()
