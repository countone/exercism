def is_paired(input_string):
	start=['[','{','(']
	end=[']','}',')']

	input_stack=[]

	for char in input_string:
		if char in start:
			input_stack.append(char)
		elif char in end:
			if not input_stack:
				return False
			if end.index(char)==start.index(input_stack[-1]):
				input_stack.pop()
			else:
				return False
		else:
			pass

	return not input_stack
