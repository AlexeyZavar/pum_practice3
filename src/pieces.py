from .consts import *
from .utils import calc_xy


def can_move(piece: str, piece_xy: str, move_xy: str):
    x1, y1 = calc_xy(piece_xy)
    x2, y2 = calc_xy(move_xy)

    if piece == BLACK_PAWN or piece == WHITE_PAWN:
        return x1 == x2 and y1 != 1 and ((y1 == 2 and y1 + 2 == y2) or y1 + 1 == y2)
    elif piece == BLACK_ROOK or piece == WHITE_ROOK:
        return x1 == x2 or y1 == y2
    elif piece == BLACK_KING or piece == WHITE_KING:
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
    elif piece == BLACK_BISHOP or piece == WHITE_BISHOP:
        return abs(x1 - x2) == abs(y1 - y2)
    elif piece == BLACK_QUEEN or piece == WHITE_QUEEN:
        return abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2
    elif piece == BLACK_KNIGHT or piece == WHITE_KNIGHT:
        t1 = abs(x1 - x2)
        t2 = abs(y1 - y2)

        return (t1 == 1 and t2 == 2) or (t1 == 2 and t2 == 1)
    else:
        print(piece)
        raise Exception()
