txt = """"""

numbers = [int(x) for x in txt.split("\n")]

pos_only = lambda n : n & -(0 < n)
one_only = lambda n : ((n | (~n + 1)) >> 31) & 1

print(sum([one_only(pos_only(numbers[n] - numbers[n-1])) for n in range(len(numbers))]))
print(sum([one_only(pos_only(numbers[n] - numbers[n-3])) for n in range(len(numbers))]))
