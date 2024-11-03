import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
data=pd.read_csv('results.csv')
data.replace('N/a',0,inplace=True)
data=data.drop(columns=['Unnamed: 0'])
df=data.select_dtypes(include=[float,int])
n_samples = len(df)
wcss = [] 
range_clusters = range(2, min(11, n_samples))  
for k in range_clusters:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)  
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)
plt.plot(range_clusters, wcss, marker='o')
plt.title('Phương pháp Elbow')
plt.xlabel('Số lượng cụm')
plt.ylabel('WCSS')
plt.show()