# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:21:25 2019

@author: jerome
"""

import numpy as np



# =============================================================================
# def variability(Y):
#     """one among different way to compute the variability"""
#     N, W = Y
#     return np.var([N, W])
# 
# def collapse(Y):
#     eps = 1e-3
#     N, W = Y
#     if(N[-1] < eps):
#         return True
#     else:
#         return False
# 
# 
# def variability_collapse_until(Y):
#     """return both variability (compute until it collapse) and collapse"""
#     N, W = Y
#     eps = 1e-3 # seuil
#     time_extinction = np.argmax(N < eps)
#     if(N[-1] < eps):
#         c = True
#         v = np.var([N[:time_extinction], W[:time_extinction]])
#     else:
#         c = False
#         v = np.var([N, W])
#     return v, c
# 
# 
# 
# def variability_collapse_only(Y):
#     """return both variability (compute only if it not collapse) and collapse"""
#     eps = 1e-3
#     N, W = Y
#     if(N[-1] < eps):
#         c = True
#         v = np.NaN
#     else:
#         c = False
#         v = np.var([N, W])
#     return v, c
# 
# 
# def variability_collapse_10(Y):
#     """return both variability (just for the 10% interval of the time study) and collapse"""
#     N, W = Y
#     eps = 1e-3 # seuil
#     if(N[-1] < eps):
#         c = True
#         v = np.var([N[:len(N)//10], W[:len(N)//10]])
#     else:
#         c = False
#         v = np.var([N, W])
#     return v, c
# =============================================================================


# =============================================================================
#   compute measure separately
# =============================================================================
    
def collapse(Y):
    eps = 1e-3
    N, W = Y
    if(N[-1] < eps):
        return True
    else:
        return False
    
# =============================================================================
# def collapse(Y):
#     eps = 1e-3
#     N, W = Y
#     if(N[-1] < eps):
#         return True
#     else:
#         return False
# =============================================================================

eps = 1e-3 # perhaps 1e-2 is enough better ...

def variability_always(Y):
    """one among different way to compute the variability"""
    N, W = Y
    return np.var([N, W])



def variability_until(Y, eps = eps):
    """return both variability (compute until it collapse) and collapse"""
    N, W = Y
    time_extinction = np.argmax(N < eps)
    if(N[-1] < eps):
        v = np.var([N[:time_extinction], W[:time_extinction]])
    else:
        v = np.var([N, W])
    return v



def variability_only(Y, eps = eps):
    """return both variability (compute only if it not collapse) and collapse"""
    N, W = Y
    if(N[-1] < eps):
        v = np.NaN
    else:
        v = np.var([N, W])
    return v


def variability_10(Y, eps = eps):
    """return both variability (just between the first 10% and 20% interval of the time study) and collapse"""
    N, W = Y
    if(N[-1] < eps):
        v = np.var([N[len(N)//10: len(N)//5], W[len(N)//10: len(N)//5]])
    else:
        v = np.var([N, W])
    return v



def variability_half(Y, eps = eps):
    """return both variability (compute until it collapse) and collapse"""
    N, W = Y
     # seuil
    if(N[-1] < eps):    
        time_extinction = np.argmax(N < eps)    
    else: # they are no extinction
        time_extinction = len(N)#//2
    final_time_variability_computation = time_extinction // 2
    average = np.mean(W[:final_time_variability_computation])
    initial_time_variability_computation = np.argmax(W < average)
    
    if(final_time_variability_computation - initial_time_variability_computation >= 0.1*len(N)): # need enough data to make relevent computation
        return np.var([W[initial_time_variability_computation:final_time_variability_computation], W[initial_time_variability_computation:final_time_variability_computation]])
    else:
        return np.NaN
        
    
    
def speed_collapse(Y, eps = eps):
    """depend of dt !!!!!"""               # need to change the computation !!
#   ALSO, we could use the allee parameter to know chen the collapse begin instead to the average ....
    N, W = Y
    i0 = 0
    if(N[-1] < eps): # collapse
        i3 = np.argmax(N < eps)
        if(i3 < 2):
            return np.NaN
        else:
            average = np.mean(N[:i3//2])
        i1 = np.argmax(N < average)
        if(i3-i1 > 0.1*len(N)):
            i2 = len(N) - np.argmax((N > average)[::-1])
            return 1. / (i3 - i2)
        else:
            return np.NaN
#        print("i0=", i0, "i1=", i1, "i2=", i2, "i3=", i3)
    else: # no collapse
        return np.NaN
    
    
    

def viability(Y, eps = eps):
    """depend of dt !!!!!"""               # need to change the computation !!
    N, W = Y
    i0 = 0
    if(N[-1] < eps): # collapse
        i3 = np.argmax(N < eps)
        if(i3 < 2):
            return np.NaN
        else:
            average = np.mean(N[:i3//2])
        i1 = np.argmax(N < average)
        if(i3-i1 > 0.1*len(N)):
            i2 = len(N) - np.argmax((N > average)[::-1])
            return (i2-i1)/(i3-i0)
        else:
            return 0
#        print("i0=", i0, "i1=", i1, "i2=", i2, "i3=", i3)
    else: # no collapse
        return 1

     
    


def ratio(Y, eps = eps):
    """we assume we begin at the equilibrium, that the case in the study for now ..."""
    N, W = Y
    if(N[-1] < eps): # collapse
        i3 = np.argmax(-N < eps)
        if(i3 < 0.1*len(N)):
            return 0
    else:
        i3 = len(N)
    average = np.mean(W[:i3//2])
    return average/W[0]




def point(Y, eps = eps):
    """depend of dt !!!!!"""               # need to change the computation !!
    N, W = Y
    i0 = 0
    if(N[-1] < eps): # collapse
        i3 = np.argmax(N < eps)
        if(i3 < 2):
            return np.NaN
        else:
            average = np.mean(N[:i3//2])
        i1 = np.argmax(N < average)
        if(i3-i1 > 0.1*len(N)):
            i2 = len(N) - np.argmax((N > average)[::-1])
            return W[(i3-i2)//2]
        else:
            return np.NaN
#        print("i0=", i0, "i1=", i1, "i2=", i2, "i3=", i3)
    else: # no collapse
        return W[len(W)//2]    
    
    
def time_rotation_N(Y, eps = eps):
    N, W = Y
    i0 = 0
    if(N[-1] < eps): # collapse
        i3 = np.argmax(N < eps)
        if(i3 < 2):
            return np.NaN
        else:
            averageN = np.mean(N[:i3//2]) 
    else:
        averageN = np.mean(N[len(N)//2]) 
#    print("averageN", averageN, "averageW", averageW)
    
    if(N[-1] < eps):
        varN = sum(abs(N[:i3-1:] - N[1:i3:]))
    else:
        varN = sum(abs(N[:-1:] - N[1::]))
    return varN/(2*averageN)
        

def time_rotation_W(Y, eps = eps):
    N, W = Y
    i0 = 0
    if(N[-1] < eps): # collapse
        i3 = np.argmax(N < eps)
        if(i3 < 2):
            return np.NaN
        else:
            averageW = np.mean(W[:i3//2]) 
    else:
        averageW = np.mean(W[len(W)//2]) 
#    print("averageN", averageN, "averageW", averageW)
    
    if(N[-1] < eps):
        varW = sum(abs(W[:i3-1:] - W[1:i3:]))
    else:
        varW = sum(abs(W[:-1:] - W[1::]))
    return varW/(2*averageW)

    
    

def all_measure(Number_of_simulation = 100, mean = True, **kwargs):
    """solve the system several times with different perturbation in order to make an average"""
    ##### Number_of_simulation : between 10 and 1000 usually 100
    Collapse = np.zeros(Number_of_simulation)
    Variability_always = np.zeros_like(Collapse)
    Variability_until = np.zeros_like(Collapse)
    Variability_only = np.zeros_like(Collapse)
    Variability_10 = np.zeros_like(Collapse)
    Collapse_10_b = np.zeros_like(Collapse)
    Collapse_10_m = np.zeros_like(Collapse)
    Variability_half = np.zeros_like(Collapse)
    Speed_collapse = np.zeros_like(Collapse)
    Viability = np.zeros_like(Collapse)
    Ratio = np.zeros_like(Collapse)
    Point = np.zeros_like(Collapse)
    Time_rotation_N = np.zeros_like(Collapse)
    Time_rotation_W = np.zeros_like(Collapse)    

    """
    DOSSIER = "plot/measures/coupled/test/"
    name = "a="+str(kwargs["Param_phy"][0])+"_m="+str(kwargs["Param_phy"][1])+"_strength="+str(kwargs["Fire_param"]["Param_strength"]["scale"])+"_alpha="+str(kwargs["Fire_param"]["Param_coupled"]["alpha"])+"_beta="+str(kwargs["Fire_param"]["Param_coupled"]["beta"])
    name = name.replace(".", "_")
    print("name", name) #rajouter alpha and beta
    """
    
    for i in range(Number_of_simulation):
        O = Ode(**kwargs)
        Y = O.solve_by_part()
        """
#        plt.figure(figsize=(16.8))
        name_s = DOSSIER+name+"_simu="+str(i)+".png"
#        print("262", name)
#        O.plot_time_series(show = False, save_name = name)
        O.plot_time_series(show = True, name=name_s)
#        plt.savefig(DOSSIER+name+"_simu="+str(i)+".png")
        """
        # measures
        Collapse[i] = collapse(Y)
        Variability_always[i] = variability_always(Y)
        Variability_until[i] = variability_until(Y)
        Variability_only[i] = variability_only(Y)
        Variability_10[i] = variability_10(Y)
        Collapse_10_b[i] = collapse(Y[:,:len(Y[0])//10])
        Collapse_10_m[i] = Y[0,len(Y[0])//10]
        Variability_half = variability_half(Y)
        Speed_collapse = speed_collapse(Y)
        Viability = viability(Y)
        Ratio = ratio(Y)
        Point = point(Y)
        Time_rotation_N  = time_rotation_N(Y)
        Time_rotation_W  = time_rotation_W(Y)
    if(mean):
        return np.nanmean(Collapse), np.nanmean(Variability_always), np.nanmean(Variability_until), np.nanmean(Variability_only), np.nanmean(Variability_10), np.nanmean(Collapse_10_b), np.nanmean(Collapse_10_m), np.nanmean(Variability_half), np.nanmean(Speed_collapse), np.nanmean(Viability), np.nanmean(Ratio), np.nanmean(Point), np.nanmean(Time_rotation_N), np.nanmean(Time_rotation_W)
    else:
        return Collapse, Variability_always, Variability_until, Variability_only, Variability_10, Collapse_10_b, Collapse_10_m, Variability_half, Speed_collapse, Viability, Ratio, Point, Time_rotation_N, Time_rotation_W
    
    
    

def exemples(name, Number_of_simulation = 100, mean = True, **kwargs):
    name = name+"_freq="+str(kwargs["Fire_param"]["param_freq"]["p"])+".png"
    O = Ode(**kwargs)
    Y = O.solve_by_part()
    O.plot_time_series(save = True, name = name, generation = True, show = False)
    return Y
    