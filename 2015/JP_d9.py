txt = """Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127"""

from itertools import permutations

nodes = []
legs  = {}

for l in txt.split("\n"):
	f = l.split(" ")
	nodes += [f[0]]
	nodes += [f[2]]
	d = int(f[-1])
	if f[0] not in legs:
		legs[f[0]] = {}
	legs[f[0]][f[2]] = d
	
nodes  = set(nodes)
paths  = list(permutations(nodes))
path_L = len(paths[0])

distances = []

for p in paths:
	d = 0
	for x in range(path_L - 1):
		A = p[x]
		B = p[x + 1]
		if A in legs:
			if B in legs[A]:
				d += legs[A][B]
			else:
				d += legs[B][A]
		else:
			d += legs[B][A]
				
	if d:
		distances += [d]

# PART 1
print(min(distances))

# PART 2
print(max(distances))