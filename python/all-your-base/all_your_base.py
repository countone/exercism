def rebase(input_base, digits, output_base):
	
	if input_base<2 or output_base<2 :
		raise ValueError('ValueError')
	else:
		for digit in digits:
			if digit<0 or digit>=input_base:
				raise ValueError('ValueError')


	number=0

	for i in range(len(digits)):
		number+=digits[i]*(input_base**(len(digits)-i-1))

	i=0
	while True:
		a=output_base**i
		if a>number:
			max_power=i-1
			break
		i+=1
	
	output_digits=[]
	while max_power>-1:

		if number >=output_base**max_power:
			output_digits.append(number//(output_base**max_power))
			number=number%(output_base**max_power)
			
		else:
			output_digits.append(0)
		max_power-=1

	return output_digits
