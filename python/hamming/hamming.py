def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
    	raise ValueError('ValueError')
	

    else:
    	hdist=0
    	for i in range(len(strand_b)):
    		if strand_a[i] != strand_b[i]:
    			hdist+=1
    return hdist

