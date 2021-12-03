

""" FIRST PASS - INITIAL SOLUTION """
counts = {n: {"1": 0, "0":0} for n in range(12)}

numbers = txt.split("\n")

for l in numbers:
    for n in range(12):
        counts[n][l[n]] += 1
        
gamma   = ""
epsilon = ""
for i, c in counts.items():
    if c["1"] > c["0"]:
        gamma   += "1"
        epsilon += "0"
    else:
        gamma    += "0"
        epsilon += "1"
        
print(int(gamma, 2) * int(epsilon, 2))

""" PART 2 """
def oxygen_rating(pos, number_list):
    if len(number_list) == 1:
        return number_list[0]
    ones  = [n for n in number_list if n[pos] == "1"]
    zeros = [n for n in number_list if n[pos] == "0"]
    if len(ones) >= len(zeros):
        o_r = oxygen_rating(pos + 1, ones)
    else:
        o_r = oxygen_rating(pos + 1, zeros)
        
    return o_r
    
def CO2_scrubber(pos, num_list):
    if len(num_list) == 1:
        return num_list[0]
    ones  = [n for n in num_list if n[pos] == "1"]
    zeros = [n for n in num_list if n[pos] == "0"]
    if len(ones) < len(zeros):
        c_s = CO2_scrubber(pos + 1, ones)
    else:
        c_s = CO2_scrubber(pos + 1, zeros)
        
    return c_s
        
print(int(oxygen_rating(0, numbers), 2) * int(CO2_scrubber(0, numbers), 2))
