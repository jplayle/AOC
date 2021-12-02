# not exactly computationally efficient but does make the final calculation a nice one-liner:
F = sum([int(l.split(" ")[1]) for l in txt.split("\n") if "forward" in l])
U = sum([int(l.split(" ")[1]) for l in txt.split("\n") if "down" in l])
D = sum([int(l.split(" ")[1]) for l in txt.split("\n") if "up" in l])
print(F * (U - D))


""" ¯\_(ツ)_/¯ """
fwd, dep1, dep2 = 0, 0, 0

def u(n):
    global dep1
    dep1 -= n
def d(n):
    global dep1
    dep1 += n
def f(n):
    global fwd, dep2
    fwd  += n
    dep2 += n * dep1
    
func_map = {"up": u, "down": d, "forward": f}

for t in txt.split("\n"):
    inp = t.split(" ")
    func_map[inp[0]](int(inp[1]))
    
print(fwd * dep1)
print(fwd * dep2) 



""" QUICK N' DIRTY!!! """
fwd = 0
dep = 0
aim = 0
for t in txt.split("\n"):
    ins = t.split(" ")
    if ins[0] == "forward":
        fwd += int(ins[1])
    elif ins[0] == "up":
        dep -= int(ins[1])
    else:
        dep += int(ins[1])
        
print(fwd * dep)

fwd = 0
dep = 0
aim = 0

for t in txt.split("\n"):
    ins = t.split(" ")
    if ins[0] == "forward":
        fwd += int(ins[1])
        dep += int(ins[1]) * aim
    elif ins[0] == "up":
        aim -= int(ins[1])
    else:
        aim += int(ins[1])
    
print(fwd * dep)
