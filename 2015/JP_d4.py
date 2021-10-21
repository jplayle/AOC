from hashlib import md5

got_answer = False
x = 0
i = "ckczppom"

# PART 1
while not got_answer:
	hash_str = i + str(x)
	h = md5(hash_str.encode('utf-8')).hexdigest()
	if h[:5] == "00000":
		print("PART 1 ANSWER:", x)
		got_answer = True
	x += 1
	
	
# PART 2
got_answer = False
x = 0
while not got_answer:
	hash_str = i + str(x)
	h = md5(hash_str.encode('utf-8')).hexdigest()
	if h[:6] == "000000":
		print("PART 2 ANSWER:", x)
		got_answer = True
	x += 1