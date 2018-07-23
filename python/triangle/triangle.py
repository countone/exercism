def is_equilateral(sides):
    
    if is_valid(sides):
    	return len(set(sides))==1
    else:
    	return is_valid(sides)


def is_isosceles(sides):

    if is_valid(sides):
    	return len(set(sides))<=2
    else:
    	return is_valid(sides)


def is_scalene(sides):
    
    if is_valid(sides):
    	return len(set(sides))==3
    else:
    	return is_valid(sides)


def is_valid(sides):

	if len(sides)==3:
		
		if sides[0]+sides[1]<=sides[2]:
			is_valid=False
		elif sides[0]+sides[2]<=sides[1]:
			is_valid=False
		elif sides[1]+sides[2]<=sides[0]:
			is_valid=False
		else:
			is_valid=True

	return is_valid