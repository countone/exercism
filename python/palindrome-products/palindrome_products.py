def largest_palindrome(max_factor, min_factor):
	
	palindrome_products={}
	for i in range (min_factor,max_factor+1):
		for j in range(i,max_factor+1):
			product=i*j
			if str(product)==str(product)[::-1]:
				if product in palindrome_products.keys():
					factors=palindrome_products[product]
					factors.append((i,j))
					palindrome_products[product]=factors
				else:
					palindrome_products[product]=[(i,j)]

	largest_palindrome=max(palindrome_products.keys())
	factors=set(palindrome_products[largest_palindrome])

	return largest_palindrome,set(palindrome_products[largest_palindrome])


def smallest_palindrome(max_factor, min_factor):

	smallest_palindrome=None
	for i in range(min_factor,max_factor+1):
		for j in range(i,max_factor+1):
			product=i*j
			if str(product)==str(product)[::-1]:
				smallest_palindrome=product
				factors={(i,j)}
				break
		if type(smallest_palindrome) is int:
			break
	if smallest_palindrome is None:
		raise ValueError('ValueError`')
	return smallest_palindrome,factors
