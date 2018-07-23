def nth_prime(positive_number):
	
	if positive_number<=0:
		raise ValueError('ValueError')

	prime_list=[]
	
	i=2
	while True:
		for j in range(2,i):
			if i%j==0:
				break
		else:
			prime_list.append(i)
		i+=1

		if len(prime_list)>=positive_number:
			break

	return prime_list[-1]

