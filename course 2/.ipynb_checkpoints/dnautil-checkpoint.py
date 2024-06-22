""" 
dnautil contains some of the functions we wrote
""" 

complements = { 'a':'t', 't':'a', 'g':'c', 'c':'g' } 

def has_inframe_stop(dna):
    """ checks if a DNA sequuence contains in frame stop codon """
    stop_codons = ['TAA', 'TAG', 'TGA'] 

    """ goes through the string from the start to end, skipping three each time """ 
    for i in range(0, len(dna), 3): 
        if dna[i:i+3] in stop_codons:
            return True
    return False 
    
# overloaded allows user to specify reading frame 
def has_inframe_stop(dna, frame = 0):
    """ checks if a DNA sequuence contains in frame stop codon """
    stop_codons = ['TAA', 'TAG', 'TGA'] 

    """ goes through the string from the start to end, skipping three each time """ 
    for i in range(frame, len(dna), 3): 
        if dna[i:i+3] in stop_codons:
            return True
    return False 

def complement(dna):
    reverse_complement_list = []
    for letter in dna:
        complement = complements[letter]
        reverse_complement_list += [complement]
    # join method joins the list with spaces in between of whatever specified before the dot. 
    return ''.join(reverse_complement_list)

def complement(dna):
    return ''.join([complements[base] for base in dna])
