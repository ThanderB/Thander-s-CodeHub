import numpy as np
import pandas as pd
import lasio
import matplotlib.pyplot as plt
from scipy.signal import lfilter


#Load the LAS file
las_read = lasio.read(r'C:\Users\HP\Desktop\AI\Sample_well_5.las')
#Show the 'Well' description of the loaded LAS file
Header = las_read.sections['Well']
#print(Header)
#Show the available curves 
Curves = las_read.sections['Curves']
#Store las file to pandas dataframe
logs_df = las_read.df()
#Select and Filter data
RHOB = logs_df['RHOB']
VS = logs_df['VS']
VP = logs_df['VP']
DPTM = logs_df['DPTM']

RHOB = logs_df['RHOB']
VS = logs_df['VS']
VP = logs_df['VP']

logs_df = logs_df.replace(np.nan,0)
#Indexing the logs
logs_df = logs_df.reset_index()
#Apply simple Infinite impulse response Filter
n =100
b = [1.0/n]*n
a = 1
Filter_RHOB = lfilter(b,a,RHOB)
Filter_VP =lfilter(b,a,VP)
Filter_VS =lfilter(b,a,VS)

#Plot
fig,ax = plt.subplots(nrows=1, ncols=3, figsize=(12,8))
ax[0].plot(Filter_RHOB ,logs_df.DEPTH,color='k')
ax[1].plot(Filter_VP,logs_df.DEPTH,color='r')
ax[2].plot(Filter_VS,logs_df.DEPTH,color='b')

#Set axes labels and limits
ax[0].set_xlabel('RHOB (gm/cc)')
ax[0].set_xlim([2.1,2.4])
ax[0].set_ylabel('Depth (m)')
ax[0].set_ylim([1000,0])

ax[1].set_xlabel('VP (m/s)')
ax[1].set_xlim([700,2200])
ax[1].set_ylim([1000,20])

ax[2].set_xlabel('VS (m/s)')
ax[2].set_xlim([350,520])
ax[2].set_ylim([1000,0])

plt.show()

