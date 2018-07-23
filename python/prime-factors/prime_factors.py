import sympy

def prime_factors(natural_number):
	
	factor_list=[]
	factor=2

	while(natural_number>1):
		if natural_number% factor==0:
			factor_list.append(factor)
			natural_number=natural_number/factor
		else:
			 factor=sympy.nextprime(factor)

	return factor_list

