def bounce(n):
    if n >= 0:
        print(n)
        bounce(n - 1)
        if n != 0:
            print(n)


def bounce2(n):
    print([n for n in range(n,-1,-1)] + [n for n in range(1,n+1)])



def tvarsumman(n):
    if n > 10:
        return n%10 + tvarsumman(n//10)
    else:
        return n


def tvarsumman2(n):
    nr = 0
    while n > 0:
        nr += n%10
        n //= 10
    return nr

#bounce2(3)
#print(tvarsumman2(12345))

def tvarsummancheat(n):
    print(sum([int(i) for i in str(n)]))
tvarsummancheat(12345)
