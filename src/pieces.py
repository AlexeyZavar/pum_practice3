from typing import List

from .consts import *
from .utils import calc_xy


def can_move(piece: str, piece_xy: str, move_xy: str, pieces: List[List[str]]):
    stage1 = can_move_stage1(piece, piece_xy, move_xy)
    if not stage1:
        return False

    return can_move_stage2(piece, piece_xy, move_xy, pieces)


def can_move_stage2(piece: str, piece_xy: str, move_xy: str, pieces: List[List[str]]):
    return True


def can_move_stage1(piece: str, piece_xy: str, move_xy: str):
    y1, x1 = calc_xy(piece_xy)
    y2, x2 = calc_xy(move_xy)

    if piece == BLACK_PAWN:
        if y1 == 1 and y2 in [2, 3] and x1 == x2:
            return True

        if y2 - y1 == 1 and x1 == x2:
            return True

        return False
    elif piece == WHITE_PAWN:
        if y1 == 6 and y2 in [5, 4] and x1 == x2:
            return True

        if y1 - y2 == 1 and x1 == x2:
            return True

        return False
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
