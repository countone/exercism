class Clock(object):
    def __init__(self, hour, minute):
        hour+=minute//60
        self.minute=minute%60
        
        self.hour=hour%24


    def __repr__(self):
        if len(str(self.hour))==1 and len(str(self.minute))==1:
        	return '0'+str(self.hour)+':'+'0'+str(self.minute)
        elif len(str(self.hour))==1 and len(str(self.minute))==2:
        	return '0'+str(self.hour)+':'+str(self.minute)
        elif len(str(self.hour))==2 and len(str(self.minute))==1:
        	return str(self.hour)+':'+'0'+str(self.minute)
        else: 
        	return str(self.hour)+':'+str(self.minute)

    def __eq__(self, other):
        return self.minute== other.minute and other.hour==self.hour

    def __add__(self, minutes):
        return Clock(self.hour,self.minute+minutes)

    def __sub__(self, minutes):
		return Clock(self.hour,self.minute-minutes)

