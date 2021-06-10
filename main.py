# learning physics through programming

import numpy as np

def s(a):
    if a < 0:        
        return '-'
    else:
        return '+'

def q(i):
    rng = np.random.default_rng()

    eq1 = rng.integers(low=-10, high=10, size=3)
    eq2 = rng.integers(low=-10, high=10, size=3)
    a = np.array([[eq1[0],eq1[1]],[eq2[0],eq2[1]]])
    b = np.array([eq1[2],eq2[2]])
    x = np.linalg.solve(a,b)

    print(f'problem {i}:')
    print(f'{a[0][0]}x {s(a[0][1])} {abs(a[0][1])}y = {b[0]}')
    print(f'{a[1][0]}x {s(a[1][1])} {abs(a[1][1])}y = {b[1]}')

    print(f'solution {i}:')
    print(f'x = {x[0]:.2}, y = {x[1]:.2}')
    print()


n = 4

for i in range(4):
    q(i)

# print(eq1)
# print(eq2)
# print(a)
# print(b)
# n = np.array([[1,2,3],[4,5,6]])




