def recite(start, take=1):
    
    song=[]

    while take>0:
    	if start==0:
    		song.append('No more bottles of beer on the wall, no more bottles of beer.')
    		song.append('Go to the store and buy some more, 99 bottles of beer on the wall.')
    	elif start==1:
    		song.append('1 bottle of beer on the wall, 1 bottle of beer.')
    		song.append('Take it down and pass it around, no more bottles of beer on the wall.')
    	else:
    		song.append(str(start)+' bottles of beer on the wall, '+str(start)+ ' bottles of beer.')
    		if start==2:
    			song.append('Take one down and pass it around, 1 bottle of beer on the wall.')
    		else:
    			song.append('Take one down and pass it around, '+str(start-1)+' bottles of beer on the wall.')
    	if take!=1:
    		song.append('')
    	start-=1
    	take-=1

    return song


