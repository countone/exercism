from string import ascii_lowercase,ascii_uppercase
def rotate(text, key):
    lower=list(ascii_lowercase)
    upper=list(ascii_uppercase)
    cipher=''
    for i in range (len(text)):
    	if text[i].isspace():
    		cipher+=' '
    	elif text[i].islower():
    		index=lower.index(text[i])
    		cipher+=lower[(index+key)%26]
    	elif text[i].isupper():
    		index=upper.index(text[i])
    		cipher+=upper[(index+key)%26]
    	else:
    		cipher+=text[i]

    return cipher