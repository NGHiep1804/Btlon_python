import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = pd.read_csv('results.csv')
data=data.drop(columns=['Unnamed: 0','Name','Nation','Position','Team'])
data.replace('N/a',0,inplace=True)
kmeans=KMeans(n_clusters=3,random_state=42)
pca = PCA(n_components=2)
X_r = pca.fit_transform(data)
y=kmeans.fit_predict(data)
colors = ['navy','turquoise','darkorange']
plt.figure()
for i in range(3):
    plt.scatter(X_r[y==i, 0], X_r[y==i, 1],color=colors[i], alpha=0.8, lw=2)
plt.title('PCA plot of IRIS dataset')
plt.show()