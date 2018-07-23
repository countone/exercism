def calculate_total(books):
	#discounts
	if len(set(books))==len(books):
		if len(books)==1:
			price=800
		elif len(books)==2:
			price=1520
		elif len(books)==3:
			price=2160
		elif len(books)==4:
			price=2560
		elif len(books)==5:
			price=3000
		else:
			price=0

		return price
	#figuring out the best set
	else:
		categories=[]
		book_sets=[]
		books1=books[:]
		
		#sets of 5
		while  len(books1)>0 :
			current_set=[]
			for i in range(1,6):
				if i in books1:
					current_set.append(i)
					books1.remove(i)
			book_sets.append(current_set)

		categories.append(book_sets)
		book_sets=[]
		books1=books[:]

		#sets of 4
		while  len(books1)>0 :
			current_set=[]
			for i in range(1,6):
				if i in books1:
					current_set.append(i)
					books1.remove(i)
				if len(current_set)==4:
					break
			book_sets.append(current_set)

		categories.append(book_sets)
		
		#calculating price for different sets
		price_list=[]
		for category in categories:	
			price=0
			for item in category:
				price+=(calculate_total(item))
			price_list.append(price)

		return min(price_list)
