def sieve(limit):
    prime=[]
    values={i:'y' for i in range(2,limit+1)}
    
    for keys in values.keys():
    	if values[keys]=='n':
    		continue
    	else:
    		for i in range(keys,limit//keys+1):
    			values[keys*i]='n'

    for key in values:
    	if values[key]=='y':
    		prime.append(key)

    return prime
