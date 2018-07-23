def sum_of_multiples(limit, multiples):
	
	product=0
	multiplelist=[]
	
	for multiple in multiples:
		for i in range(1,limit//multiple+1):
			multiplelist.append(multiple*i)
	
	sum=0
	
	for products in set(multiplelist):
		sum+=products

	return sum