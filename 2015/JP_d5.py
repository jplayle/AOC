txt = """"""

# PART 1
n_nice = 0
vowels = ['a', 'e', 'i', 'o', 'u']
bad_s  = ['ab', 'cd', 'pq', 'xy']
for l in txt.split("\n"):
    nice = False
    
    skip = False
    for s in bad_s:
        if s in l:
            skip = True
            break
    if skip:
        continue
    
    v_count = 0
    for v in vowels:
        if v in l:
            v_count += l.count(v)
            
    for x in range(len(l) - 1):
        if l[x:x+2][0] == l[x:x+2][1]:
            nice = True
            break
            
    if nice and v_count >= 3:
        n_nice += 1
        
print(n_nice)

# PART 2
n_nice = 0
for l in txt.split("\n"):
    crit_1 = False
    for x in range(len(l) - 1):
        pair = l[x:x+2]
        r1 = l[:l.find(pair)]
        r2 = l[l.find(pair)+2:]
        if pair in r1 or pair in r2:
            crit_1 = True
            break
            
    crit_2 = False
    for x in range(len(l) - 1):
        trip = l[x:x+3]
        if len(trip) < 3:
            continue
        if trip[0] == trip[2]:
            crit_2 = True
            break
            
    if crit_1 and crit_2:
        n_nice += 1
        
print(n_nice)