txt = """"""

numbers = txt.split("\n")


""" PART 1 """
g = int("".join(["1" if y > 0 else "0" for y in [sum([1 if x == "1" else -1 for x in [n[pos] for n in numbers]]) for pos in range(12)]]), 2)
e = int("".join(["1" if y < 0 else "0" for y in [sum([1 if x == "1" else -1 for x in [n[pos] for n in numbers]]) for pos in range(12)]]), 2)

print(g * e)


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
    
def co2_scrubber(pos, num_list):
    if len(num_list) == 1:
        return num_list[0]
    ones  = [n for n in num_list if n[pos] == "1"]
    zeros = [n for n in num_list if n[pos] == "0"]
    if len(ones) < len(zeros):
        c_s = co2_scrubber(pos + 1, ones)
    else:
        c_s = co2_scrubber(pos + 1, zeros)
        
    return c_s
        
print(int(oxygen_rating(0, numbers), 2) * int(CO2_scrubber(0, numbers), 2))
