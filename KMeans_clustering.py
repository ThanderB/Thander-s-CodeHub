### KMeans_clustering for Vp vs Density Plot###
import numpy as np
import pandas as pd
import lasio
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
from sklearn.cluster import KMeans
import sklearn.cluster as cluster

#Load the LAS file
las_read = lasio.read(r'D:\Sample_Well_1.las')
#Show the 'Well' description of the loaded LAS file
Header = las_read.sections['Well']
#Show the available curves 
Curves = las_read.sections['Curves']
#Store las file to pandas dataframe
df = las_read.df()
#replace nan value by zero
#df = df.replace(np.nan,0)
#remove zero values from data 
df_new = df[df.loc[:]!=0].dropna()
RHOB = df_new['RHOB']
DT = df_new['DT']
DT = df_new['DT'].values[:,np.newaxis]
Density = df_new['RHOB'].values
Vp = (10**6/DT)*0.3048
Vp_df = pd.DataFrame(Vp,columns=['Vp'])
Density_df = pd.DataFrame(Density,columns=['Density'])

#DataFrame
data = pd.concat([Vp_df,Density_df], axis=1)
#Elbow Method for KMeans (Sum of Squared Error =SSE)
SSE = {}
for i in range(1, 10):
    kmeans = KMeans(n_clusters = i, n_init= 4, init = 'k-means++', random_state = 20)
    kmeans.fit(data)
    SSE[i] = kmeans.inertia_
plt.plot(SSE.keys(),SSE.values(),'gs-')
plt.xlabel("Values of 'k'")
plt.ylabel("Sum of Squared Error (SSE)")
plt.title('Elbow method of K-Means Clustering')
plt.grid()
plt.show()



 







              
         



