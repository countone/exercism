from random import choice
from string import ascii_lowercase

lowercase=list(ascii_lowercase)

class Cipher(object):

	def __init__(self, key=''.join(choice(ascii_lowercase) for i in range(100))):
		
		if key.islower():
			self.key=key
		else:
			raise ValueError('ValueError')

	def encode(self, text):
		
		encoded=''

		if len(text)>len(self.key):
			self.key=self.key*(len(text)//len(self.key)+1)

		if text.islower():
			for i in range(len(text)):
				encoded+=lowercase[(lowercase.index(text[i])+lowercase.index(self.key[i]))%26]
		else:
			raise ValueError('ValueError')

		return encoded 

	def decode(self, text):
		
		decoded=''
		
		if len(text)>len(self.key):
			self.key=self.key*(len(text)//len(self.key)+1)
			
		if text.islower():
			for i in range(len(text)):
				decoded+=lowercase[lowercase.index(text[i])-lowercase.index(self.key[i])]
		else:
			raise ValueError('ValueError')

		return decoded