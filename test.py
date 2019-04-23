#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:23:13 2019
"""


import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# give the line of code
#print("python says line ", cf.f_lineno)
# =============================================================================


# Create some mock data
"""
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
"""


#fig, ax1 = plt.subplots()
"""
color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
"""




# =============================================================================
# faire 2 axe y
# =============================================================================

"""
A = np.array([1,2,3])
plt.plot(A, A**2, "b")
plt.tick_params(labelcolor = 'tab:blue')

plt.twinx()
plt.plot(A, A**4, "r")
plt.tick_params(labelcolor = 'tab:red')

plt.show()
"""


# =============================================================================
# increase legend size
# =============================================================================
"""
fontsize=20
"""

"""
plt.semilogx(Ampl, V, "b", label="variability")
plt.ylabel("variability", color="blue", fontsize=20)
plt.xlabel("Scale (log scale)", fontsize=20)
plt.tick_params(labelcolor = 'tab:blue')

plt.twinx()    
plt.semilogx(Ampl, C, "orange", label="collapse probability")
plt.tick_params(labelcolor = 'tab:orange')    
plt.xlabel("Scale (log scale)", fontsize=20)
plt.ylabel("collapse probability", color = "orange", fontsize=20)

plt.title("Measures over amplitude fire\ncompute variability : "+compute_variability, fontsize=20)
plt.savefig("plot/measures/Measures_over_amplitude_fire_compute_variability_"+compute_variability)
plt.show()
"""


# =============================================================================
# cleaning plot from memory
# =============================================================================

"""
import numpy as np
import matplotlib.pyplot as plt

from memory_profiler import profile # https://pypi.python.org/pypi/memory_profiler
from memory_profiler import memory_usage

import gc # use to clean memory

"""
"""
for i in range(50):
    A = np.random.randint(10, size = 3)
    fig = plt.figure(figsize = (16, 8))
    plt.plot([1,2,3], A)
    plt.savefig("test_folder/"+str(i))
    plt.close(fig)
#    plt.gcf()
#    del fig
"""
"""

N = 500

#def do_plots():
##    fig = plt.figure()
#    fig, ax = plt.subplots()
#    ax.plot(np.random.rand(50))
#    fig.savefig('test_folder/'+str(np.random.randint(1000)))
#    plt.close()
#    fig.clear() #############################
##    plt.close(fig)


def do_plots():
    fig = plt.figure()
    image = plt.plot(np.random.rand(50))
    plt.savefig('test_folder/'+str(np.random.randint(1000)))
    plt.close()
#    fig.clear() #############################

    plt.clf()
    plt.cla()
    plt.close("all")
    plt.close(fig)
    plt.close()
    plt.show()
    del fig, image
    
    
#    plt.close(fig)


def default():
    for k in range(N):
#        print(k)
        do_plots()


def manual_gc():
    for k in range(N):
 #       print(k)
        do_plots()
        gc.collect()
#        plt.show()
#        plt.close('all')
        

print("138")
mem_default = memory_usage((default, [], {}))
print("140")
mem_manual_gc = memory_usage((manual_gc, [], {}))
print("142")
                    
                    
#plt.plot(mem_default, label='default behaviour')
plt.plot(mem_manual_gc, label='gc.collect() after close')
plt.ylabel('MB')
plt.xlabel('time (in s * 0.1)')  # `memory_usage` logs every 100ms
plt.legend()
plt.title('memory usage'    )
plt.show() 
    
"""





# =============================================================================
# New variability computation, using spline approximation
# =============================================================================
"""
from scipy import interpolate
from scipy.interpolate import UnivariateSpline

s = UnivariateSpline(O.Time, O.W)
s.set_smoothing_factor(10000)
X = np.linspace(O.Time[0], O.Time[-1], 100*len(O.Time)) # X array more accurate to have a smooth approximation
Y= s(X)
plt.plot(X, Y, label="spline")
plt.plot(O.Time, O.W, label="W")
plt.legend()
plt.show()

plt.plot(O.Time, O.W - s(O.Time))
"""





# =============================================================================
# for test the collapse probability computation
# =============================================================================

"""
numberOfSimulation = 100
Collapse = np.zeros(numberOfSimulation)
for i in range(numberOfSimulation):
    O = Ode(model = "allee_effect_adi", Init=Init, Param_phy= Param_phy, finalTime = finalTime, dt=dt, Fire_param = Fire_param)
    O.solve_by_part()
    Collapse[i] = O.get_collapse()
"""






# =============================================================================
# Measures print
# =============================================================================

"""
exec(open("variability.py").read(), globals())

print("collapse", collapse([O.N, O.W]))
print("variability_always", variability_always([O.N, O.W]))
print("variability_until", variability_until([O.N, O.W]))
print("variability_only", variability_only([O.N, O.W]))
print("variability_10", variability_10([O.N, O.W]))
#print("Collapse_10_b", collapse(Y[:,:len(Y[0])//10]))
#print("Collapse_10_m", Y[0,len(Y[0])//10])
print("variability_half", variability_half([O.N, O.W]))
print("speed_collapse", speed_collapse([O.N, O.W]))
print("viability", viability([O.N, O.W]))
print("ratio", ratio([O.N, O.W]))
print("point", point([O.N, O.W]))
"""



# =============================================================================
# Study of the time calculation
# =============================================================================

"""
t0 = tm.time()
O = Ode(model = "allee_effect_adi", Init=Init, Param_phy= Param_phy, finalTime = finalTime, dt=dt, Fire_param = Fire_param)
t1 = tm.time()
O.solve_by_part()
t2 = tm.time()
A = O.solve_by_part()
t3 = tm.time()

print("creation object", t1-t0)
print("solve", t2-t1)
print("solve and save", t3-t2)



# =============================================================================
# =============================================================================

t0 = tm.time()
for i in range(numberOfSimulation):
    O = Ode(model = "allee_effect_adi", Init=Init, Param_phy= Param_phy, finalTime = finalTime, dt=dt, Fire_param = Fire_param)
    O.solve_by_part()
t1 = tm.time()    
print("solve", t1-t0)

t0 = tm.time()
O = [[]]*numberOfSimulation
for i in range(numberOfSimulation):
    O[i] = Ode(model = "allee_effect_adi", Init=Init, Param_phy= Param_phy, finalTime = finalTime, dt=dt, Fire_param = Fire_param)
    O[i].solve_by_part()
t1 = tm.time()    
print("solve and save", t1-t0)
"""





# =============================================================================
# Afficher un arrondi
# =============================================================================
"""
n = 789.123
print("nombre arrondi : ", round(n, ndigits=1))
print("%.5f" % 0.57338244358883583)
"""


# =============================================================================
# map
# =============================================================================
"""
print(map(lambda x:x**2, [i for i in range(10)]))
"""


# =============================================================================
#
# =============================================================================



