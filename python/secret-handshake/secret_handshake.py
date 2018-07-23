codedict={1:'wink',2:'double blink',3:'close your eyes',4:'jump'}
codelist=[(1,'wink'),(2,'double blink'),(3,'close your eyes'),(4,'jump')]

def handshake(code):
    
    actions=[]

    if code//16>0:
     	actions = handshake(code%16)
    	actions.reverse()
    	return actions 

    binary=str(bin(code))[2:]
    
    for i in range(1,len(binary)+1):
    	if binary[-i]=='1':
    		actions.append(codedict[i])
    return actions

def secret_code(actions):
	code=0
	order=[]
	for action in actions:
		for i in range(len(codelist)):
			if action== codelist[i][1]:
				code+= codelist[i][0]
				order.append(i)

	if sorted(order)!=order:
		code+=16

	return code