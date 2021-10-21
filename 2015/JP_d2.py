
# convert input string to python list
boxes = [[int(b) for b in box.split("x")] for box in txt.split("\n")]

# STEP 1
total = 0
for b in boxes:
    a1 = b[0]*b[1]
    a2 = b[0]*b[2]
    a3 = b[1]*b[2]
    a  = [a1, a2, a3]
    total += (2 * sum(a)) + min(a)
    
print(total)

# STEP 2
ribbon = 0
for b in boxes:
    box = sorted(b) # two fingers to time complexity
    L1  = 2 * (box[0] + box[1])
    L2  = box[0] * box[1] * box[2]
    ribbon += L1 + L2
    
print(ribbon)  