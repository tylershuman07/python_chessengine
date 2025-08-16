from board import *
from attacks import *
from magic import *
import warnings
warnings.filterwarnings("ignore", "^overflow encountered in scalar negative", category=RuntimeWarning)

initAll()
board = Board()