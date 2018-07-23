
def flatten(iterable):
    flat=[]
    for i in iterable:
    	if type(i) in [list,tuple]:
    		flat+=flatten(i)
    	else:
    		if i is None:
    			continue
    		else:
    			flat.append(i)

    return flat
