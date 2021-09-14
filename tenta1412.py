def delete(s):
    switch = 0
    new_str = ""
    for i in range(len(s)):
        if s[i] == "t":
            if switch==0:
                new_str += "t"
                switch = 1
            else:
                new_str += "T"
                switch = 0
        else:
            new_str += s[i]
    return new_str

print(delete("iterationstentamen"))
print(delete("stor"))

def subtract(n,seq):

    if not seq:
        return n
    else:
        return subtract(n-seq[0],seq[1:])

print(subtract(10, [1,2,3,3]))
