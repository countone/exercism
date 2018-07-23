def tally(tournament_results):
	standing =['Team                           | MP |  W |  D |  L |  P']
	if tournament_results=='':
		return '\n'.join(standing)

	lines= tournament_results.split('\n')
	results=[list(line.split(';')) for line in lines]
	table={}

	for match in results:
		
		first_team= match[0]
		second_team=match[1]
		result= match[2]

		if first_team in table.keys():
			table[first_team][0]+=1
		else:
			table[first_team]=[1,0,0,0,0]

		if second_team in table.keys():
			table[second_team][0]+=1
		else:
			table[second_team]=[1,0,0,0,0]

		if result=='win':
			table[first_team][1]+=1
			table[second_team][3]+=1
		elif result=='loss':
			table[first_team][3]+=1
			table[second_team][1]+=1
		elif result=='draw':
			table[first_team][2]+=1
			table[second_team][2]+=1

	for key,value in table.items():
		current =table[key]
		current[4]=current[1]*3+current[2]
		table[key]=current
	
	table_list=[]
	for key , value in table.items():
		table_list.append([key,value[0],value[1],value[2],value[3],value[4]])
	table_list.sort(key=lambda x: (-x[5],x[0]))

	
	for items in table_list:
		standing.append(items[0].ljust(31)+
					'|  '+str(items[1])+
					' |  '+str(items[2])+
					' |  '+str(items[3])+
					' |  '+str(items[4])+
					' |  '+str(items[5]))


	return '\n'.join(standing)



