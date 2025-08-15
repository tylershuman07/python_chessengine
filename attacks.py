import numpy as np
from board import *
# Pawn attacks table
pawnAttacks = [[],[]]

# Knight attacks table
knightAttacks = []

# King attacks table
kingAttacks = []

def maskPawnAttacks(side, sq64):
    bitboard = np.uint64(0)
    bitboard = setBit(bitboard, sq64)
    if side != True:
        attacks = shiftNE(bitboard) | shiftNW(bitboard)
    else:
        attacks = shiftSE(bitboard) | shiftSW(bitboard)
    return attacks

def maskKnightAttacks(sq64):
    bitboard = np.uint64(0)
    bitboard = setBit(bitboard, sq64)
    attacks = shiftE(shiftNE(bitboard)) | shiftN(shiftNE(bitboard)) | \
    shiftE(shiftSE(bitboard)) | shiftS(shiftSE(bitboard)) | \
    shiftW(shiftNW(bitboard)) | shiftN(shiftNW(bitboard)) | \
    shiftW(shiftSW(bitboard)) | shiftS(shiftSW(bitboard))
    return attacks

def maskKingAttacks(sq64):
    bitboard = np.uint64(0)
    bitboard = setBit(bitboard, sq64)
    attacks = shiftN(bitboard) | shiftNE(bitboard) | \
    shiftE(bitboard) | shiftSE(bitboard) | \
    shiftS(bitboard) | shiftSW(bitboard) | \
    shiftW(bitboard) | shiftNW(bitboard)
    return attacks

def maskBishopAttacks(sq):
    tarRank = int(sq / 8)
    tarFile = int(sq % 8)
    attacks = np.uint64(0)

    # mask relevant occupancy squares
    for r,f in zip(range(tarRank + 1, 7, 1), range(tarFile + 1, 7, 1)):
        attacks = attacks | np.uint64(1) << ((8*r) + f)
    for r,f in zip(range(tarRank - 1, 0, -1), range(tarFile - 1, 0, -1)):
        attacks = attacks | np.uint64(1) << ((8*r) + f)
    for r,f in zip(range(tarRank - 1, 0, -1), range(tarFile + 1, 7, 1)):
        attacks = attacks | np.uint64(1) << ((8*r) + f)
    for r,f in zip(range(tarRank + 1, 7, 1), range(tarFile - 1, 0, -1)):
        attacks = attacks | np.uint64(1) << ((8*r) + f)
    return attacks

def maskRookAttacks(sq):
    tarRank = int(sq / 8)
    tarFile = int(sq % 8)
    attacks = np.uint64(0)

    # mask relevant occupancy squares
    for r in range(tarRank + 1, 7, 1):
        attacks = attacks | np.uint64(1) << ((8*r) + tarFile)
    for r in range(tarRank - 1, 0, -1):
        attacks = attacks | np.uint64(1) << ((8*r) + tarFile)
    for f in range(tarFile + 1, 7, 1):
        attacks = attacks | np.uint64(1) << ((8*tarRank) + f)
    for f in range(tarFile - 1, 0, -1):
        attacks = attacks | np.uint64(1) << ((8*tarRank) + f)
    return attacks

def otfBishopAttacks(sq, block):
    tarRank = int(sq / 8)
    tarFile = int(sq % 8)
    attacks = np.uint64(0)

    # Generate bishop attacks
    for r,f in zip(range(tarRank + 1, 8, 1), range(tarFile + 1, 8, 1)):
        attacks = attacks | np.uint64(1) << ((8*r) + f)
        if (np.uint64(1) << ((8*r) + f)) & block:
            break
    for r,f in zip(range(tarRank - 1, -1, -1), range(tarFile - 1, -1, -1)):
        attacks = attacks | np.uint64(1) << ((8*r) + f)
        if (np.uint64(1) << ((8*r) + f)) & block:
            break
    for r,f in zip(range(tarRank - 1, -1, -1), range(tarFile + 1, 8, 1)):
        attacks = attacks | np.uint64(1) << ((8*r) + f)
        if (np.uint64(1) << ((8*r) + f)) & block:
            break
    for r,f in zip(range(tarRank + 1, 8, 1), range(tarFile - 1, -1, -1)):
        attacks = attacks | np.uint64(1) << ((8*r) + f)
        if (np.uint64(1) << ((8*r) + f)) & block:
            break
    return attacks

def otfRookAttacks(sq, block):
    tarRank = int(sq / 8)
    tarFile = int(sq % 8)
    attacks = np.uint64(0)

    # Generate rook attacks
    for r in range(tarRank + 1, 8, 1):
        attacks = attacks | np.uint64(1) << ((8*r) + tarFile)
        if (np.uint64(1) << ((8*r) + tarFile)) & block:
            break
    for r in range(tarRank - 1, -1, -1):
        attacks = attacks | np.uint64(1) << ((8*r) + tarFile)
        if (np.uint64(1) << ((8*r) + tarFile)) & block:
            break
    for f in range(tarFile + 1, 8, 1):
        attacks = attacks | np.uint64(1) << ((8*tarRank) + f)
        if (np.uint64(1) << ((8*tarRank) + f)) & block:
            break
    for f in range(tarFile - 1, -1, -1):
        attacks = attacks | np.uint64(1) << ((8*tarRank) + f)
        if (np.uint64(1) << ((8*tarRank) + f)) & block:
            break
    return attacks

def initPawnAttacks():
    for sq in range(64):
        pawnAttacks[white].append(maskPawnAttacks(white,sq))
        pawnAttacks[black].append(maskPawnAttacks(black,sq))

def initKnightAttacks():
    for sq in range(64):
        knightAttacks.append(maskKnightAttacks(sq))

def initKingAttacks():
    for sq in range(64):
        kingAttacks.append(maskKingAttacks(sq))
            