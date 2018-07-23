def saddle_points(matrix):

	for c in range(1,len(matrix)):
		length=len(matrix[0])
		if length==len(matrix[c]):
			continue
		else:
			raise ValueError('ValueError')


	saddle_points=[]

	for row in range(len(matrix)):
		for column in range(len(matrix[0])):
			current=matrix[row][column]
			saddle=True
			for j in range(len(matrix[0])):
				if current >= matrix[row][j]:
					continue
				else:
					saddle=False
			if saddle:
				for i in range(len(matrix)):
					if current <= matrix[i][column]:
						continue
					else:
						saddle=False
			if saddle:
				saddle_points.append((row,column))
	return set(saddle_points)	