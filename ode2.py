#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from plotdf import plotdf
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm
from inspect import currentframe, getframeinfo
import time as tm
import copy

import pickle # to save object

import scipy.stats as stats



#exec(open("variability.py").read(), globals())
exec(open("simple_function.py").read(), globals()) #import this file by actualizing the change (without restart the kernel)

cf = currentframe()
    

Param_freq = {"p":0.01}
Param_strength = {"scale":0.07}
Fire_param_default = {"model": "proportionnal",
                      "frequence": "bernoulli",
                      "param_freq" : Param_freq,
                      "amplitude": "exponential",
                      "Param_strength" : Param_strength,
                      "type" : "proportionnal",
                      "coef_W_N" : 5}



class Ode:
    def __init__ (self, model = "allee_effect_adi_3", Init = [0.5, 0.5], Param_phy = None, solveur = "euler_ex", finalTime = 500, dt = 1.0, law_amplitude = "exponential", law_freq = "bernoulli", Fire_param = Fire_param_default):
        # Physical parameter
        self.model = model
        self.Init = Init # commencr à l'équilibre
        
        if(model == "allee_effect"):
            if(Param_phy != None):
                self.g, self.K, self.A, self.m, self.d = Param_phy
            else:
                self.g = 1.
                self.K = 1.
                self.A = 1.
                self.m = 1.
                self.d = 1.
        elif(model == "allee_effect_adi"):
            if(Param_phy != None):
                self.param1, self.param2 = Param_phy
            else:
                self.param1 = .4
                self.param2 = .4
        elif(model == "allee_effect_adi_3"):
            if(Param_phy != None):
                self.param1, self.param2, self.param3 = Param_phy
            else:
                self.param1 = .4
                self.param2 = .4     
                self.param3 = .4
                
      
        # Numerical parameter
        self.solveur = solveur
        self.finalTime = finalTime
        self.dt = dt
        self.NbreIte = int(self.finalTime / self.dt)
        self.Time = np.linspace(0, self.finalTime, self.NbreIte)
        
         
        # Fire !
        self.Fire_param = Fire_param
        self.Fire_events = self.fire_events()
        self.Fire_strength = np.random.exponential(**self.Fire_param["Param_strength"], size = self.NbreIte)
        return


    def copy(self):
        """copy all the object physically"""
        return copy.copy(self)      
    
    
    def save_object(self, filename):
        """save the object on the disk"""
        filehandler = open(filename, 'wb') 
        pickle.dump(self, filehandler)    
        filehandler.close()
        return    
    
    



    def fire_events(self):       
        """For now, we assume that the event of a fire is indepedant to Y"""
        law_freq = self.Fire_param["frequence"]

        if(law_freq == "without"):
            Freq_fire = np.zeros(self.NbreIte)
        elif(law_freq == "bernoulli"):
            p = self.Fire_param["param_freq"]["p"]
            if(p*self.dt <= 1):
                Freq_fire = np.random.binomial(n=1, p=self.dt*p, size = self.NbreIte) # we have to multiply by dt in order to have a perturbation independant to the numerical step
            else:
                print("Please decrease the time step to have more")
#        elif(law_freq == "bernoulli_without_dt"):
#            p = self.Fire_param["param_freq"]["p"]
#            Freq_fire = np.random.binomial(n=1, p = p, size = self.NbreIte) # we have to multiply by dt in order to have a perturbation independant to the numerical step
        else:
            print("The law of the fire frequence is not known")
            
        Freq_fire = np.array(Freq_fire, dtype=np.bool)
        Freq_fire[0] = False # we assume we dont' have a fire at the initial time of the study
        self.Fire_events = Freq_fire
        return Freq_fire
    
    
    def density_burned(self, n, w, i):
        """when a fire occur, give the density burned by the fire for N and W"""
        model_fire = self.Fire_param["model"]
        alpha = self.Fire_param["Param_coupled"]["alpha"]
        beta = self.Fire_param["Param_coupled"]["beta"] 
        if(model_fire == "proportionnal"):
            
            n_burned = self.Fire_strength[i]*n
            w_burned = self.Fire_strength[i]*w
        elif(model_fire == "coupled"):
            ############################################################################################
            # Remark :
            # previous W continues to impact the strength of the fire even if they are not anymore W ...
            ############################################################################################
            n_burned = self.Fire_strength[i]*(n+alpha*w)
            w_burned = beta*self.Fire_strength[i]*(n+alpha*w)
# =============================================================================
#             # if all the dead wood is burned, the fire stop !!
# =============================================================================
            if(w_burned > w):
                w_burned = w
                n_burned = w_burned/beta
        return n_burned, w_burned
    



    def F_allee_effect(self, Y, t):
        """ F for model with allee effect"""
        n, w = Y
        Nder = self.g*n*(1-n/self.K)*(n/self.A-1)
        Wder = self.m*n - self.d*w
        return [Nder, Wder]
    

    def F_allee_effect_adi(self, Y, t):
        """ F for allee effect without dimension"""
        n, w = Y
        Nder = n*(1-n)*(n-self.param1)
        Wder = self.param2*n - w
        return [Nder, Wder]
    
    
    def F_allee_effect_adi_3(self, Y, t):
        """ F for allee effect without dimension but """
        n, w = Y
        Nder = n*(1-n)*(n-self.param1)
        Wder = self.param2*n - self.param3*w
        return [Nder, Wder]

    
    def F_verhulst(self, Y, t):
        """ verhulst """
        n, w = Y
        Nder = self.g*n*(1-n/self.K)
        Wder = self.m*n - self.d*w
        return [Nder, Wder]
                

    def euler_ex(self, F, Init, Time):
        """ compute the solution with explicit euler method"""
        Y = np.zeros((len(Time), len(Init)))
        Y[0,:] = Init        
        for i in range(1, len(Time)):
            Y[i,:] = Y[i-1,:] + self.dt*np.array(F(Y[i-1,:], Time[i])) # t or i ??????
        return Y


    def solve(self, Init=None, Time=None, solveur = None):
        """solve the system (without fire)"""
        if(Init is None):
            Init = self.Init
        if(Time is None):
            Time = self.Time
        if(solveur is None):
            solveur = self.solveur
        
        dic_model = {"allee_effect" : self.F_allee_effect, 
                     "allee_effect_adi" : self.F_allee_effect_adi,
                     "allee_effect_adi_3" : self.F_allee_effect_adi_3,
                     "verhulst" : self.F_verhulst}
        if(solveur == "odeint"):
            Y = odeint(dic_model[self.model], Init, Time)
        elif(solveur == "euler_ex"):
            Y = self.euler_ex(dic_model[self.model], Init, Time)
        else:
            print("(line ", cf.f_lineno, ") The choice of the solveur is not correct")
            
# =============================================================================
#         check if the density remain positive
# =============================================================================
            
#        self.N, self.W = np.array(Y).transpose()
#        return self.N, self.W
        return Y
    
    
    def solve_by_part(self):
        """solve the ode between two fires"""
#        Y = self.solve(self.Init, self.Time)
#        self.N, self.W = np.array(Y).transpose()
#        return self.N, self.W
        Y = np.zeros((self.NbreIte, 2))
        c = 0           # compteur
        Init = self.Init
        while(c < self.NbreIte):
            if(self.Fire_events[c] == False):
                c_old = c
                Sequence = [self.Time[c]]
                c += 1               
                while(c < self.NbreIte and self.Fire_events[c] == False):
                    Sequence += [self.Time[c]]
                    c+=1
                Y[c_old:c] = self.solve(Init, Sequence) 
#                if(c < len(FireB)): ### they are a fire !!
#                    Y[c] = Y[c-1] #+ self.Perturbation[:,c]
#                    Init = Y[c]
            else:
                # fire !
                Init = Y[c-1] - self.density_burned(*Y[c-1], c)
   
#                Y[c] = np.array([np.NAN, np.NAN])
                if(Init[0] < 0):
                    Init[0] = 0
                if(Init[1] < 0):
                    Init[1] = 0
                Y[c] = self.solve(Init, [self.Time[c-1], self.Time[c]])[-1]
                c += 1
        Y = np.array(Y).transpose()
        self.N, self.W = Y
#        print("255")
        return Y
    
        
    
    def plot_time_series(self, show=True, save = False, name=False, generation = False, legend = True):
        try:
            self.N
        except:
            self.solve_by_part()
            print("you forgot to lunch the simulation ! ")
###############################################
        if(generation):
            plt.clf()
            plt.cla()
###############################################

        
      #  print("\n\nlen(self.perturbation", len(self.Perturbation))
       # print("len(self.N)", len(self.N))
        
#        plt.figure(figsize=(16.8))
        
        plt.plot(self.Time, self.N, color = "g", label="N")
        plt.plot(self.Time, self.W, color = "maroon", label="W")
#        plt.plot(self.Time[abs(O.Perturbation) > 1e-4], self.N[abs(O.Perturbation) > 1e-4], "*r", label = "Fire\nfrequence "+self.law_freq+" ("+str(0)+")\namplitude "+self.law_amplitude+"("+str(0)+")")


        before_fire = list(self.Fire_events[1:])+[False]        
#        if(self.Fire_events[0] and self.Fire_events[1] == False):
#            before_fire[0] = True
#        elif(self.Fire_events[0] and self.Fire_events[1]):
            
        if(generation):
            plt.plot(self.Time[before_fire], self.N[before_fire], "*r", label = "Fire")
        else:
            plt.plot(self.Time[before_fire], self.N[before_fire], "*r", label = Fire_print(self.Fire_param))
        plt.plot(self.Time[before_fire], self.W[before_fire], "*r")
        
        
        if(legend):
            plt.legend(fontsize = 20)
        plt.xlabel("time", fontsize = 20)
        mmax = max([max(self.N), max(self.W)])

        plt.ylim(0, 1.1*mmax)

        plt.ylabel("density", fontsize = 20)
#        plt.title("Time series, \n with perturbation : "+self.law+", with parameters : "+str(self.Param_pertubation))
        
                    
        if(generation is False):
            if(name is False):
                if(self.model == "allee_effect_adi"):
#                    plt.title("Time series \na = "+str(self.param1)+", m = "+str(self.param2))#+", with parameters : "+str(self.Param_pertubation))
                    plt.title("Time series", fontsize = 25)#+", with parameters : "+str(self.Param_pertubation))
                else:
                    plt.title("Time series", fontsize = 25)#+", with parameters : "+str(self.Param_pertubation))
            else:
                plt.title(name)
        if(save):
            plt.savefig(name)
        if(show):
            plt.show()
        return

        
    def plot_phase_portrait(self, Xwindow = np.array([0,10]), Ywindow = np.array([0,10]), name = "Phase portrait", B_legend = True):
        if(self.model == "allee_effect"):
            plotdf(self.F_allee_effect, Xwindow, Ywindow, parameters={'t':0})
        elif(self.model == "allee_effect_adi"):
            plotdf(self.F_allee_effect_adi, Xwindow, Ywindow, parameters={'t':0})
            if(self.param1 < 1):
                plt.plot([0, 1], [0, self.param2], "o", label="stable\nequilibrium")
                plt.plot([self.param1], [self.param1*self.param2], "*", label="unstable\nequilibrium")
            else:
                plt.plot([0, self.param1], [0, self.param1*self.param2], "o", label="stable\nequilibrium")
                plt.plot([1], [self.param2], "*", label="unstable\nequilibrium")
                
            if(B_legend):
                plt.legend()
        plt.title(name)
        plt.xlabel("N")
        plt.ylabel("W")   
        plt.show()
        
        

    def plot_phase_portrait_0(self, Xwindow = np.array([0,10]), Ywindow = np.array([0,10]), name = "Phase portrait", B_legend = True):
        if(self.model == "allee_effect"):
            print("To DO (line ", cf.f_lineno)
        elif(self.model == "allee_effect_adi"):
#            plotdf(self.F_allee_effect_adi, Xwindow, Ywindow, parameters={'t':0})
            if(self.param1 < 1):
                plt.plot([0, 1], [0, self.param2], "o", label="stable\nequilibrium")
                plt.plot([self.param1], [self.param1*self.param2], "*", label="unstable\nequilibrium")
            else:
                plt.plot([0, self.param1], [0, self.param1*self.param2], "o", label="stable\nequilibrium")
                plt.plot([1], [self.param2], "*", label="unstable\nequilibrium")
            
            X = np.linspace(Xwindow[0], Xwindow[1], 10)
            Y = np.linspace(Ywindow[0], Ywindow[1], 10)
            for i, x in enumerate(X):
                for j, y in enumerate(Y):
#                    print(x, y)
                    O2 = O.copy()
                    O2.Perturbation = np.zeros_like(O2.Perturbation)
                    O2.Init = [x, y]
                    N, W = O2.solve_by_part()
                    eps = 1e-2
                    if(N[-1] < eps):
                        plt.plot(N, W, "black")
#                        print(N[1]-N[0], W[1]-W[0])
#                        plt.quiver(N[1]-N[0], W[1]-W[0])#, "black")
                    elif(abs(N[-1] - 1) < eps):
                        plt.plot(N, W, "blue")
                    elif(abs(N[-1] - 1) < eps):
                        plt.plot(N, W, "orange")
                    else:
                        plt.plot(N, W, "magenta")
                        print("No convergence yet ...")
                    plt.plot(color = "black", label= "extinctions")
                    plt.plot(color = "blue", label= "equilibrium state")
                    plt.plot(color = "orange", label= "equilibrium state")                    
            if(B_legend):
                plt.legend()
        plt.title(name)
        plt.xlabel("N")
        plt.ylabel("W")         
        plt.show()




    def plot_phase_portrait_2(self, Xwindow = np.array([0,10]), Ywindow = np.array([0,10]), name = "Phase portrait", B_legend = True, show = False):
        if(self.model == "allee_effect"):
            print("To DO (line ", cf.f_lineno)
        elif(self.model == "allee_effect_adi"):
#            plotdf(self.F_allee_effect_adi, Xwindow, Ywindow, parameters={'t':0})
            if(self.param1 < 1):
                plt.plot([0, 1], [0, self.param2], "o", label="stable\nequilibrium")
                plt.plot([self.param1], [self.param1*self.param2], "*", label="unstable\nequilibrium")
            else:
                plt.plot([0, self.param1], [0, self.param1*self.param2], "o", label="stable\nequilibrium")
                plt.plot([1], [self.param2], "*", label="unstable\nequilibrium")
            
            X = np.linspace(Xwindow[0], Xwindow[1], 10)
            Y = np.linspace(Ywindow[0], Ywindow[1], 10)
            FN = np.zeros((len(X), len(Y)))
            FW = np.zeros_like(FN)         
            
            for i, x in enumerate(X):
                for j, y in enumerate(Y):
                    O2 = O.copy()
                    #O2.Fire_events = np.zeros_like(O2.Fire_events)
                    O2.Init = [x, y]
                    N, W = O2.solve_by_part()
                    FN[i,j], FW[i,j] = N[-1], W[-1]

            eps = 1e-2
            Extinction = FN < eps
            Equilibrium1 = abs(FN-1) < eps
            Equilibrium2 = abs(FN-self.param1) < eps

#            FN[:,:] = 0
            FN[Extinction] = 0
            FN[Equilibrium1] = 1
            FN[Equilibrium2] = self.param1
                       
            FN = FN.transpose()

#            Color = np.array([["b"]*len(X)]*len(Y))
#            Color[Extinction] = "black"
#            Color[Equilibrium1] = "blue"
#            Color[Equilibrium2] = "orange"
                      
            ### make a condition if either of the above is not verify, print a message warning

#            plt.plot(color = "black", label= "extinctions")
#            plt.plot(color = "blue", label= "equilibrium state")
#            plt.plot(color = "orange", label= "equilibrium state")                    

            XX, YY = np.meshgrid(X, Y)
            U = XX*(1-XX)*(XX-self.param1)
            V = self.param2*XX - YY
            
#            print(Extinction)      
#            print("\n", np.shape(XX[Extinction]))
#            print(np.shape(U[Extinction]))
            
#            plt.streamplot(XX, YY, U, V, color = FN)
            plt.streamplot(XX, YY, U, V)

            plt.contourf(XX, YY, FN)

            if(B_legend):
                plt.legend()
        plt.title(name, fontsize=20)
        plt.xlabel("N", fontsize=12)
        plt.ylabel("W", fontsize=12)   
        if(show):
            plt.show()
        return



# =============================================================================
# Measures         
# =============================================================================


    def collapse_computation(self):
        if(self.model == "allee_effect_adi" or self.model == "allee_effect_adi_3"):
            if(self.N[-1] < self.param1): # collapse ?
                self.collapse = self.Time[np.argmax(self.N < self.param1)]
                return self.collapse # return the time of the collapse
            else:
                self.collapse = np.NaN
                return self.collapse
        else:
            print("Collapse for this model is not implemented yet")
            
            
    def get_collapse(self):
        try: 
            return self.collapse
        except:
            self.collapse_computation()
            return self.collapse
    
    
    
    
    def variability(self, applicant, timeRegime = 0.1):
        """depend of dt !!!!!"""               # need to change the computation !!
        if(self.N[-1] < self.param1): # collapse
            i3 = np.argmax(self.N < self.param1)
        else:
            i3 = len(self.N)-1
        average = np.mean(self.W[:i3//2])
        i1 = np.argmax((self.W[1::]-average)*(self.W[:1:]-average) < 0) # first time we cross the average
    #    print("Initial point", O.Time[i1])    
    #    print("final point : ", O.Time[i3])
    #    print("average : ", average)
        if((i3-i1) >= timeRegime*len(self.N)):
            if(applicant == "N+W"):
                return np.var(self.N[i1:i3//2] + self.W[i1:i3//2])
            elif(applicant == "N"):
                return np.var(self.N[i1:i3//2])
            elif(applicant == "W"):
                return np.var(self.W[i1:i3//2])
            else:
                print("Wrong choice of the application of the variability")
        else:
            return np.NaN



