txt = """"""

vals = {"forward": 0, "up": 0, "down": 0, "depth2": 0}
fmap = {"forward": lambda n : (vals["down"] - vals["up"]) * n, "up": lambda n : 0, "down": lambda n : 0}

for l in txt.split("\n"):
    ins, val = l.split(" ")[0], int(l.split(" ")[1])
    vals[ins] += val
    vals["depth2"] += fmap[ins](val)
    
print(vals["forward"] * (vals["down"] - vals["up"]))
print(vals["forward"] * vals["depth2"])
