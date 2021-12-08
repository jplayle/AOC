txt = """"""

sigs  = [l.split(" | ") for l in txt.split("\n")]

p1 = sum([sum([1 for s in os[1].split(" ") if len(s) in [2, 3, 4, 7]]) for os in sigs])

print(p1)

""" PART 2 """
def seg_to_num(seg_list1=""):
	# matches the segments that are lit to a corresponding number
	seg_num_map = {
					"0": "t,tr,br,b,bl,tl",
					"1": "tr,br",
					"2": "t,tr,m,bl,b",
					"3": "t,tr,m,br,b",
					"4": "tl,m,tr,br",
					"5": "t,tl,m,br,b",
					"6": "t,tl,m,bl,br,m",
					"7": "t,tr,br",
					"8": "t,tr,tl,m,br,bl,b",
					"9": "t,tr,tl,m,br,b"
					}
					
	for int_str, seg_list2 in seg_num_map.items():
		n_seg_list1 = len(seg_list1.split(","))
		n_seg_list2 = len(seg_list2.split(","))
		if sum([1 for s in seg_list1.split(",") if s in seg_list2]) == n_seg_list2 and n_seg_list1 == n_seg_list2:
			return int_str
	
total = 0
for sig in sigs:
	_inputs = sig[0].split(" ")
	outputs = sig[1].split(" ")
	sig_map = {}
	
	right_side = [] # segments on the right
	left_side  = [] # segments on the left
	middle     = [] # candidates for the middle segment
	bottom     = [] # candidates for the bottom segment
	
	# find the right hand side:
	for seg_str in _inputs:
		if len(seg_str) == 2:
			right_side = [s for s in seg_str]
			
	# find the top:
	for seg_str in _inputs:
		if len(seg_str) == 3:
			top = [s for s in seg_str if s not in right_side][0]
			sig_map[top] = "t"
			
	# find candidates for the middle:
	# 2 candidates - one is the middle, the other is the top left
	for seg_str in _inputs:
		if len(seg_str) == 4:
			middle = [s for s in seg_str if s not in right_side]
			
	# find candidates for the bottom:
	# 2 candidates - one is the bottom, the other is the bottom left
	for seg_str in _inputs:
		if len(seg_str) == 7:
			bottom = [s for s in seg_str if s not in right_side and s not in middle and s != top]
			
	# find the middle and bottom:
	# if the length is 5 and the entire right hand side is present then it must be a 3
	# none of the left hand side is lit for a 3 so using that, the middle and bottom can be found
	for seg_str in _inputs:
		if len(seg_str) == 5:
			if sum([1 for s in right_side if s in seg_str]) == 2:
				m = [s for s in seg_str if s not in right_side and s != top and s in middle][0]
				b = [s for s in seg_str if s not in right_side and s != top and s in bottom and s != m][0]
				sig_map[m] = "m"
				sig_map[b] = "b"
	
	# top left and bottom left:
	# the remaining candidates in the middle and bottom candidates
	tl = [s for s in middle if s != m][0]
	bl = [s for s in bottom if s != b][0]
	sig_map[tl] = "tl"
	sig_map[bl] = "bl"

	# top right and bottom right:
	# if the length is 6 and only one of the right hand side is lit then it must be a 6
	# therefore the lit segment must be the bottom right
	for seg_str in _inputs:
		if len(seg_str) == 6:
			if sum([1 for s in right_side if s in seg_str]) == 1:
				br = [s for s in seg_str if s in right_side][0]
				tr = [s for s in right_side if s != br][0]
				sig_map[br] = "br"
				sig_map[tr] = "tr"
	
	output_str = ""
	for o in outputs:
		lit_seg_list = ",".join([sig_map[s] for s in o])
		output_str += seg_to_num(lit_seg_list)
	
	total += int(output_str)

print(total)
