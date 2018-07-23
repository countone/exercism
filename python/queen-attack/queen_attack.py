class Queen(object):
    def __init__(self, row, column):

    	if -1<row<8 and -1<column<8:
        	self.row = row
        	self.column = column
        else:
        	raise ValueError('ValueError')

    def can_attack(self, another_queen):
		
		if self.row==another_queen.row and self.column==another_queen.column:
			raise ValueError('ValueError')

		if self.row==another_queen.row or self.column==another_queen.column:
			return True
		elif (abs(self.row-another_queen.row))==(abs(self.column-another_queen.column)):
			return True
		else:
			return False