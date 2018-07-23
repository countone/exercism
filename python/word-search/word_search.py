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
				if word[0]==self.puzzle[i][j]:
					if word==self.puzzle[i][j:min(j+len(word),len(self.puzzle[0]))]:
						return Point(j,i),Point(j+len(word)-1,i)
					
		word=word[::-1]
		for i in range(len(self.puzzle)):
			for j in range(len(self.puzzle[0])):
				if word[0]==self.puzzle[i][j]:
					if word==self.puzzle[i][j:min(j+len(word),len(self.puzzle[0]))]:
						return Point(j+len(word)-1,i),Point(j,i)
		
		#searching vertically
		word=word[::-1]
		for i in range(len(self.vertical)):
			for j in range(len(self.vertical[0])):
				if word[0]==self.vertical[i][j]:
					if word==self.vertical[i][j:min(j+len(word),len(self.vertical[0]))]:
						return Point(i,j),Point(i,j+len(word)-1)

		word=word[::-1]
		for i in range(len(self.vertical)):
			for j in range(len(self.vertical[0])):
				if word[0]==self.vertical[i][j]:
					if word==self.vertical[i][j:min(j+len(word),len(self.vertical[0]))]:
						return Point(i,j+len(word)-1),Point(i,j)

		word=word[::-1]
		for i in range(len(self.puzzle)):
			for j in range(len(self.puzzle[0])):
				if word[0]==self.puzzle[i][j]:
					firstx,firsty=i,j
					a,b=i,j
					for i in range(1,len(word)):
						a+=1
						b+=1
						try:
							if word[i]==self.puzzle[a][b]:
								continue
							else:
								break
						except IndexError:
							break
					else:
						return Point(firstx,firsty),Point(a,b)

		word=word[::-1]
		for i in range(len(self.puzzle)):
			for j in range(len(self.puzzle[0])):
				if word[0]==self.puzzle[i][j]:
					firstx,firsty=j,i

					a,b=j,i
					for c in range(1,len(word)):
						a+=1
						b+=1
						try:
							if word[c]==self.puzzle[b][a]:
								continue
							else:
								break
							
						except IndexError:
							break
					else:
						return Point(a,b),Point(firstx,firsty)
		word=word[::-1]
		for i in range(len(self.puzzle)):
			for j in range(len(self.puzzle[0])):
				if word[0]==self.puzzle[i][j]:
					firstx,firsty=i,j
					a,b=i,j
					for i in range(1,len(word)):
						a+=1
						b-=1
						try:
							if word[i]==self.puzzle[a][b]:
								continue
							else:
								break
						except IndexError:
							break
					else:
						return Point(firsty,firstx),Point(b,a)

		
		for i in range(len(self.vertical)):
			for j in range(len(self.vertical[0])):
				if word[0]==self.vertical[i][j]:
					firstx,firsty=j,i

					a,b=j,i
					for c in range(1,len(word)):
						a-=1
						b+=1
						try:
							if word[c]==self.vertical[b][a]:
								continue
							else:
								break
							
						except IndexError:
							break
					else:
						return Point(a,b),Point(firstx,firsty)


