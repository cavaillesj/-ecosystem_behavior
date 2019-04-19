# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:52:17 2019

@author: jerome
"""



# =============================================================================
# first try
# =============================================================================

"""
DOSSIER = "plot/study_loop/"

Number_of_simulation = 40
numbreDePoint = 10

N0 = [0.4, 0.45, 0.5, 0.6, 0.7, 0.8]
W0 = [0., 2., 4., 6., 8., 10.]
A = [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] 
M = [0.5, 1. ,2., 4., 8., 10.]
Strength = [0.0001, 0.0002, 0.0004, 0.0007, 0.001, 0.002, 0.005, 0.008, 0.01, 0.02, 0.05, 0.1]
Alpha = [0, 10, 20, 30, 40, 50, 60]
Beta = [40, 60 ,80, 100, 120, 140, 160]
FinalTime = [10, 20, 40, 60, 80, 100]

n0_default = 0.5
w0_default = 6.
a_default = 0.4
m_default = 8.
strength_default = 0.005
alpha_default = 40
beta_default = 100
finalTime_default = 40

n0 = n0_default
w0 = w0_default
a = a_default
m = m_default
strength = strength_default
alpha = alpha_default
beta = beta_default
finalTime = finalTime_default

Param = {"n0":N0,
        "w0":W0,
        "a":A,
        "m":M,
        "strength":Strength,
        "alpha":Alpha,
        "beta":Beta,
        "finalTime":FinalTime}

Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1
"""


# =============================================================================
# better param
# =============================================================================
"""
DOSSIER = "../plot/study_loop_2/"
"""

Number_of_simulation = 40
numbreDePoint = 10

N0 = [0.4, 0.45, 0.5, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.8]
W0 = [0., 2., 4., 6., 8., 10.]
A = [0., 0.1, 0.2, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.5, 0.6, 0.7] 
M = [0.2, 0.4, 0.6, 0.8, 1., 1.2, 1.4, 1.6, 1.8 ,2., 4., 4.5, 5., 5.5, 6., 6.5, 7., 7.5, 8., 10.]
Strength = [0.00001, 0.00002, 0.00004, 0.00007, 0.0001, 0.0002, 0.0004, 0.0008, 0.001, 0.002, 0.005, 0.01]
Alpha = [0, 2, 4, 6, 8, 10, 20, 30, 40, 50, 60] 
Beta = [20, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200]
FinalTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 60, 80, 100]





# Old param 0
"""
n0_default = 0.5
w0_default = 6.
a_default = 0.4
m_default = 10.
strength_default = 0.0004
alpha_default = 10
beta_default = 100
finalTime_default = 40
"""

# param 1
"""
n0_default = 0.5
w0_default = 0
a_default = 0.4
m_default = 12.
strength_default = 0.001
alpha_default = 10
beta_default = 70
finalTime_default = 100
"""

# param 2
"""
n0_default = 0.5
w0_default = 10
a_default = 0.4
m_default = 6.
strength_default = 0.0005
alpha_default = 50
beta_default = 70
finalTime_default = 100
"""
# =============================================================================
#    study loop 3 
# =============================================================================

"""
DOSSIER = "../plot/study_loop_3/"

Strength = [0.0000001, 0.0000002, 0.0000004, 0.0000007, 0.000001, 0.000002, 0.000004, 0.000007, 0.00001, 0.00002, 0.00004, 0.00007, 0.0001, 0.0002, 0.0004, 0.0008, 0.001, 0.002, 0.005, 0.01]
    
n0_default = 0.5
w0_default = 10
finalTime_default = 100
a_default = 0.4
m_default = 6.
strength_default = 0.0005
alpha_default = 50
beta_default = 70
"""


# =============================================================================
# Study loop 4, calibration on the cross point on the strength impact
# =============================================================================
"""
DOSSIER = "../plot/study_loop_4/"

Strength = [0.0000001, 0.0000002, 0.0000004, 0.0000007, 0.000001, 0.000002, 0.000004, 0.000007, 0.00001, 0.00002, 0.00004, 0.00007, 0.0001, 0.0002, 0.0004, 0.0008, 0.001, 0.002, 0.005, 0.01]
M = [0.2, 0.4, 0.6, 0.8, 1., 1.2, 1.4, 1.6, 1.8, 1.8, 1.9, 1.92, 1.94, 1.96, 1.98, 2., 2.005, 2.01, 2.015, 2.02, 2.025, 2.03, 2.035, 2.04, 2.045, 2.05, 2.055, 2.06, 2.065, 2.07, 2.075, 2.08, 2.085, 2.09, 2.095, 2.1, 2.2, 2.3, 2.4, 2.6, 2.8, 3., 4., 4.5, 5., 5.5, 6., 6.5, 7., 7.5, 8., 10.]

n0_default = 0.5
w0_default = 10
finalTime_default = 100
a_default = 0.4
m_default = 6.
strength_default = 2*10**-5
alpha_default = 50
beta_default = 70


n0 = n0_default
w0 = w0_default
a = a_default
m = m_default
strength = strength_default
alpha = alpha_default
beta = beta_default
finalTime = finalTime_default

Param = {"n0":N0,
        "w0":W0,
        "a":A,
        "m":M,
        "strength":Strength,
        "alpha":Alpha,
        "beta":Beta,
        "finalTime":FinalTime}

Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1

"""



# =============================================================================
# Study loop 4, calibration on the cross point on the strength impact
# =============================================================================
"""
DOSSIER = "../plot/study_loop_5/"

Strength = [0.0000001, 0.0000002, 0.0000004, 0.0000007, 0.000001, 0.000002, 0.000004, 0.000007, 0.00001, 0.00002, 0.00004, 0.00007, 0.0001, 0.0002, 0.0004, 0.0008, 0.001, 0.002, 0.005, 0.01]
M = [0.2, 0.4, 0.6, 0.8, 1., 1.2, 1.4, 1.6, 1.8, 1.8, 1.9, 1.92, 1.94, 1.96, 1.98, 2., 2.005, 2.01, 2.015, 2.02, 2.025, 2.03, 2.035, 2.04, 2.045, 2.05, 2.055, 2.06, 2.065, 2.07, 2.075, 2.08, 2.085, 2.09, 2.095, 2.1, 2.2, 2.3, 2.4, 2.6, 2.8, 3., 4., 4.5, 5., 5.5, 6., 6.5, 7., 7.5, 8., 10.]

Alpha = [ 0 ,  2 ,  4 ,  6 ,  8 , 10 , 20 , 30 , 35 , 38 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50 , 50.5, 51 , 51.5, 52 , 52.5, 53 , 54 , 55 , 56 , 58 , 60]
Beta = np.array([ 20,  40,  50,  53,  55,  56,  57,  58,  59,  60,  61,  62,  63,64,  65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76, 77,  78,  79,  80,  90, 100, 110, 120, 130, 140, 150, 160, 180, 200])

FinalTime = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 60, 70, 75, 78, 79, 80, 81, 82, 83, 84, 85, 87, 90, 95, 100]


# =============================================================================
# FUSIONNER LES ALPHA ET BETA
# =============================================================================

n0_default = 0.5
w0_default = 10
finalTime_default = 100
a_default = 0.4
m_default = 2.02
strength_default = 2*10**-5
alpha_default = 50
beta_default = 70


n0 = n0_default
w0 = w0_default
a = a_default
m = m_default
strength = strength_default
alpha = alpha_default
beta = beta_default
finalTime = finalTime_default

Param = {"n0":N0,
        "w0":W0,
        "a":A,
        "m":M,
        "strength":Strength,
        "alpha":Alpha,
        "beta":Beta,
        "finalTime":FinalTime}

Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1
"""

# =============================================================================
# Study loop 6, new measures, and other correction see simulation 21
# =============================================================================
DOSSIER = "../plot/study_loop_6/"

#A = [0., 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9] 
#M = [0.5, 1., 2., 4., 8.]
M = [0.1, 0.3, 0.6, 0.7, 0.8, 0.9, 1.5]

#Strength = [0.00005, 0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02]
Strength = [0.0003, 0.0004, 0.0006, 0.0007, 0.0008, 0.0009, 0.0015]

#Alpha = [1, 2, 5, 10, 20, 40]
Alpha  = [3, 4, 6, 7, 8, 9]

#Beta = np.array([0.5, 1., 2., 4., 8.])
Beta = [0.1, 0.2, 0.3, 0.4, 0.7]

FinalTime = [2, 4, 6, 8, 10, 20, 40, 60, 80, 100]

tot = len(A)+len(M)+len(Strength)+len(Alpha)+len(Beta)+len(FinalTime)

n0_default = 1.
w0_default = 0.    # equilibirum or not ??
finalTime_default = 100
a_default = 0.2
m_default = 2.
strength_default = 0.002
alpha_default = 20
beta_default = 2.


n0 = n0_default
w0 = w0_default
a = a_default
m = m_default
strength = strength_default
alpha = alpha_default
beta = beta_default
finalTime = finalTime_default

Param = {"n0":N0,
        "w0":W0,
        "a":A,
        "m":M,
        "strength":Strength,
        "alpha":Alpha,
        "beta":Beta,
        "finalTime":FinalTime}

Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1
