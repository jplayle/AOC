_input = """"""

valid = 0
for l in _input.split("\n"):
    fields = l.split(" ")
    rang   = fields[0].split("-")
    rang_0 = int(rang[0])
    rang_1 = int(rang[1])
    ch     = fields[1].replace(":", "")
    txt    = fields[-1]
    n      = txt.count(ch)
    if n >= rang_0 and n <= rang_1:
        valid += 1
        
print(valid)

# PART 2
valid = 0
for l in _input.split("\n"):
    fields = l.split(" ")
    rang   = fields[0].split("-")
    rang_0 = int(rang[0]) - 1
    rang_1 = int(rang[1]) - 1
    ch     = fields[1].replace(":", "")
    txt    = fields[-1]
    if txt[rang_0] == ch and txt[rang_1] != ch:
        valid += 1
    elif txt[rang_1] == ch and txt[rang_0] != ch:
        valid += 1
        
print(valid)
























