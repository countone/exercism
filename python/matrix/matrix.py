class Matrix(object):
    def __init__(self, matrix_string):
        
        self.mList=matrix_string.split('\n')
        for i in range(len(self.mList)):
        	self.mList[i]=self.mList[i].split(' ')
        	for j in range(len(self.mList[i])):
        		self.mList[i][j]=int(self.mList[i][j]) 

    def row(self, index):
        return self.mList[index]

    def column(self, index):
        return [item[index] for item in self.mList]