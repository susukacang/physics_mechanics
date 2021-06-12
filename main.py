# learning physics through programming

import numpy as np
import random

# sign
def s(a):
    if a < 0:        
        return '-'
    else:
        return '+'
# indent
def ii(a):
    if a < 0:        
        return ''
    else:
        return ' '    

def q(i,j=0, h=True):
    rng = np.random.default_rng(random.randint(0,j))

    eq1 = rng.integers(low=-10, high=10, size=3)
    eq2 = rng.integers(low=-10, high=10, size=3)
    a = np.array([[eq1[0],eq1[1]],[eq2[0],eq2[1]]])
    b = np.array([eq1[2],eq2[2]])
    x = np.linalg.solve(a,b)
    x = x.round(3)

    print(f'problem {i}:')
    # print(f'{ii(a[0][0])}{a[0][0]}x {s(a[0][1])} {abs(a[0][1])}y = {b[0]}')
    # print(f'{ii(a[1][0])}{a[1][0]}x {s(a[1][1])} {abs(a[1][1])}y = {b[1]}')
    print(f'{a[0][0]}x + {(a[0][1])}y = {b[0]}')
    print(f'{a[1][0]}x + {(a[1][1])}y = {b[1]}')

    if h:
        print(f'solution {i}:')
        print(f'x = {x[0]:.2}, y = {x[1]:.2}')
    print()

    eq=[]
    eq.append(ii(a[0][0]) + str(a[0][0]) + "x " + str(s(a[0][1])) + " " + str(abs(a[0][1])) + "y" + " = " + str(b[0]))
    eq.append(ii(a[1][0]) + str(a[1][0]) + "x " + str(s(a[1][1])) + " " + str(abs(a[1][1])) + "y" + " = " + str(b[1]))
    sol = 'x = ' + str(x[0]) + ', ' + 'y = ' + str(x[1])

    print(eq)

    eq.append(sol)
    return {"eq": eq}
    # return {"a":a.tolist(),"b":b.tolist(),"x":x.tolist()}

def p(n=4):
    e = []
    r = 1
    # use r as seed if need control i.e. use datetime as seed
    random.seed()
    h = True
    for i in range(n):
        j = random.randint(0,99)
        _q = q(i,j,h)
        e.append(_q)
    print(e)
    return e



if __name__ == "__main__":
    print('main')
    n = 6
    r = 1
    random.seed(r)
    h = True
    for i in range(n):
        j = random.randint(0,99)
        q(i,j,h)
        

