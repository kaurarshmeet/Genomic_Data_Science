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

import modules.boyer_moore
from modules.boyer_moore import * 

def naive(p, t): 
    occurences = []
    """ i is every index until the last one we search. """
    for i in range(len(t) - len(p) + 1):
        """ at every i, we search a substring of t starting at i, equivalent to the length of p. 
        For a length of p = 4, we compare indices 0 1 2 3 of p and indices i+0, i+1, i+2, i+3 of t.
        As soon as we find the first dissimilar character, stop the comparision and move to the next index of i.""" 
        for j in range(len(p)):
            match = True
            if p[j] != t[i+j]: 
                match = False 
                break
        """ If we found no dissimilar characters, append i to occurences. """ 
        if match:
            occurences.append(i)
    return occurences

def naive_hamming(p, t, max_distance = 2):
    """ compares two strings, specify max number of edits that can differ
    Default number of mismatches allowed is 2."""
    occurences = []
    """ i is every index until the last one we search. """
    for i in range(len(t) - len(p) + 1):
        """ at every i, we search a substring of t starting at i, equivalent to the length of p. 
        For a length of p = 4, we compare indices 0 1 2 3 of p and indices i+0, i+1, i+2, i+3 of t.
        As soon as we find the third dissimilar character, stop the comparision and move to the next index of i.""" 
        mismatches = 0
        for j in range(len(p)):
            match = True
            if p[j] != t[i+j]: 
                mismatches += 1 # everytime we hit a mismatch, +1
                if mismatches > max_distance: 
                    match = False 
                    break
        if match:
            occurences.append(i)
    return occurences
    occurences = []
    """ i is every index until the last one we search. """
    for i in range(len(t) - len(p) + 1):
        """ at every i, we search a substring of t starting at i, equivalent to the length of p. 
        For a length of p = 4, we compare indices 0 1 2 3 of p and indices i+0, i+1, i+2, i+3 of t.
        As soon as we find the third dissimilar character, stop the comparision and move to the next index of i.""" 
        mismatches = 0
        for j in range(len(p)):
            match = True
            if p[j] != t[i+j]: 
                mismatches += 1 # everytime we hit a mismatch, +1
                if mismatches > 2: 
                    match = False 
                    break
        if match:
            occurences.append(i)
    return occurences

def naive_with_rc(p, t): 
    occurences = []
    """ i is every index until the last one we search. """
    for i in range(len(t) - len(p) + 1):
        """ at every i, we search a substring of t starting at i, equivalent to the length of p. 
        For a length of p = 4, we compare indices 0 1 2 3 of p and indices i+0, i+1, i+2, i+3 of t.
        As soon as we find the first dissimilar character, stop the comparision and move to the next index of i.""" 
        for j in range(len(p)):
            match = True
            if p[j] != t[i+j]: 
                match = False 
                break

        """ If we found no dissimilar characters, append i to occurences. """ 
        if match:
            occurences.append(i)

        """ at every i, check for the reverse complement as well. """
        rc = reverse_complement(p)
        # skip to next iteration to avoid counting the same index again. 
        if rc == p:
            continue
        
        for r in range(len(rc)):
            match = True
            if rc[r] != t[i+r]:
                match = False
                break
            
        """ If we found no dissimilar characters, append i to occurences. """ 
        if match:
            occurences.append(i)
    
    return occurences

def approximate_match_official(p,t,n):
    """ This is their code, I used my own algorithm later because couldn't understand how start and end worked."""
    segment_length = int(round(len(p) / (n+1)))
    all_matches = set()
    for i in range(n+1):
        start = i*segment_length
        end = min((i+1)*segment_length, len(p))

        p_bm = BoyerMoore(p[start:end], alphabet='ACGT')
        matches = boyer_moore(p[start:end], p_bm, t)

        # Extend matching segments to see if whole p matches
        for m in matches:
            if m < start or m-start+len(p) > len(t):
                continue
            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            for j in range(end, len(p)):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break
            if mismatches <= n:
                all_matches.add(m - start)
    list_all_matches = list(all_matches)
    list_all_matches.sort()
    return list_all_matches

def approximate_match_bm(p, t, k, hits = False): 
    """ 
    Steps to approximate matching: 
    1. Split the P string into k + 1 substrings. 
    2. Compares each substring of the P substring to T.
    3. If at least one of those substrings have a match or matches with boyer moore, you can inspect the rest of it. 
    4. Inspect rest to see if it's a match, then append the place of the match in T. 
    """

    index_hits = 0 

    # split P string into k+1 substrings 
    # 32 // 3 = 10 
    length_of_partition = len(p) // (k+1) 

    actual_matches = set() # making it a set eliminates possibility of duplicates.

    # Compare each substring of P to T using the Boyer Moore algorithm.
    for i in range(k+1): 
        # instead of creating substrings, use indices 
        start = i * length_of_partition
        end = start + length_of_partition 
        if (len(p) - end < length_of_partition):
            end = len(p) 
        
        # apply the Boyer Moore algorithm to each substring of P. 
        p_bm = BoyerMoore(p[start:end])
        possible_matches = boyer_moore(p[start:end], p_bm, t)
        index_hits += len(possible_matches)
        
        if len(possible_matches) == 0: 
            continue 

        # for every possible match index, check if p really matches. 
        for m in possible_matches:

            # to deal with the case that the match to the segment was found at the very end of t so p would span beyond t
            if m < start or m-start+len(p) > len(t):
                continue

            mismatches = 0 
            
            # check from the start of p to the start of the matching fragment 
            for j in range(start):
                if p[j] != t[m - start + j]:
                    mismatches += 1
                    # break 
                    if mismatches > k: 
                        break 
            
            # check from the end of the matching fragment to end of p 
            for j in range(end, len(p)):

                if p[j] != t[m - start + j]:
                    mismatches += 1
                    if mismatches > k: 
                        break 

            # if the number of mistmatics is tolerated, add it to the set 
            if mismatches <= k:
                actual_matches.add(m - start)

    list_actual_matches = list(actual_matches)
    list_actual_matches.sort()

    # only return hits if specified
    if hits == False:
        return list_actual_matches
    return list_actual_matches, index_hits

def hamming_distance(x, y): 
    """ returns hamming distance (subs only). """
    subs = 0
    for i in range(len(x)):
        if x[i] != y[i]: 
            subs += 1 
    return subs 

def edit_distance(x, y):
    """ uses dynamic programming to compute edit distance. """
    D = [] # intial array 
    
    # initialize the array as rows = (x+1) by cols = (y+1) (+1 because we're counting the empty prefix)
    for i in range(len(x) + 1):
        D.append([0] * (len(y) + 1))

    # initialize first row as 0 through y+1
    for i in range(len(y) + 1):
        D[0][i] = i
    # initialize first column as 0 through x+1 
    for i in range(len(x) + 1):
        D[i][0] = i
    
    # step through and fill in the rest of the matrix (not going through the top left corner)
    # for each row... 
    for r in range(1, len(x) + 1): 
        # for each column...
        for c in range(1, len(y) + 1): 
            # check if the strings are equal at the indices corresponding to each character's row/column 
            delt = 0 if x[r-1] == y[c-1] else 1
            # evaluate the values of the top, left and diagonal choices
            top = D[r-1][c] + 1
            left = D[r][c-1] + 1
            diagonal = D[r-1][c-1] + delt 
            # new spot filled by min of all choices 
            D[r][c] = min(top, left, diagonal)

    # once done filling in the matrix, return bottom right corner value 
    return D[len(x)][len(y)]

# global alignment 

# A and G are purines
# C and T are pyrimidines
alphabet = ['A', 'C', 'G', 'T']
# penalty matrix 
# nucleotide against A, C, G, T, skip
# row A, C, G, T
penalty = [ [0, 4, 2, 4, 8], #A 
            [4, 0, 4, 2, 8], #C
            [2, 4, 0, 4, 8], #G
            [4, 2, 4, 0, 8], #T 
            [8, 8, 8, 8, 8] ] #all skips

def global_alignment(x, y):
    D = [] # intial array 
    
    # initialize the array as rows = (x+1) by cols = (y+1) (+1 because we're counting the empty prefix)
    for i in range(len(x) + 1):
        D.append([0] * (len(y) + 1))

    """ 
    Step: Initialize first row and column 
    - top right char is always 0
    - the first column should contain all skips, the penalties for skipping a character.
    - for each column value in the first row (after column 1), penalties for skipping a character. 
    """
    
    # initialize first column 
    # only 1, len(x) + 1 because top corner should be 0. e
    for i in range(1, len(x) + 1):
        D[i][0] = D[i-1][0] + penalty[alphabet.index(x[i-1])][-1]
     # initialize first row 
    for i in range(1, len(y) + 1):
        # take the character to the current character and add the penalty of a skip for that character
        D[0][i] = D[0][i-1] + penalty[-1][alphabet.index(y[i-1])]
    
    # step through and fill in the rest of the matrix (not going through the top left corner)
    # for each row... 
    for r in range(1, len(x) + 1): 
        # for each column...
        for c in range(1, len(y) + 1): 
            # evaluate the values of the top, left and diagonal choices
            top = D[r-1][c] +  penalty[alphabet.index(x[r-1])][-1] # penalty for skipping a character in y 
            left = D[r][c-1] + penalty[-1][alphabet.index(y[c-1])] # penalty for skipping a character
            diagonal = D[r-1][c-1] + penalty[alphabet.index(x[r-1])][alphabet.index(y[c-1])] # penalty for difference in char
            # new spot filled by min of all choices 
            D[r][c] = min(top, left, diagonal)

    # once done filling in the matrix, return bottom right corner value 
    return D[len(x)][len(y)]

from itertools import permutations

def overlap(a, b, min_length = 3): # min length of the overlap. 
    """ find overlap betwedn suffix of a and prefix of b. 
    Mimumum overlap must be 3 between the suffix and prefix by default.
    If the suffix and prefix overlap by less than min_length, return 0. 
    If the suffix and prefix overlap by more than min_length, return their max overlap length. """
    start = 0 # start seaching at index 0
    while True:
        # search for the first prefix substring of b (length 3) in a 
        start = a.find(b[:min_length], start) 
        # if there was no occurence of an overlap of size min_length, return 0. 
        if start == -1:
            return 0 
        # if the start is not -1, we found prefix of b in a. 
        # check that the prefix of a matches with the suffix of a (after the start occurence of b)
        if b.startswith(a[start:]):
            return len(a) - start 
        # if the prefix of b didn't match fully with the suffix of a after start, 
        # increment start so we can start searching at the next place. 
        start += 1 

def naive_overlap_map(reads, k): 
    """ Reads and min overlap length k """
    olaps = {} # dictionary of overlaps 

    """ For all pairs of reads in a set of reads, 
    calculate the overlap between a and b (with min_length = k)
    if the overlap is greater than zero, record that overlap in the dictionary. 
    """
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > 0: 
            olaps[(a, b)] = olen 
    
    return olaps 