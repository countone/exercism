roman=[(1000, 'M'),(900,'CM') ,(500, 'D'),(400,'CD') ,(100, 'C'),(90,'XC'), (50, 'L'),(40,'XL'), (10, 'X'),(9,'IX'), (5, 'V'),(4,'IV'), (1, 'I'),(0,'')]

def numeral(number,index=0):

	for i in range(14):
		if roman[i][0]==number:
			return roman[i][1]

	num=roman[index][0]
	if 0<number//num<4:
		return number//num*numeral(num)+numeral(number%num,index+1)
	else:
		return numeral(number,index+1)

