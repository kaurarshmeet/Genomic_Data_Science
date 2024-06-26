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