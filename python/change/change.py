def find_minimum_coins(total_change, coins):
	
	coins=coins[::-1]
	
	change_list=[]
	for i in range (0,len(coins)):
		coin_list=coins[i:len(coins)]
		
		change=total_change

		count_list=[]
		for coin in coin_list:

			
			if change>=coin:
				
				count_list.append(change//coin)
				change=change%coin
			else:
				
				count_list.append(0)	
		
		if change==0:
			change_list.append(count_list)
			print(count_list)
	print(change_list)
	
	minimum_coins=0
	for i in range(1,len(change_list)):
		if sum(change_list[i])<sum(change_list[minimum_coins]):
			minimum_coins=i
	
	change=[]
	print(change_list[minimum_coins])
	start=len(coins)-len(change_list[minimum_coins])
	print(start)

	for i in range(len(change_list[minimum_coins])):
		for j in range(change_list[minimum_coins][i]):
			change.append(coins[start])
			print(change)
		start+=1

	return sorted(change)

#print(find_minimum_coins(21, [2, 5, 10, 20]),'result')