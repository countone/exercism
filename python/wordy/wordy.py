def calculate(question):
	question= question[:len(question)-1]
	question=question.split(' ')

	arguments= question[2:]

	if len(arguments)>4:
		if arguments[1] in ['multiplied','divided']:
			first_result= calculate('What is '+' '.join(arguments[:4])+'?')
			return calculate('What is '+' '.join([str(first_result)]+arguments[4:])+'?')
		elif arguments[1] in ['plus','minus']:
			first_result= calculate('What is '+' '.join(arguments[:3])+'?')
			return calculate('What is '+' '.join([str(first_result)]+arguments[3:])+'?')
		else:
			raise ValueError('ValueError')

	operator=arguments[1]
	if operator=='plus':
		return int(arguments[0])+int(arguments[2])
	elif operator=='minus':
		return int(arguments[0])-int(arguments[2])
	elif operator=='multiplied':
		return int(arguments[0])*int(arguments[3])
	elif operator=='divided':
		return int(arguments[0])/int(arguments[3])
	else:
		raise ValueError('ValueError')
