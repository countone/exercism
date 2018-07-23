def is_armstrong(number):
    length=len(str(number))
    sum=0
    for i in range(length):
    	sum+= int(str(number)[i])**length
    
    return sum==number
