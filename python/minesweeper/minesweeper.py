def board(input_board_array):
	board=input_board_array

	
	for i in range(1,len(board)-1):
		if len(board[i])!=len(board[i+1]):
			raise ValueError('ValueError')

	for i in range(len(board)):
		board[i]=list(board[i])

	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j]==' ':
				count=0
				for a in range(max(i-1,0),min(i+2,len(board))):
					for b in range(max(j-1,0),min(j+2,len(board[0]))):
						if board[a][b]=='*':
							count+=1
				if count!=0:
					board[i][j]=str(count)
			elif board[i][j]=='*':
				continue
			else:
				raise ValueError('ValueError')

	for i in range(len(board)):
		board[i]=''.join(board[i])

	return board



    