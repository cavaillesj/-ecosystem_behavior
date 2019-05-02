# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:08:06 2019

@author: jerome
"""



# =============================================================================
# param 1
# =============================================================================


"""
A = [0.2, 0.4, 0.6]
M = [0.5, 1., 1.5]
Alpha = [2, 4, 7, 10]
Beta = [2, 4, 7, 10]
Strength = [0.01, 0.05, 0.1]
"""



# =============================================================================
#   Second try
# =============================================================================


"""
DOSSIER = "plot/param2/"

A = [0.2, 0.4]
M = [5., 7., 9.]
Strength = [0.001, 0.005, 0.01]
Alpha = [2, 7, 15, 28]
Beta = [5, 15, 50, 200]
"""


# =============================================================================
#   Third try
# =============================================================================

"""
DOSSIER = "plot/param3/"

A = [0.1, 0.3, 0.5]
M = [4., 7., 10.]
Strength = [0.005, 0.01, 0.05, 0.1]
Alpha = [4, 15, 28]
Beta = [4, 15, 50, 200]


Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability"]
"""

# =============================================================================
#   Object save
# =============================================================================

"""
DOSSIER = "plot/param4/"

A = [0.1, 0.3, 0.5]
M = [4., 7., 10.]
Strength = [0.005, 0.01, 0.05, 0.1]
Alpha = [4, 15, 28]
Beta = [4, 15, 50, 200]

Freq = [0.005, 0.1, 0.3, 0.5, 1., 3., 5., 9.]

#Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability"]
"""

# =============================================================================
# =============================================================================

"""
DOSSIER = "plot/param5/"

A = [0.1, 0.3, 0.5]################## surrpimer 0.1
M = [4., 7., 10.]
Strength = [0.005, 0.01, 0.05, 0.1]
Alpha = [4, 15, 28]
Beta = [4, 15, 50, 200]

Freq = [0.005, 0.1, 0.3, 0.5, 1., 3., 5., 9.]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio"]
"""

# =============================================================================
# =============================================================================

"""
DOSSIER = "plot/param6/"

A = [0.3, 0.5]################## surrpimer 0.1
M = [4., 7., 10.]
Strength = [0.001, 0.005, 0.01, 0.05]
Alpha = [4, 15, 28]
Beta = [10, 50, 200]

Freq = [0.005, 0.1, 0.3, 0.5, 1., 3., 5., 9.]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio"]
"""


# =============================================================================
# correction measures andnew measure : point
# =============================================================================

"""
DOSSIER = "plot/param7/"

A = [0.3, 0.5]################## surrpimer 0.1
M = [4., 7., 10.]
Strength = [0.001, 0.005, 0.01, 0.05]
Alpha = [4, 15, 28]
Beta = [10, 50, 200]

Freq = [0.005, 0.1, 0.3, 0.5, 1., 3., 5., 9.]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point"]
"""

# =============================================================================
# TEST
# =============================================================================

"""
DOSSIER = "plot/test/"

A = [0.5]################## surrpimer 0.1
M = [10.]
Strength = [0.005]
Alpha = [15]
Beta = [50]

Freq = [0.005, 0.1, 0.3, 0.5, 1., 3., 5., 9.]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point"]
"""



# =============================================================================
# param 8 : long time study (100 instead to 10)
# =============================================================================

"""
DOSSIER = "plot/param8/"

A = [0.3, 0.5] 
M = [4., 7., 10.]
Strength = [0.001, 0.005, 0.01, 0.05]
Alpha = [4, 15, 28]
Beta = [10, 50, 200]

Freq = [0.005, 0.1, 0.3, 0.5, 1., 3., 5., 9.]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point"]
"""



# =============================================================================
# param 9 : long time study (100 instead to 10) with range parameter adapted
# =============================================================================

"""
DOSSIER = "plot/param9/"

A = [0.3, 0.5] 
M = [3., 6., 9.]
Strength = [0.001, 0.002, 0.005, 0.008, 0.01]
Alpha = [8, 15, 25]
Beta = [30, 70, 200]
Freq = [0.005, 0.02, 0.1, 0.3, 0.5, 1., 4., 9.]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point"]
"""



# =============================================================================
# param 10 : final time as a parameter
# =============================================================================

"""
DOSSIER = "plot/param10/"

A = [0.3, 0.5] 
M = [2., 4., 7., 10.] # [2., 5., 10.]
Strength = [0.001, 0.002, 0.005, 0.008, 0.01]
Alpha = [8, 15, 25]
Beta = [5, 20, 40, 100]
Freq = [0.005, 0.02, 0.1, 0.3, 0.6, 1., 2., 4., 6., 9.]
FinalTime = [10, 40, 100]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point"]
"""

# =============================================================================
# param 11 : final time and initial point as a parameter
# =============================================================================

"""
DOSSIER = "plot/param11/"


N0 = [0.5]
W0 = [0, 4., 10.]

A = [0.3, 0.5] 
M = [2., 4., 7., 10.] # [2., 5., 10.]
Strength = [0.001, 0.002, 0.005, 0.008, 0.01]
Alpha = [8, 15, 25]
Beta = [5, 20, 40, 100]
Freq = [0.005, 0.02, 0.1, 0.3, 0.6, 1., 2., 4., 6., 9.]
#FinalTime = [10, 40, 100]
FinalTime = [10]


Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point", "Time_rotation_N", "Time_rotation_W"]
"""

# =============================================================================
# param 12 : final time and initial point as a parameter and with time series
# =============================================================================

"""
DOSSIER = "plot/param12/"


N0 = [0.5]
W0 = [0, 4., 10.]

A = [0.3, 0.5] 
M = [2., 4., 7., 10.] # [2., 5., 10.]
Strength = [0.001, 0.002, 0.005, 0.008, 0.01]
Alpha = [8, 15, 25]
Beta = [5, 20, 40, 100]
Freq = [0.005, 0.02, 0.1, 0.3, 0.6, 1., 2., 4., 6., 9.]
#FinalTime = [10, 40, 100]
FinalTime = [10]


Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point", "Time_rotation_N", "Time_rotation_W"]
"""

# =============================================================================
# param 13 : New plot measures against freq
# =============================================================================

"""
DOSSIER = "plot/param13/"
Number_of_simulation = 40
numbreDePoint = 10

#Freq = [0.005, 0.1, 0.3, 0.5, 1., 3., 5., 9.]
dt = 0.1
#finalTime = 100


N0 = [0.5]
#W0 = [0, 4., 10.]
W0 = [5.]
#A = [0.3, 0.5] 
A = [0.4] 
M = [7., 10.] # [2., 5., 10.]
Strength = [0.002, 0.005, 0.008]
Alpha = [20, 30]
Beta = [80, 120]
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
#FinalTime = [10, 40, 100]
FinalTime = [20,50]


Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point", "Time_rotation_N", "Time_rotation_W"]
"""

# =============================================================================
# param 14 : Just more parameter (and long time study)
# =============================================================================

"""
DOSSIER = "plot/param14/"
Number_of_simulation = 40
numbreDePoint = 10

N0 = [0.5]
W0 = [0, 4., 10.]
A = [0.4] 
M = [6., 8., 10., 12.] # [2., 5., 10.]
Strength = [0.005, 0.001, 0.002, 0.005, 0.008, 0.01, 0.02]
Alpha = [10, 20, 30, 50]
Beta = [30, 60, 90, 120]
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1
FinalTime = [100]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point", "Time_rotation_N", "Time_rotation_W"]
"""



# =============================================================================
# param 15 : Better param (for the summary)
# =============================================================================

"""
DOSSIER = "../plot/param15/"
Number_of_simulation = 40
numbreDePoint = 10

N0 = [0.5]
W0 = [0, 10.]
A = [0.4] 
M = [6., 8., 10., 12.] # [2., 5., 10.]
Strength = [0.0001, 0.0005, 0.001, 0.002, 0.005, 0.008, 0.01]
Alpha = [10, 30, 50]
Beta = [30, 70, 120]
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1
FinalTime = [10, 30, 100]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point", "Time_rotation_N", "Time_rotation_W"]
"""



# =============================================================================
# param 16 : searching when the loop turn in the other side
# =============================================================================

"""
DOSSIER = "../plot/param16/"
Number_of_simulation = 40
numbreDePoint = 10

N0 = [0.5]
W0 = [10.]
A = [0.4] 
M = [6.] # [2., 5., 10.]
Strength = [0.000001, 0.000002, 0.000005, 0.00001, 0.00002, 0.00005, 0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.008, 0.01]
Alpha = [50]
Beta = [70]
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1
FinalTime = [100]

Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point", "Time_rotation_N", "Time_rotation_W"]
"""


# =============================================================================
# param 17 : computation of the variability with both N and W (not only W)
# =============================================================================

"""
DOSSIER = "../plot/param17/"
Number_of_simulation = 40
numbreDePoint = 10



N0 = [0.5]
W0 = [6.]
A = [0.4] 
M = [6., 8., 10., 12.] # [2., 5., 10.]
Strength = [0.000001, 0.000002, 0.000005, 0.00001, 0.00002, 0.00005, 0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.008, 0.01]
Alpha = [10, 30, 50]
Beta = [30, 70, 120]
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1
FinalTime = [100]
Variability = ["Variability_always", "Variability_until", "Variability_only", "Variability_10", "Variability_half", "Speed_collapse", "Viability", "Ratio", "Point", "Time_rotation_N", "Time_rotation_W"]
"""



# =============================================================================
# param 18 : New computation of the measures, we keep the same param to check if the measures is more consistent
# =============================================================================

"""
DOSSIER = "../plot/param18/"
Number_of_simulation = 40
numbreDePoint = 10

N0 = [0.5]
W0 = [6.]
A = [0.4] 
M = [6., 8., 10., 12.] # [2., 5., 10.]
Strength = [0.000001, 0.000002, 0.000005, 0.00001, 0.00002, 0.00005, 0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.008, 0.01]
Alpha = [10, 30, 50]
Beta = [30, 70, 120]
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1
FinalTime = [100]
Variability = ["Variability"]
"""


# =============================================================================
# param 19 : New computation of the measures, and other variability (alaways, tr10 et tr0)
# =============================================================================

"""
DOSSIER = "../plot/param19/"
Number_of_simulation = 40
numbreDePoint = 10



N0 = [0.5]
W0 = [6.]  # 00000000000000
A = [0.1, 0.4] 
M = [2., 10.] # [2., 5., 10.]
Strength = [0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005]
Alpha = [20, 40]
Beta = [50, 90]
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 7., 9.]
dt = 0.1
FinalTime = [100]
Variability = ["Variability_always", "Variability_tr10", "Variability_tr0"]
"""


# =============================================================================
# param 20 : WHEN W is all burned => fire stop 
# =============================================================================

"""
DOSSIER = "../plot/param20/"
Number_of_simulation = 100
numbreDePoint = 10



N0 = [0.5]
W0 = [0.]
A = [0.1, 0.4] 
M = [2., 10.] # [2., 5., 10.]
Strength = [0.0005, 0.001, 0.002, 0.005]
Alpha = [20, 40]
Beta = [2., 10., 50.]
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 3., 5., 6., 7., 8., 9.]
dt = 0.02
FinalTime = [100]
Variability = ["Variability_always", "Variability_tr10", "Variability_tr0"]
"""





# =============================================================================
# param 21 : WHEN W is all burned => fire stop 
#
#- adaptative dt
#- commencer à l'eq stable
#- different variability
#- different collapse (collapse proba and collapse proba per time unit)
#- different application to the variability
# =============================================================================

"""
DOSSIER = "../plot/param21/"
Number_of_simulation = 40
numbreDePoint = 10



N0 = [1.0]
W0 = [2.0]

A = [0.1, 0.4] 
M = [2., 10.] # [2., 5., 10.]
Strength = [0.0005, 0.001, 0.002, 0.005]
Alpha = [20, 40]
Beta = [2., 10., 50.] # DECREASE !
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 4., 7., 9.]

#dt = 0.02
FinalTime = [100]

Collapse = ["Collapse_proba", "Collapse_proba_per_time_unit"]
Applicant = ["N", "W", "NW"]
Variability = ["Variability_always", "Variability_until", "Variability_10", "Variability_only", "Variability_tr10", "Variability_tr0"]
"""

# =============================================================================
# param 22 : Better set of param
# =============================================================================

"""
DOSSIER = "../plot/param22/"
Number_of_simulation = 40
numbreDePoint = 10

N0 = [1.0]
W0 = [2.0]

A = [0.2] 
M = [0.5, 1., 3.] #ralancer pour M = [1., 3.]

Strength = [0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01]
Alpha = [5, 10]
Beta = [0.5, 1., 3.] # DECREASE ! useful to compute for beta more than m/(1-a) ????
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 4., 7., 9.]

#dt = 0.02
FinalTime = [100]

Collapse = ["Collapse_proba", "Collapse_proba_per_time_unit"]
Applicant = ["N", "W", "NW"]
Variability = ["Variability_always", "Variability_until", "Variability_10", "Variability_only", "Variability_tr10", "Variability_tr0"]
"""


# =============================================================================
# param 23 : Better set of param
# =============================================================================

"""
DOSSIER = "../plot/param23/"
Number_of_simulation = 40
numbreDePoint = 10

N0 = [1.0]
W0 = [2.0]

A = [0.2] 
M = [0.25, 0.5, 0.75, 1., 2., 3., 4.] #ralancer pour M = [1., 3.]

Strength = [0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01]
Alpha = [5, 10, 20]
Beta = [0.25, 0.5, 0.75, 1., 2., 3.] # DECREASE ! useful to compute for beta more than m/(1-a) ????
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 4., 7., 9.]

#dt = 0.02
FinalTime = [100]

Collapse = ["Collapse_proba", "Collapse_proba_per_time_unit"]
Applicant = ["N", "W", "NW"]
Variability = ["Variability_always", "Variability_until", "Variability_10", "Variability_only", "Variability_tr10", "Variability_tr0"]
"""

# =============================================================================
# param 24 : CCorrection collpase per time unit (same param)
# =============================================================================

"""
DOSSIER = "../plot/param24/"
Number_of_simulation = 40
numbreDePoint = 10

N0 = [1.0]
W0 = [2.0]

A = [0.2] 
M = [0.25, 0.5, 0.75, 1., 2., 3., 4.] #ralancer pour M = [1., 3.]

Strength = [0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01]
Alpha = [5, 10, 20]
Beta = [0.25, 0.5, 0.75, 1., 2., 3.] # DECREASE ! useful to compute for beta more than m/(1-a) ????
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 2., 4., 7., 9.]

#dt = 0.02
FinalTime = [100]

Collapse = ["Collapse_proba", "Collapse_proba_per_time_unit"]
Applicant = ["N", "W", "NW"]
Variability = ["Variability_always", "Variability_until", "Variability_10", "Variability_only", "Variability_tr10", "Variability_tr0"]
"""


# =============================================================================
# param 25 : Better param and initial point eq or other
# =============================================================================

"""
DOSSIER = "../plot/param25/"
Number_of_simulation = 40
numbreDePoint = 10

N0 = ["equilibrium"] #####
W0 = [0, "equilibrium"] #####

A = [0.2] 
M = [0.5, 1., 2., 4., 8.] #ralancer pour M = [1., 3.]
#M = [8.]

Strength = [0.0002, 0.0005, 0.001, 0.002]
#Alpha = [5]
Alpha = [5, 10, 20, 40]
Beta = [1., 2., 4., 8., 16., 32.] ### DECREASE ! useful to compute for beta more than m/(1-a) ????
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1., 2., 5., 10.]

#dt = 0.02
FinalTime = [100]

Collapse = ["Collapse_proba", "Collapse_proba_per_time_unit"]
Applicant = ["N", "W", "NW"]
Variability = ["Variability_always", "Variability_until", "Variability_10", "Variability_only", "Variability_tr10", "Variability_tr0"]
"""

# =============================================================================
# param 26 : Model with 3 param
# =============================================================================


DOSSIER = "../plot/param26/"
Number_of_simulation = 40
numbreDePoint = 10

N0 = ["equilibrium"] #####
W0 = [0] #####

A = [0.2] 
#M = [1., 2., 4.] #ralancer pour M = [1., 3.]
M = [0.25, 0.5]

D = [0.25, 0.5, 1., 2., 4.]
#M = [8.]

Strength = [0.0002, 0.0005, 0.001, 0.002]
#Alpha = [5]
Alpha = [10, 20]
Beta = [4., 8., 16.] ### DECREASE ! useful to compute for beta more than m/(1-a) ????
Freq = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1., 2., 5., 10.]

#dt = 0.02
FinalTime = [100]

Collapse = ["Collapse_proba", "Collapse_proba_per_time_unit"]
Applicant = ["N", "W", "NW"]
Variability = ["Variability_always", "Variability_until", "Variability_10", "Variability_only", "Variability_tr10", "Variability_tr0"]


