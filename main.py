from src import GAME_BOARD, clear_console, GameBoard, get_move
from src.pieces import can_move

board = GameBoard()


def draw_board():
    clear_console()
    flatten = [item for sublist in board.pieces for item in sublist]
    print(GAME_BOARD % tuple(flatten))


if __name__ == '__main__':
    err = ''

    while 1:
        draw_board()
        print('    Turn: ' + ('WHITE' if board.white_turn else 'BLACK'))
        print()
        print('  ' + err)
        piece_xy = get_move('  SELECT')
        piece = board.get_piece(piece_xy)

        if piece[0] == ' ':
            err = 'EMPTY CHESS'
            continue

        if piece[1] != board.white_turn:
            err = 'NOT YOUR CHESS'
            continue

        print(f'  SELECTED {piece[0]}')

        move_xy = get_move('  MOVE')

        if not can_move(piece[0], piece_xy, move_xy, board.pieces):
            err = 'INVALID MOVE'
            continue

        board.move_chess(piece_xy, move_xy)

        err = ''
