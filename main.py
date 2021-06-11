# learning physics through programming

import numpy as np

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

def q(i,j=0):
    rng = np.random.default_rng(j)

    eq1 = rng.integers(low=-10, high=10, size=3)
    eq2 = rng.integers(low=-10, high=10, size=3)
    a = np.array([[eq1[0],eq1[1]],[eq2[0],eq2[1]]])
    b = np.array([eq1[2],eq2[2]])
    x = np.linalg.solve(a,b)

    print(f'problem {i}:')
    print(f'{ii(a[0][0])}{a[0][0]}x {s(a[0][1])} {abs(a[0][1])}y = {b[0]}')
    print(f'{ii(a[1][0])}{a[1][0]}x {s(a[1][1])} {abs(a[1][1])}y = {b[1]}')

    if h:
        print(f'solution {i}:')
        print(f'x = {x[0]:.2}, y = {x[1]:.2}')
    print()





if __name__ == "__main__":
    print('main')
    n = 4
    j = 1
    h = False
    for i in range(4):
        q(i,j)

