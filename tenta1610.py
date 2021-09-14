import sys
def minAndMax(seq):

    return minAndMaxHelper(seq,sys.maxsize,-sys.maxsize)

def minAndMaxHelper(seq,min_v,max_v):

    if not seq:
        return (min_v,max_v)
    min_v = min(min_v,seq[0])
    max_v = max(max_v,seq[0])
    return minAndMaxHelper(seq[1:],min_v,max_v)


print(minAndMax([1,5,6,2,3,9,8,1,8]))
