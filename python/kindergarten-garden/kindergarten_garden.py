class Garden(object):
    def __init__(self, diagram, students='Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry'.split(' ')):
        
        
        self.row1,self.row2=diagram.split('\n')
        self.students=students
        self.students.sort()

    def plants(self, student):
    	plantcode=''
    	plantcode+=self.row1[self.students.index(student)*2]+self.row1[self.students.index(student)*2+1] \
    	+self.row2[self.students.index(student)*2]+self.row2[self.students.index(student)*2+1]
    	
    	plantlist=[]
    	for i in plantcode:
    		if i=='V':
    			plantlist.append('Violets')
    		elif i=='R':
    			plantlist.append('Radishes')
    		elif i=='C':
    			plantlist.append('Clover')
    		elif i=='G':
    			plantlist.append('Grass')

    	return plantlist
