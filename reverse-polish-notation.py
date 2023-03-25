l,s=input().split(),[]
for i in l:
	if i<"0":b,a=s.pop(),s.pop();s+=[int(eval(f"{a}{i}{b}"))] 
	else:s.append(i)
print(*s)