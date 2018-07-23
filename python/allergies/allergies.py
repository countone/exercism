class Allergies(object):

	def __init__(self, score):
		
		self.score=score
	
	def is_allergic_to(self, item):
		
		return (item in self.lst) 

	@property
	def lst(self):
		
		allergy_list=[]
		temp_score=self.score%256

		while temp_score>0:
			if temp_score>=128:
				temp_score-=128
				allergy_list.append('cats')
			elif temp_score>=64:
				temp_score-=64
				allergy_list.append('pollen')
			elif temp_score>=32:
				temp_score-=32
				allergy_list.append('chocolate')
			elif temp_score>=16:
				temp_score-=16
				allergy_list.append('tomatoes')
			elif temp_score>=8:
				temp_score-=8
				allergy_list.append('strawberries')
			elif temp_score>=4:
				temp_score-=4
				allergy_list.append('shellfish')
			elif temp_score>=2:
				temp_score-=2
				allergy_list.append('peanuts')
			elif temp_score>=1:
				temp_score-=1
				allergy_list.append('eggs')

		return allergy_list[::-1]

		
