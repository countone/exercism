def largest_product(series, size):
	
	product_list=[]
	if len(series)<size or (len(series)>0 and not series.isdigit()) or size<0:
		raise ValueError('ValueError')
	else:
		for i in range(len(series)-size+1):
			product=1
			for j in range(i,i+size):
				product*=int(series[j])
			product_list.append(product)

	return max(product_list)