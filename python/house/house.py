verse={
	1:'the house that Jack built.',
	2:'the malt ',
	3:'the rat ',
	4:'the cat ',
	5:'the dog ',
	6:'the cow with the crumpled horn ',
	7:'the maiden all forlorn ',
	8:'the man all tattered and torn ',
	9:'the priest all shaven and shorn ',
	10:'the rooster that crowed in the morn ',
	11:'the farmer sowing his corn ',
	12:'the horse and the hound and the horn '
	}
prefix={0:'This is ',
		1:'that lay in ',
		2:'that ate ',
		3:'that killed ',
		4:'that worried ',
		5:'that tossed ',
		6:'that milked ',
		7:'that kissed ',
		8:'that married ',
		9:'that woke ',
		10:'that kept ',
		11:'that belonged to '}

def recite(start_verse, end_verse):

	rhyme=[]
	if start_verse==end_verse:
		song=''
		song+=prefix[0]+verse[start_verse]
		start_verse-=1

		while start_verse>0:
			song+= prefix[start_verse]+verse[start_verse]
			start_verse-=1

		rhyme.append(song)
	
		return rhyme
	else:
		for i in range(start_verse,end_verse+1):
			rhyme.append(recite(i,i)[0])

		return rhyme