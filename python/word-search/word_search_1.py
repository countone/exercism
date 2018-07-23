class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch(object):
    def __init__(self, puzzle):
        self.puzzle=puzzle
        
        vertical=[]
        for i in range(len(puzzle[0])):
        	row=''
        	for j in range(len(puzzle)):
        		row+=puzzle[j][i]
        	vertical.append(row)
        
        self.vertical=vertical
    
    def search(self, word):
		
		# for horizontal search
		for i in range(len(self.puzzle)):
			for j in range(len(self.puzzle[0])):
				#forward
				if word[0]==self.puzzle[i][j]:
					if word==self.puzzle[i][j:min(j+len(word),len(self.puzzle[0]))]:
						return Point(j,i),Point(j+len(word)-1,i)
				# backwards
				elif word[-1]==self.puzzle[i][j]:
					if word[::-1]==self.puzzle[i][j:min(j+len(word),len(self.puzzle[0]))]:
						return Point(j+len(word)-1,i),Point(j,i)
					

		#searching vertically
		
		for i in range(len(self.vertical)):
			for j in range(len(self.vertical[0])):
				# downwards
				if word[0]==self.vertical[i][j]:
					if word==self.vertical[i][j:min(j+len(word),len(self.vertical[0]))]:
						return Point(i,j),Point(i,j+len(word)-1)
				# upwards
				elif word[-1]==self.vertical[i][j]:
					if word[::-1]==self.vertical[i][j:min(j+len(word),len(self.vertical[0]))]:
						return Point(i,j+len(word)-1),Point(i,j)


		#diagonally
		for i in range(len(self.puzzle)):
			for j in range(len(self.puzzle[0])):

				
				if word[0]==self.puzzle[i][j]:
					x,y=i,j
					a,b=i,j

					#left top - bottom right
					for z in range(1,len(word)):
						a+=1
						b+=1
						try:
							if word[z]==self.puzzle[a][b]:
								continue
							else:
								break
						except IndexError:
							break
					else:
						return Point(x,y),Point(a,b)

					#left bottom - top right
					a,b=i,j
					for z in range(1,len(word)):
						a-=1
						b+=1
						try:
							if word[z]==self.puzzle[a][b]:
								continue
							else:
								break
						except IndexError:
							break
					else:
						return Point(a,b),Point(x,y)

				
				elif word[-1]==self.puzzle[i][j]:
					x,y=i,j
					a,b=i,j
					#bottom right - left top
					for z in range(len(word)-2,-1,-1):
						a+=1
						b+=1
						try:
							if word[z]==self.puzzle[a][b]:
								continue
							else:
								break
						except IndexError:
							break
					else:
						return Point(b,a),Point(y,x)

					#top right - bottom left
					a,b=i,j
					for z in range(len(word)-2,-1,-1):
						print(a,b,word[z],z)
						a-=1
						b+=1
						try:
							if word[z]==self.puzzle[a][b]:
								print(self.puzzle[a][b])
								continue
							else:
								print(self.puzzle[a][b])
								break
						except IndexError:
							break
					else:
						return Point(b,a),Point(y,x)
		

