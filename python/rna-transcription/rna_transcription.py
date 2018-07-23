def to_rna(dna_strand):
    rna=[]
    for i in range(len(dna_strand)):
    	if dna_strand[i]=='G':
    		rna.append('C')
    	elif dna_strand[i]=='C':
    		rna.append('G')
    	elif dna_strand[i]=='T':
    		rna.append('A')
    	elif dna_strand[i]=='A':
    		rna.append('U')
    return ''.join(rna)