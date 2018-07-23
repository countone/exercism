def encode(message, rails):

    message=message.replace(' ','')

    encoded=''
    next=0
    for i in range(rails):
    	if i in [0,rails-1]:
    		suffix=rails*2-2
    		while next<len(message):
    			encoded+=message[next]
    			next+=suffix
    		next=i+1
    	else:
    		next=i
    		down=True
    		while next<len(message):
    			encoded+=message[next]
    			if down:
    				suffix=rails*2-2-2*i
    			else:
    				suffix=2*i
    			next+=suffix
    			down= not down
    		next=i+1

    return encoded
    	

def decode(encoded_message, rails):
	
	#calculate the length of rails
	length=[]
	for i in range(rails):
		if i==0:
			length.append(len(encoded_message)//(2*rails-2))
		elif i==rails-1:
			length.append(length[0])
		else:
			length.append(length[0]*2)
	
	remainder=len(encoded_message)%(2*rails-2)

	down=True
	i=0
	while remainder>0:
		length[i]+=1
		remainder-=1
		if down:
			i+=1
		else:
			i-=1
		if i==len(length)-1:
			down=not down
	
	#creating rails based on length
	start=0
	rail_list=[]
	for width in length:
		rail_list.append(list(encoded_message[start:start+width]))
		start+=width
	
	#decrypting the message from rails
	down=True
	decoded=''
	i=0
	while True:
		decoded+=rail_list[i][0]
		del(rail_list[i][0])

		if i==0:
			down=True
		elif i==rails-1:
			down=False

		if down:
			i+=1
		else:
			i-=1
		

		#checking if entire message is decoded
		is_empty=False
		count=0
		for j in range(rails):
			if len(rail_list[j])==0:
				count+=1
				if count==rails:
					is_empty=True
					break
			else:
				break

		if is_empty:
			break

	return decoded

