def classify(number):

	if number<1:
		raise ValueError('ValueError')
	
	aliquot_sum=0
	
	for i in range(1,number//2+1):
		if number%i==0:
			aliquot_sum+=i

	if aliquot_sum<number:
		return "deficient"
	elif aliquot_sum==number:
		return "perfect"
	else:
		return "abundant"