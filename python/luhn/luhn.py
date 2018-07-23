class Luhn(object):
    def __init__(self, card_num):
        self.card_num=card_num
        self.num=self.card_num.replace(' ','')

    def is_valid(self):
        
        if self.card_num!=self.card_num.strip() or self.card_num=='0':
        	return False

        elif self.num.isdigit():
        	sum=0
        	for i in range(1,len(self.num)+1):
        		add=int(self.num[-i])*2
        		if i%2==0 and add>9:
        			sum+=add-9
        		elif i%2==0:
        			sum+=add
        		else:
        			sum+=int(self.num[-i])

        	if sum%10==0:
        		return True
        	else:
        		return False 
        else:
        	return False
        	