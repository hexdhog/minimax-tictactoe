from math import sqrt, floor

SEED = 0.5 * (sqrt(5) - 1)

# Hash single integer value
# source: https://www.cs.hmc.edu/~geoff/classes/hmc.cs070.200101/homework10/hashfuncs.html
#
# :param value: interger value to hash
# :param size: number of bits in a word
# :param extract: number of bits to extract
# :return: hashed interger value
def hashval(value: int, size: int = 8, extract: int = 4) -> int:
    seed = floor(SEED * 2 ** size)
    return (value * seed) >> (size - extract)
