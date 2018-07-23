digit = {
		(" _ ",
         "| |",
         "|_|",
         "   "): '0',
		("   ",
		 "  |",
		 "  |",
		 "   "): '1',
		(" _ ",
         " _|",
         "|_ ",
         "   "): "2",
		(" _ ",
         " _|",
         " _|",
         "   "): "3",
		("   ",
         "|_|",
         "  |",
         "   "): "4",
		(" _ ",
         "|_ ",
         " _|",
         "   "): "5",
		(" _ ",
         "|_ ",
         "|_|",
         "   "): "6",
		(" _ ",
         "  |",
         "  |",
         "   "): "7",
		(" _ ",
         "|_|",
         "|_|",
         "   "): "8",
		(" _ ",
         "|_|",
         " _|",
         "   "): "9"}
def convert(input_grid):

	if len(input_grid)%4==0:
		if len(input_grid)//4>1:
			result=''
			line=[]
			for i in range(len(input_grid)/4):
				line.append(input_grid[4*i:4*i+4])
			for item in line:
				result+=convert(item)+','
			return result[:len(result)-1]
		elif len(input_grid[0])==3:
			if tuple(input_grid) in digit.keys():
				return digit[tuple(input_grid)]
			else:
				return '?'
		elif len(input_grid[0])%3==0:
			
			first=[]
			for j in range(len(input_grid)):
				first.append(input_grid[j][:3])
			rest=[]
			for j in range(len(input_grid)):
				rest.append(input_grid[j][3:])
			
			if tuple(first) in digit.keys():
					return digit[tuple(first)]+convert(rest)
			else:
				return '?'+convert(rest)
		else:
			raise ValueError('ValueError') 
	else:
		raise ValueError('ValueError')