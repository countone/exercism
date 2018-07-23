def verify(isbn):
	isb=isbn.replace('-','')
	multiplier=10
	sum=0
	if len(isb)>10:
		return False
	else:
		for i in range(len(isb)-1) :
			if isb[i].isdigit():
				sum=sum+(int(isb[i])*multiplier)
				multiplier-=1
		if len(isb)==10:
			if isb[-1]=='X':
				sum=sum+10
			elif isb[-1].isdigit():
				sum=sum+int(isb[-1])
			if sum%11==0:
				return True
			else:
				return False
		else:
			return False

