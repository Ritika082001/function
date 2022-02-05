def count():
	a=["abc","xyz","aba","1221"]
	i=0
	c=0
	while i<len(a):
		if a[i] ==a[-i]:
			c=c+1
		i=i+1
	print(c)
count()