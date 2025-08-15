from board import *
from attacks import *
import warnings
warnings.filterwarnings("ignore", "^overflow encountered in scalar negative", category=RuntimeWarning)

board = Board()
initKingAttacks()

# for sq in range(64):
#     printbb(otfBishopAttacks(sq,1))
block = setBit(np.uint64(0), d2)
block = setBit(block, d5)
block = setBit(block, f4)
block = setBit(block, a4)
print(block.bit_count())
print(getLsbIndex(block))
printbb(-block)