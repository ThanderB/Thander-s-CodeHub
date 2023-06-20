import numpy as np
import math
import matplotlib.pyplot as plt

#data loading
data = (r'D:\AVO\Data.txt')
data_load = np.loadtxt(data)

#Define data column
Density = data_load[:,1]
RHOB = Density.tolist()
VP = data_load[:,2]
Vp= VP.tolist()
VS= data_load[:,3]
Vs = VS.tolist()

#Poisson's Ratio Calculation at Reservoir Zone

def sigma(Vp,Vs):
    sigma_values = []
    for i in range(5):
        sigma = (0.5 - pow((Vs[i]/Vp[i]),2))/(1-pow((Vs[i]/Vp[i]),2))
        sigma_values.append(sigma)
    return sigma_values
#print(sigma(Vp,Vs))                                         

Poisson_Ratio = np.array(sigma(Vp,Vs))
Poisson_Ratio_sort = np.sort(Poisson_Ratio)

#Vp by Vs Calculation at Reservoir Zone
def VpByVs(Vp,Vs):
    VP_VS =[]
    for i in range(5):
        Vp_Vs = Vp[i]/Vs[i]
        VP_VS.append(Vp_Vs)
    return VP_VS

#print(VpByVs(Vp,Vs))
Vp_Vs_Ratio = np.array(VpByVs(Vp,Vs))
Vp_Vs_Ratio_sort = np.sort(Vp_Vs_Ratio)

#Poisson Ratio Vs Vp/Vs Plot
plt.plot(Poisson_Ratio_sort,Vp_Vs_Ratio_sort)
plt.grid()
plt.title("Poisson's Ratio Vs Vp/Vs Plot")
plt.xlabel("Poisson's Ratio")
plt.ylabel("Vp/Vs")
plt.show()

