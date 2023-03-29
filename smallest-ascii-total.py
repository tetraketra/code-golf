# test_cases = [["a", "b", "c"],
# 			  ["hello", "world", "code"],
# 			  ["aaa", "aa", ""],
# 			  ["cat", "bat", "rat"],
# 			  ["zab", "xyz", "abcd"]]

def t(l):
	a=[*map(lambda x:sum(map(ord,x)),l)]
	return l[a.index(min(a))]

# for test in test_cases:
#     print(t(test))