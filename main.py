from board import *
from attacks import *
import warnings
warnings.filterwarnings("ignore", "^overflow encountered in scalar negative", category=RuntimeWarning)

board = Board()

attackMask = maskRookAttacks(a1)
for index in range(5):
    printbb(setOccupancy(index, attackMask.bit_count(), attackMask))