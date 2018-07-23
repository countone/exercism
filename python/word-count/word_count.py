def word_count(phrase):
	phrase=phrase.strip()
	for char in ['.',':','\n','!','@','#','$','%','^','&']:
		if char in phrase:
			phrase=phrase.replace(char,'')

	for char in [',','   ','  ','_','\t']:
		if char in phrase:
			phrase=phrase.replace(char,' ')
	phraselist= phrase.lower().split(' ')
	for word in phraselist:
		if word.startswith("'") and word.endswith("'"):
			phraselist.remove(word)
			phraselist.append(word[1:len(word)-1])
	phraseset = set(phraselist)
	wordcount={}

	for value in phraseset:
		wordcount[value]=phraselist.count(value)
	return wordcount

