lights = {x: {y: "off" for y in range(1000)} for x in range(1000)}

for l in txt.split("\n"):
    fields = l.split(" ")
    if fields[0] == "toggle":
        c1 = fields[1].split(",")
        c2 = fields[3].split(",")
        for x in range(int(c1[0]), int(c2[0]) + 1):
            for y in range(int(c1[1]), int(c2[1]) + 1):
                if lights[x][y] == "on":
                    lights[x][y] = "off"
                else:
                    lights[x][y] = "on"
    else:
        c1 = fields[2].split(",")
        c2 = fields[4].split(",")
        for x in range(int(c1[0]), int(c2[0]) + 1):
            for y in range(int(c1[1]), int(c2[1]) + 1):
                lights[x][y] = fields[1]

lit = 0  
for x in range(1000):
    for y in range(1000):
        if lights[x][y] == "on":
            lit += 1
            
print(lit)


# PART 2
lights = {x: {y: 0 for y in range(1000)} for x in range(1000)}

for l in txt.split("\n"):
    fields = l.split(" ")
    if fields[0] == "toggle":
        c1 = fields[1].split(",")
        c2 = fields[3].split(",")
        for x in range(int(c1[0]), int(c2[0]) + 1):
            for y in range(int(c1[1]), int(c2[1]) + 1):
                lights[x][y] += 2
    else:
        c1 = fields[2].split(",")
        c2 = fields[4].split(",")
        for x in range(int(c1[0]), int(c2[0]) + 1):
            for y in range(int(c1[1]), int(c2[1]) + 1):
                if fields[1] == "on":
                    lights[x][y] += 1
                elif lights[x][y] > 0:
                    lights[x][y] -= 1

brightness = 0  
for x in range(1000):
    for y in range(1000):
        brightness += lights[x][y]
            
print(brightness)
