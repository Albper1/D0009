"""def findRev(s1,s2,n):
    temp = ""
    for i in range(len(s2)-1,-1,-1):
        temp += s2[i]
    s2 = temp
    for i in range(len(s1)-1):
        if s1[i:i+len(s2)] == s2:
            return i
    return n


#print(findRev("Fin sensommardag", "mos", 40))
#print(findRev("Fin sensommardag", "abc", 40))
"""
def sumPart(l1,l2):
    if not l1 or l1==l2:
        return 0
    else:
        if l1[0] not in l2:
            return l1[0] + sumPart(l1[1:],l2)
        else:
            return sumPart(l1[1:],l2)

print(sumPart([4,6,2,9,8], [4,9]))
