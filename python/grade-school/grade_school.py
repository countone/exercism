class School(object):
	def __init__(self, name):
		self.name=name
		self.studentlist=[]
		
	def add(self,name,grade):
		for i in range(len(self.studentlist)):
			if grade==self.studentlist[i][0]:
				self.studentlist[i]=(grade,self.studentlist[i][1]+(name,))
				break
		else:
			self.studentlist.append((grade,(name,)))

	def grade(self, grade_no):
		for gradelist in self.studentlist:
			if grade_no==gradelist[0]:
				return gradelist[1]
		else:
			return set()

	def sort(self):
		for i in range(len(self.studentlist)):
			self.studentlist[i]=(self.studentlist[i][0], tuple(sorted(self.studentlist[i][1])))
			self.studentlist=sorted(self.studentlist, key=lambda x: x[0])
		return self.studentlist






