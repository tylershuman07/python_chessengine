import numpy as np
white, black = 0, 1

a1, b1, c1, d1, e1, f1, g1, h1, \
a2, b2, c2, d2, e2, f2, g2, h2, \
a3, b3, c3, d3, e3, f3, g3, h3, \
a4, b4, c4, d4, e4, f4, g4, h4, \
a5, b5, c5, d5, e5, f5, g5, h5, \
a6, b6, c6, d6, e6, f6, g6, h6, \
a7, b7, c7, d7, e7, f7, g7, h7, \
a8, b8, c8, d8, e8, f8, g8, h8 = \
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \
10, 11, 12, 13, 14, 15, 16, 17, \
18, 19, 20, 21, 22, 23, 24, 25, \
26, 27, 28, 29, 30, 31, 32, 33, \
34, 35, 36, 37, 38, 39, 40, 41, \
42, 43, 44, 45, 46, 47, 48, 49, \
50, 51, 52, 53, 54, 55, 56, 57, \
58, 59, 60, 61, 62, 63
'''
a-file             0x0101010101010101
h-file             0x8080808080808080
1st rank           0x00000000000000FF
8th rank           0xFF00000000000000
a1-h8 diagonal     0x8040201008040201
h1-a8 antidiagonal 0x0102040810204080
light squares      0x55AA55AA55AA55AA
dark squares       0xAA55AA55AA55AA55
'''
notAfile = 0xfefefefefefefefe
notHfile = 0x7f7f7f7f7f7f7f7f
notABfile = np.uint64(18229723555195321596)
notHGfile = np.uint64(4557430888798830399)
class Board():
    def __init__(self):
        self.wP_bitboard = np.uint64(0)
        self.wN_bitboard = np.uint64(0)
        self.wB_bitboard = np.uint64(0)
        self.wR_bitboard = np.uint64(0)
        self.wQ_bitboard = np.uint64(0)
        self.wK_bitboard = np.uint64(0)

        self.bP_bitboard = np.uint64(0)
        self.bN_bitboard = np.uint64(0)
        self.bB_bitboard = np.uint64(0)
        self.bR_bitboard = np.uint64(0)
        self.bQ_bitboard = np.uint64(0)
        self.bK_bitboard = np.uint64(0)

        self.init_pieces()

        self.bitboards = [self.wP_bitboard, 
                          self.wN_bitboard,
                          self.wB_bitboard,
                          self.wR_bitboard,
                          self.wQ_bitboard,
                          self.wK_bitboard,
                          self.bP_bitboard, 
                          self.bN_bitboard,
                          self.bB_bitboard,
                          self.bR_bitboard,
                          self.bQ_bitboard,
                          self.bK_bitboard]

    def init_pieces(self): #Sets the starting state of the board
        self.wP_bitboard = 0x000000000000FF00
        self.wN_bitboard = sq64tobb(b1) | sq64tobb(g1)
        self.wB_bitboard = sq64tobb(c1) | sq64tobb(f1)
        self.wR_bitboard = sq64tobb(a1) | sq64tobb(h1)
        self.wQ_bitboard = sq64tobb(d1)
        self.wK_bitboard = sq64tobb(e1)

        self.bP_bitboard = 0x00FF000000000000
        self.bN_bitboard = sq64tobb(b8) | sq64tobb(g8)
        self.bB_bitboard = sq64tobb(c8) | sq64tobb(f8)
        self.bR_bitboard = sq64tobb(a8) | sq64tobb(h8)
        self.bQ_bitboard = sq64tobb(d8)
        self.bK_bitboard = sq64tobb(e8)

    def get_occupied_squares(self):
        return self.wP_bitboard | \
        self.wN_bitboard | \
        self.wB_bitboard | \
        self.wR_bitboard | \
        self.wQ_bitboard | \
        self.wK_bitboard | \
        self.bP_bitboard | \
        self.bN_bitboard | \
        self.bB_bitboard | \
        self.bR_bitboard | \
        self.bQ_bitboard | \
        self.bK_bitboard

def printbb(bb):
    myStr = str(format(bb, '064b'))
    for rank in range(8):
        print(8 - rank,end = " ")
        for file in range(7,-1,-1):
            print(" " + myStr[rank*8 + file] + " ", end = '')
        print()
    print("   a  b  c  d  e  f  g  h")
    print()

def shiftN(bb):
    return (bb << 8)
def shiftNE(bb):
    return (bb << 9) & notAfile
def shiftE(bb):
    return (bb << 1) & notAfile
def shiftSE(bb):
    return (bb >> 7) & notAfile
def shiftS(bb):
    return (bb >> 8)
def shiftSW(bb):
    return (bb >> 9) & notHfile
def shiftW(bb):
    return (bb >> 1) & notHfile
def shiftNW(bb):
    return (bb << 7) & notHfile
    
    
def setBit(bb, sq64):
    return (bb | (np.uint64(1) << sq64))
def popBit(bb, sq64):
    return (bb ^ (np.uint64(1) << sq64))
def testBit(bb, sq64):
    if bb & (np.uint64(1) << sq64):
        return True
    else:
        return False

# gets the index of the least significant bit of a bitboard
def getLsbIndex(bb):
    
    # make sure bitboard has a LSB
    if bb:
        # count trailing bits before LSB
        bb = ((bb & -bb)-1)
        return bb.bit_count()
    else:
        return -1


def sq64tobb(sq64):
    return np.uint64(1) << sq64

    
    
