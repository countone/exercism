class Phone(object):
    def __init__(self, phone_number):
    	for ch in ['(',')','.',' ','+','-']:
    		phone_number=phone_number.replace(ch,'')

    	if len(phone_number)==11:
    		if phone_number.startswith('1'):		
    			phone_number=phone_number[1:]
    		else:
    			raise ValueError('ValueError')
    	elif len(phone_number)!=10:
    		raise ValueError('ValueError')

    	if phone_number[3]in ['1','0'] or phone_number[0] in ['1','0']:
    		raise ValueError('ValueError')
    	else:
    		self.number=phone_number
    		self.area_code=phone_number[0:3]

    def pretty(self):
    	return '('+self.area_code+')'+' '+self.number[3:6]+'-'+self.number[6:]