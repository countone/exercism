def abbreviate(words):
	words=words.replace(',','')
	words=words.replace('-',' ')
	wordlist=words.split(' ')
	acronym=''
	for word in wordlist:
		acronym+=word[0].upper()

	return acronym