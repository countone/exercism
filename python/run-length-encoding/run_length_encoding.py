def decode(string):
	decoded=''
	position=0
	length=0
	for i in range(len(string)):
		if string[i].isdigit():
			length+=1
		elif string[i].isalpha() or string[i].isspace():
			if length==1:
				print(string[position:i])
				decoded=decoded+int(string[position])*string[i]
			elif length==0:
				decoded=decoded+string[i]
			else:
				decoded=decoded+int(string[position:i])*string[i]
			position=i+1
			length=0
	return decoded


def encode(string):
	encoded=''
	position=0
	for i in range(len(string)):
		if (i < position):
			continue
		else:
			current=string[i]
			count=0
			for j in range(i,len(string)):
				if string[j]==current:
					count+=1
					if j==len(string)-1:
						position=j+1
						break
				else:
					position=j
					break
			if count==1:
				encoded=encoded+current
			else:
				encoded=encoded+str(count)+current
			if position==len(string):
				break
	return encoded

