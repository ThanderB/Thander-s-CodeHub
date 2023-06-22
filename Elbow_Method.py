### Elbow Method for defining no of clusters for Vp vs Density Plot ###
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
#Elbow Method for KMeans (Sum of Squared Error=SSE)
SSE = {}
for i in range(1, 5):
    kmeans = KMeans(n_clusters = i, n_init= 4, init = 'k-means++', random_state = 20)
    kmeans.fit(data)
    SSE[i] = kmeans.inertia_

#Clustering of data for k=4 
data['cluster'] = kmeans.labels_
data['cluster'].value_counts()
sns.scatterplot(x=data['Vp'],y=data['Density'], hue=data['cluster'],palette=sns.color_palette('hls',data['cluster'].nunique()))
plt.title('Vp vs Density plot with 4 cluster')
plt.xlabel("P wave velocity in m/s")
plt.ylabel("Density in gm/cc")
plt.show()


 







              
         



