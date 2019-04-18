# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:38:53 2019

@author: jerome
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Symbolic calcul of the best grow
# =============================================================================
"""
from sympy import init_printing, Symbol, expand

a = Symbol('a')
r = (a**2-a+1)**0.5
# =============================================================================
# n = 1./3*(1+a+r)
# =============================================================================

n = (1+a+r)
bestGrow = n*(1-n)*(n-a)

print(bestGrow.expand())
print(bestGrow.diff(a))
"""






# =============================================================================
# Dynamics of DN/dt =f(N)
# =============================================================================

"""
a = 0.00000000000000001
N = [n for n in np.linspace(0, 1, 100)]
DN = np.zeros(len(N))
for i, n in enumerate(N):
    DN[i] = n*(1-n)*(n-a)
plt.plot(N, DN)
plt.plot([(1+a+(a**2-a+1)**0.5)/3], [0], "*")
plt.show()
print("best groth", np.max(DN))
"""


# =============================================================================
# freq & a
# =============================================================================

A = np.linspace(0, 1, 101)
Max = np.zeros_like(A)

for i,a in enumerate(A):
    Max[i] = 4./(27*a*(1-a)-4)
plt.plot(A, Max)
plt.fill_between(A[Max>0], 0, Max[Max>0], facecolor='blue', alpha=0.4)
plt.ylim(bottom = -10)
plt.xlabel("a")
plt.ylabel("4/(27a(1-a-4))")
plt.show()