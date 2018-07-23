# Score categories
# Change the values as you see fit
YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
	score=0
	if category==1:
		score=dice.count(1)
	elif category==2:
		score=dice.count(2)*2
	elif category==3:
		score=dice.count(3)*3
	elif category==4:
		score=dice.count(4)*4
	elif category==5:
		score=dice.count(5)*5
	elif category==6:
		score=dice.count(6)*6
	elif category==12:
		if dice.count(dice[0])==5:
			score=50
	elif category==10:
		if set(dice)=={2,3,4,5,6}:
			score=30
	elif category==9:
		if set(dice)=={1,2,3,4,5}:
			score=30
	elif category==8:
		for i in range(2):
			if dice.count(dice[i])>=4:
				score=4*dice[i]
	elif category ==11:
		sum=0
		for i in range(5):
			sum+=dice[i]
		score=sum
	elif category==7:
		if len(set(dice))==2:
			if dice.count(list(set(dice))[0]) in [2,3]:
				for i in range(5):
					score+=dice[i]

	return score



