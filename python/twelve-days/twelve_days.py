prefix='On the '
suffix=' day of Christmas my true love gave to me, '
day={1:'first',
		2:'second',
		3:'third',
		4:'fourth',
		5:'fifth',
		6:'sixth',
		7:'seventh',
		8:'eighth',
		9:'ninth',
		10:'tenth' ,
		11:'eleventh',
		12:'twelfth'}
verse={1:'a Partridge in a Pear Tree.',
		2:'two Turtle Doves, ',
		3:'three French Hens, ',
		4:'four Calling Birds, ',
		5:'five Gold Rings, ',
		6:'six Geese-a-Laying, ',
		7:'seven Swans-a-Swimming, ',
		8:'eight Maids-a-Milking, ',
		9:'nine Ladies Dancing, ',
		10:'ten Lords-a-Leaping, ' ,
		11:'eleven Pipers Piping, ',
		12:'twelve Drummers Drumming, '}
def recite(start_verse, end_verse):
	lyrics=[]
	if start_verse==end_verse:
		if start_verse>1:
			last=True
		else:
			last=False
		curr_verse=prefix+day[start_verse]+suffix
		for i in range(start_verse,0,-1):
			if i==1 and last:
				curr_verse+='and '+verse[i]
			else:
				curr_verse+=verse[i]
		lyrics.append(curr_verse)
		return lyrics
	elif start_verse<end_verse:
		for i in range(start_verse,end_verse+1):
			curr_verse=recite(i,i)
			lyrics.append(curr_verse[0])
		return lyrics
