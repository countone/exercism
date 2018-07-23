def is_isogram(string):
    wordlist=list(string.upper())
    is_isogram=True
    for letter in wordlist:
    	if letter in [' ','-']:
    		continue
    	elif wordlist.count(letter)>1:
    		is_isogram=False
    		break
    return is_isogram

