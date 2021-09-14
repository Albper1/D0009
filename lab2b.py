#import StringIO


def derivate(f, x, h):
    return (1/(2*h))*(f(x+h)-f(x-h))
def solve(f, x0, h):
    while True:
        xi = x0 - (f(x0)/derivate(f,x0,h))
        if abs(x0 - xi) < h:
            return xi
        x0 = xi


# för redovisning
#print(solve(math.cos,8,0.00001))

#def f(n):
#    return n**2-5*n+3

#print(solve(f,5,0.00001))
