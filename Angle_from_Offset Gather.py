import math
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

#Interval Velocity
Vi = np.array([2473,2622,2572,2656,2853],dtype='int')

Vi_list = Vi.tolist()

#Travel Time 
ti = np.array([0.010,0.010,0.010,0.010,0.010],dtype='f')
ti_list = ti.tolist()

#RMS Velocity Calculation
for i in range(len(Vi_list)):
    Vrms = sqrt(sum(ti*(pow(Vi_list[i],2))/sum(ti)))

#Offset
X = np.array([40,120,200,280,360,440,520,600,680], dtype ='int')
X_list = X.tolist()
print("Offsets in meter:",X)
#Zero offset TWT
T0 = np.array([0.640,0.650,0.660,0.670,0.680], dtype='f')
T0_list = T0.tolist()

#Calculate Angle from Offset
for j in range(len(X_list)):
    for k in range(len(Vi_list)):
        for m in range(len(T0_list)):
            P = sqrt((pow(X_list[j],2)*pow(Vi_list[k],2))/(pow(Vrms,2)*(pow(Vrms,2)*pow(T0_list[m],2)+ pow(X_list[j],2))))
            A = math.degrees(math.asin(P))
            
    print("Angle in Degrees:", A)
    
        


    


           


                
              



    
             
    
