def contains(s1, s2):
	for i in range(s1.len()):
		if s1[i,i+len(s2)] = s2:
			return True
	return False

print(contains("Hello world", "world"))

# output: True