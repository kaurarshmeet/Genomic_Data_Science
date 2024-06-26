import bisect

""" class to represent the hash table. """
class Index(object):

    """ Takes text and kmer length. """
    def __init__(self, t, k):
        self.k = k
        self.index = []

        # for evey index where you can create a kmer, 
        # add tupule to (kmer, index) to the index table
        for i in range(len(t) - k + 1):
            self.index.append( (t[i:i+k], i) )

        # sort the list of tupules (will sort kmers alphabetically)
        # alphabetical sort allows for binary search later. 
        self.index.sort()

    """ Takes read to look up in the kmer table. 
    This returns "hits" which mean the first k bases of p match with some indices in t"""
    def query(self, p, numhits = False):

        # trim to length of kmer
        kmer = p[:self.k] 

        # figure out which index the kmer is supposed to be at.
        # the tupule is compared based on natural ordering, compares first thing in the tupule first, then next 
        i = bisect.bisect_left(self.index, (kmer, -1))

        # search right of the ith index and append to hits
        # stop appending when it's not equal to the kmer anymore. 
        hits = []
        while i < len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1 
        
        if not numhits:
            return hits
        return hits, len(hits)
    
""" Takes pattern, T to match with, and an index table (from T)
You can easily get indices where the first k bases of p match the first k bases of T.
Have to do verification, check that rest of p matches. 
"""
def query_index(p, t, index, numhits = False):
    kmer_length = index.k
    offsets = [] 

    hits, numhits = index.query(p, True)

    # only consider it a valid offset if the rest of p matches with rest of t
    for i in hits:
        if p[kmer_length:] == t[i+kmer_length:i+len(p)]:
            offsets += [i]

    if not numhits:
        return offsets
    return offsets, numhits