from string import ascii_uppercase
from random import choice

digit_list=[0,1,2,3,4,5,6,7,8,9]

class Robot(object):

	names=[]

	def __init__(self):
		
		name_set=False

		while name_set==False:
			new_name=choice(ascii_uppercase)+choice(ascii_uppercase)+str(choice(digit_list))+str(choice(digit_list))+str(choice(digit_list))
			if new_name not in Robot.names:
				self.name=new_name
				Robot.names.append(new_name)
				name_set=True

			
	def reset(self):

		name_set=False

		while name_set==False:
			new_name=choice(ascii_uppercase)+choice(ascii_uppercase)+str(choice(digit_list))+str(choice(digit_list))+str(choice(digit_list))
			if new_name not in Robot.names:
				Robot.names.remove(self.name)
				self.name=new_name
				Robot.names.append(new_name)
				name_set=True
