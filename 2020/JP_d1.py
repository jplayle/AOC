_input = """"""

from itertools import combinations

# PART 1
print([x*y for x, y in combinations([int(n) for n in _input.split('\n')], 2) if x + y == 2020][0])

# PART 2
print([x*y*z for x, y, z in combinations([int(n) for n in _input.split('\n')], 3) if x + y + z == 2020][0])
























