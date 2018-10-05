for i in range(1000000):	
	res=0
	num=i
	c=len(str(num))
	while num>0:
		a=num%10
		res =res+(a**c)
		num =num//10
	if res==i: print(i)	
