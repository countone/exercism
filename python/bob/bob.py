def hey(phrase):
	phrase=phrase.strip()
	if phrase.endswith('?') and phrase.isupper():
		answer="Calm down, I know what I'm doing!"
	elif phrase.endswith('?'):
		answer='Sure.'
	elif phrase.isupper():
		answer='Whoa, chill out!'
	elif phrase=='':
		answer= 'Fine. Be that way!'
	else:
		answer='Whatever.'
	return answer