# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:48:04 2019

@author: jerome

This script give a framework to run a set of simulation

"""
import numpy as np


exec(open("ode2.py").read(), globals()) #import this file by actualizing the change (without restart the kernel)


    



class Solver:
    def __init__(self, numberOfSimulation = 100, **param):
        self.numberOfSimulation = numberOfSimulation
        self.param = param
        self.finalTime = param["finalTime"]
        self.dt = param["dt"]
        self.Time = np.arange(0, self.finalTime, self.dt)
        return
    
    def run(self):
        self.O = [[]]*self.numberOfSimulation
        for i in range(self.numberOfSimulation):
            self.O[i] = Ode(**self.param)
            self.O[i].solve_by_part()
        return
        
    def collapse_proba_per_time_unit(self):
        """
        return the probability of collapse per time unit
        Collapse for this model is not implemented yetpse should be an array of the time collapse or False if not collapse
        """ 
        try:
            self.O
        except:
            self.run()
            print("you forgot to lunch the simulation ! ")
        
        try:
            self.Collapse
        except:
            self.Collapse = np.zeros(self.numberOfSimulation)
            for i in range(self.numberOfSimulation):
                self.Collapse[i] = self.O[i].get_collapse()
        
        Time = np.arange(0, self.finalTime, self.dt)
        X = np.zeros_like(Time)
        #for i,t in enumerate(Time): ### Optimizer !
        #    X[i] = sum(self.Collapse < t) / len(self.Collapse)    
        for c in self.Collapse:
            if(1-np.isnan(c)):
                X[Time>=c] += 1 
        X /= len(self.Collapse)
        
        # Having 1 in  the series will explose the follow link functions
        if(X[-1]==1):
            indice = np.argmax(X == 1.)
            if(indice <=1):
                return 1
            else:
                Time = Time[:indice]
                X = X[:indice]
        a, b, coef, p_value, err = stats.linregress(Time, -np.log(1-X))
        return 1-np.exp(-a)


    def collapse_proba(self):
        """
        return the probability of collapse
        Collapse for this model is not implemented yetpse should be an array of the time collapse or False if not collapse
        """ 
        try:
            self.O
        except:
            self.run()
            print("you forgot to lunch the simulation ! ")
        
        try:
            self.Collapse
        except:
            self.Collapse = np.zeros(self.numberOfSimulation)
            for i in range(self.numberOfSimulation):
                self.Collapse[i] = self.O[i].get_collapse()
        return np.mean(1-np.isnan(self.Collapse))


    
    def variability_always(self, applicant):
        """Compute the variability always"""            
        self.Variability = np.zeros(self.numberOfSimulation)
        for i in range(self.numberOfSimulation):
            self.Variability[i] = self.O[i].variability(applicant=applicant, timeRegime = 0.)
        var = np.mean(self.Variability) # normalement il n'y a pas de nan
        return var
    
        
    
    def variability_until(self, applicant):
        """compute variability until the system collapse (in practise just half the time before the system collapse)"""
        try:
            self.Collapse
        except:
            self.collapse()
        
        self.V = np.zeros(self.numberOfSimulation)
        for i in range(self.numberOfSimulation):
            if(np.isnan(self.Collapse[i])):    
                if(applicant == "N+W"):
                    self.V[i] = np.var(self.O[i].N[len(self.O[i].N)//10:] + self.O[i].W[len(self.O[i].N)//10:])
                elif(applicant == "N"):
                    self.V[i] = np.var(self.O[i].N[len(self.O[i].N)//10:])
                elif(applicant == "W"):
                    self.V[i] = np.var(self.O[i].W[len(self.O[i].N)//10:])
                else:
                    print("Wrong choice of the application of the variability") 
            elif(self.Collapse[i] <= len(self.O[i].N)//10):
                self.V[i] = np.NaN 
            else: # collapse
                until = np.argwhere(self.Time == self.Collapse[i])
                if(applicant == "N+W"):
                    self.V[i] = np.var(self.O[i].N[len(self.O[i].N)//10: until] + self.O[i].W[len(self.O[i].N)//10: until])
                elif(applicant == "N"):
                    self.V[i] = np.var(self.O[i].N[len(self.O[i].N)//10: until])
                elif(applicant == "W"):
                    self.V[i] = np.var(self.O[i].W[len(self.O[i].N)//10: until])
                else:
                    print("Wrong choice of the application of the variability") 
        return np.nanmean(self.V)




    def variability_10(self, applicant):
        """return both variability (just between the first 10% and 20% interval of the time study)"""
        self.V = np.zeros(self.numberOfSimulation)
        for i in range(self.numberOfSimulation):
            if(applicant == "N+W"):
                self.V[i] = np.var(self.O[i].N[len(self.O[i].N)//10: len(self.O[i].N)//5] + self.O[i].W[len(self.O[i].N)//10: len(self.O[i].N)//5])
            elif(applicant == "N"):
                self.V[i] = np.var(self.O[i].N[len(self.O[i].N)//10: len(self.O[i].N)//5])
            elif(applicant == "W"):
                self.V[i] = np.var(self.O[i].W[len(self.O[i].N)//10: len(self.O[i].N)//5])
            else:
                print("Wrong choice of the application of the variability")    
        return np.mean(self.V)
 
    
    
    def variability_only(self, applicant):
        """Compute the variability only when the system do not collapse"""
        try:
            self.Collapse
        except:
            self.collapse()
            
        self.Variability_0 = np.zeros(self.numberOfSimulation)
        for i in range(self.numberOfSimulation):
            self.Variability_0[i] = self.O[i].variability(applicant=applicant, timeRegime = 0.)
            
        return np.mean(self.Variability_0[np.isnan(self.Collapse)]) # normalement il n'y a pas de nan
    
    
    
    
    def variability_tr10(self, applicant):
        """we need a time regime of a at least 10% of the time study to compute the variability"""
        try:
            self.Collapse
        except:
            self.collapse()
            
        self.Variability_10 = np.zeros(self.numberOfSimulation)
        for i in range(self.numberOfSimulation):
            self.Variability_10[i] = self.O[i].variability(applicant=applicant, timeRegime = 0.1)
        
        var_after = np.nanmean(self.Variability_10[np.isnan(self.Collapse)])
        var_no_collapse = np.nanmean(self.Variability_10[1-np.isnan(self.Collapse)])
        var = (var_after*sum(np.isnan(self.Collapse)) + var_no_collapse*sum(1-np.isnan(self.Collapse))) / len(self.Variability_10)
        return var




    def variability_tr0(self, applicant):
        try:
            self.Collapse
        except:
            self.collapse()
            
        self.Variability_0 = np.zeros(self.numberOfSimulation)
        for i in range(self.numberOfSimulation):
            self.Variability_0[i] = self.O[i].variability(applicant=applicant, timeRegime = 0.)
        
        var_after = np.nanmean(self.Variability_0[np.isnan(self.Collapse)])
        var_no_collapse = np.nanmean(self.Variability_0[1-np.isnan(self.Collapse)])
        var = (var_after*sum(np.isnan(self.Collapse)) + var_no_collapse*sum(1-np.isnan(self.Collapse))) / len(self.Variability_0)
        return var


  
#Collapse = np.zeros(numberOfSimulation) 
#for i in range(numberOfSimulation):
#    Collapse[i] = S.O[i].get_collapse()
#     
#Time = np.arange(0, finalTime, dt)
#X = np.zeros_like(Time)
#for c in Collapse:
#    if(1-np.isnan(c)):
#        X[Time>=c] += 1 
#X /= len(Collapse)        
#
#
#indice = np.argmax(X == 1.)
#
#X2 = X[:indice]
#Time2 = Time[:indice]
#a, b, coef, p_value, err = stats.linregress(Time2, -np.log(1.1-X2))
#plt.plot(1-np.exp(-(a*Time+b)), label="reg")
#plt.plot(X2, label="data")
#plt.legend()
#plt.show()



# =============================================================================
# "model" : "proportionnal", coupled
# =============================================================================


#n0=0.5_w0=0.0_final_time=100_a=0.1_m=2.0_strength=0.0005_alpha=20_beta=2.0_freq=0.8

"""
a = 0.2
Param_phy = [a, 0.5]      # 0.2, 10
      
Init = [0.5, Param_phy[1]]
#Init = [1., 0]



Param_freq = {"p":  5} #2
dt = min([0.1, 0.1/Param_freq["p"]])


finalTime = 100
Param_strength = {"scale":0.002} # 0.0008
Param_coupled = {"alpha":10, # 20
                 "beta":.5} # 500



Fire_param = {"model": "coupled",
                "frequence": "bernoulli",
                "param_freq" : Param_freq,
                "amplitude": "exponential",
                "Param_strength" : Param_strength,
                "Param_coupled" : Param_coupled,
                "type" : "proportionnal",
                "coef_W_N" : 5}



O = Ode(model = "allee_effect_adi", Init=Init, Param_phy= Param_phy, finalTime = finalTime, dt=dt, Fire_param = Fire_param)
O.solve_by_part()
plt.figure(figsize = (12, 6))
O.plot_time_series(generation=True)
"""


"""
v = O.variability(applicant = "N+W", timeRegime = 0.1)
print("Variability :   ", v*10**6//1*10**-6)
#v = O.variability(applicant = "N", timeRegime = 0.)
print("Variability 0 : ", v*10**6//1*10**-6)
print("Variability N   ", np.var(O.N)*10**6//1*10**-6)
print("Variability W   ", np.var(O.W)*10**6//1*10**-6)
"""


# =============================================================================
# 
# =============================================================================

"""
numberOfSimulation = 100
S = Solver(numberOfSimulation=numberOfSimulation, model = "allee_effect_adi", Init=Init, Param_phy= Param_phy, finalTime = finalTime, dt=dt, Fire_param = Fire_param)
S.run()
c = S.collapse_proba_per_time_unit()
print("Probability of collapse (per time units): ", c)
"""
