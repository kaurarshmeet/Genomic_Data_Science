""" Contains all important functions used in this course. """

def longest_common_prefix(dna1, dna2):
    """ finds longest common prefix.
    should check whether each character matches, if each character matches, 
    concatenate that character to a string. 
    break out of the loop when stops matching. 
    at the end, return len and string """
    lcp = ''
    for i in range( min(len(dna1), len(dna2)) ):
        if dna1[i] != dna2[i]:
            break
        lcp += dna1[i]
    return lcp, len(lcp) # two return values return as a tupule. 

# better function (don't have to create a string) 
def longest_common_prefix(dna1, dna2):
    for i in range( min(len(dna1), len(dna2)) ):
        if dna1[i] != dna2[i]:
            break
    return dna1[:i+1], i+1

def reverse_complement(dna):
    """ dictionary of A, T, C, G """ 
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N'}
    rc = ''
    dna = dna.upper()
    for base in dna:
        rc += complement[base]
    return rc[::-1]

def read_genome_fasta(filename):
    genome = ''
    with open(filename, 'r') as r:
        for line in r:
            if line[0] == '>': 
                continue
            genome += line.rstrip() # removes any trailing whitespace.
    return genome 

# function to parse it 
def read_genome_fastq(file): 
    sequences = []
    qualities = []
    with open(file, 'r') as fastq:
        while True: 
            fastq.readline()
            seq = fastq.readline().rstrip()
            fastq.readline()
            qual = fastq.readline().rstrip()

            if len(seq) == 0:
                break 
            sequences.append(seq)
            qualities.append(qual) 

    return sequences, qualities 

def Q_to_PHRED33(Q):
    return chr(round(Q) + 33) 

def PHRED33_to_Q(PHRED33):
    # ord converts to ascii number
    return ord(PHRED33) - 33 