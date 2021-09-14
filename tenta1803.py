def flatten(seq):

    if not seq: #ifall längden av listan är 0
        return seq
    elif isinstance(seq[0],list):
        return flatten(seq[0]) + flatten(seq[1:])
    else:
        return [seq[0]] + flatten(seq[1:])


print(flatten([[1,[3,[2]]],[4,1],[8,[9,3]]]))
