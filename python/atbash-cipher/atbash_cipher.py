from string import ascii_lowercase
alphabets=list(ascii_lowercase)
def encode(plain_text):
	
	encoded=''
	for symbol in [' ',',','.']:
		if symbol in plain_text:
			plain_text=plain_text.replace(symbol,'')

	count=0
	for i in range(len(plain_text)):
		try:
			encoded+=alphabets[25-alphabets.index(plain_text[i].lower())]
			
		except ValueError:
			encoded+=plain_text[i]
			
		finally:
			count+=1
			if count%5==0 and i!=len(plain_text)-1:
				encoded+=' '

	return encoded

def decode(ciphered_text):
	
	ciphered_text=ciphered_text.replace(' ','')
	decoded=''
	
	for i in range(len(ciphered_text)):
		try:
			decoded+=alphabets[25-alphabets.index(ciphered_text[i])]
		except ValueError:
			decoded+=ciphered_text[i]
	return decoded