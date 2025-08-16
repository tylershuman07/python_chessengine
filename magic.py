import numpy as np
from board import *
from attacks import *
# generate 32 bit pseudo legal numbers

def xor_shift32():
    number = np.uint32(1804289383)
    
    while True:
        number ^= number << 13
        number ^= number >> 17
        number ^= number << 5
        yield number

# generate 64 bit pseudo legal numbers

def xor_shift64():
    gen = xor_shift32()
    while True:
        n1 = np.uint64(next(gen)) & 0xFFFF
        n2 = np.uint64(next(gen)) & 0xFFFF
        n3 = np.uint64(next(gen)) & 0xFFFF
        n4 = np.uint64(next(gen)) & 0xFFFF
        yield n1 | (n2 << 16) | (n3 << 32) | (n4 << 48)


# generates the candidates for the magic numbers
def genMagicNumber():
    gen = xor_shift64()
    while True:
        yield (next(gen) & next(gen) & next(gen))

# function for finding the magic numbers

# def findMagicNumber(sq: int, relevantBits: int, bishop: int):
#     occupancies = []
#     attacks = []
#     usedAttacks = []

#     # get attack mask depending on if piece is rook or bishop
#     if bishop:
#         attackMask = maskBishopAttacks(sq)
#     else:
#         attackMask = maskRookAttacks(sq)

#     # initialize occupancy indicies
#     occupancyIndices = np.uint64(1) << relevantBits

#     # loop over occupancy indices
#     for i in range(occupancyIndices):
#         occupancies[i] = setOccupancy(i, relevantBits, attackMask)

#         if bishop:
#             attacks[i] = otfBishopAttacks(sq, occupancies[i])
#         else:
#             attacks[i] = otfRookAttacks(sq, occupancies[i])
    
#     # test magic numbers
#     gen = genMagicNumber()
#     for randCount in range(100000000):
#         # generate magic number candidate
#         magicNumber = next(gen)

#         # skip inappropriate magic numbers
#         if (attackMask*magicNumber &  0xFF00000000000000).bit_count() < 6:
#             continue
#         for i
        