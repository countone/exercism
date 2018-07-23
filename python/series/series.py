def slices(series, length):
	slicelist=[]
	if series=='' or len(series)<length or length<1:
		raise ValueError('ValueError')
	else:
		for i in range(len(series)-length+1):
			slicelist.append(series[i:i+length])
	return slicelist
