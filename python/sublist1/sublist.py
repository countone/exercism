SUBLIST=1
EQUAL=0
SUPERLIST=2
UNEQUAL=3

def check_lists(first_list, second_list):
    
    if len(first_list)==len(second_list):
    	if first_list==second_list:
    		return EQUAL
    	else:
    		return UNEQUAL

    elif len(first_list)<len(second_list):
    	if not first_list:
    		return SUBLIST
    	else:
    		for i in range(len(second_list)):
    			if first_list[0]==second_list[i]:
    					if first_list==second_list[i:i+len(first_list)]:
    						return SUBLIST
    		else:
    			return UNEQUAL
    elif len(first_list)>len(second_list):

    	if check_lists(second_list,first_list)==SUBLIST:
    		return SUPERLIST
    	else:
    		return UNEQUAL