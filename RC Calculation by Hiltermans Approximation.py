#RC Calculation by Hiltermans(2 Terms)Approximation
import numpy as np
import math
import matplotlib.pyplot as plt

#data loading
data = (r'C:\Users\HP\Desktop\AVO\Data.txt')
data_load = np.loadtxt(data)

#Define data column
Density = data_load[:,1]
RHOB = Density.tolist()
VP = data_load[:,2]
Vp = VP.tolist()
VS = data_load[:,3]
Vs = VS.tolist()
Angl = np.array([1.1811645538972224,3.5394863378484898,5.885867265483403,8.212613081755933,10.512415142881295,12.778478235315633,15.004624810910421,17.18537250994401,19.315983862663764])
A= Angl.tolist()

#Poisson's Ratio Calculation at Reservoir Zone

def sigma(Vp,Vs):
    sigma_values = []
    for i in range(5):
        sigma = (0.5 - pow((Vs[i]/Vp[i]),2))/(1-pow((Vs[i]/Vp[i]),2))
        sigma_values.append(sigma)
    return sigma_values
#print(sigma(Vp,Vs))                                         

Pr = np.array(sigma(Vp,Vs))
#PR_sort = np.sort(PR)
PR = Pr.tolist()
PR_avg = 0.415792345
#RC Calculation
#Hilterman (2 Term) Approximation

RC=[]
for i in range(len(Vp)-1):
    for j in range(len(A)-1):
        RC.append(((Vp[i+1]*RHOB[i+1]- Vp[i]*RHOB[i])/(Vp[i+1]*RHOB[i+1]+ Vp[i]*RHOB[i]))*pow(math.cos(A[j]*math.pi/180),2)\
                  + (PR[i+1]-PR[i])*math.pow(math.sin(A[j]*math.pi/180),2)/math.pow((1- PR_avg),2)) 
        
RC = np.array(RC)
RC_list = RC.tolist()
RC_list_sort = np.sort(RC_list)
print(RC)
plt.stem(RC)
plt.title(" RC by Hiltermans (2 Terms) Approximation")
plt.show()
       
    
        
