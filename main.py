from board import *
from attacks import *
from magic import *
import warnings
warnings.filterwarnings("ignore", "^overflow encountered in scalar negative", category=RuntimeWarning)

initAll()
board = Board()

occupancy = np.uint64(0)
occupancy = setBit(occupancy,f4)
occupancy = setBit(occupancy,d2)
occupancy = setBit(occupancy,d7)
occupancy = setBit(occupancy,b4)

printbb(occupancy)

printbb(getRookAttacks(d4,occupancy))