




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
