def detect_anagrams(word, candidates):
    wordlist=list(word.lower())
    vcandidates=[]
    for words in candidates:
    	if word.lower()==words.lower():
    		continue
    	else:
    		temp=wordlist[:]
    		if len(words)==len(wordlist):
    			for i in range(len(words)):
    				if words[i].lower() in temp:
    					temp.remove(words[i].lower())
    		if len(temp)==0 :
    			vcandidates.append(words)
    return vcandidates
