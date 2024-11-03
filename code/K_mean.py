from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('results.csv')
data=data.drop(columns=['Unnamed: 0','Name','Nation','Position','Team'])
data.replace('N/a',0,inplace=True)
data=data.select_dtypes(include=[float, int])
def kmeans_display(X, label):
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .8)
    plt.axis('equal')
    plt.plot()
    plt.show()
means =data.values.tolist()
data_means=np.array(means)
cov=np.cov(data_means,rowvar=False)
kmeans = KMeans(n_clusters=3, random_state=0).fit(data_means)
pred_label = kmeans.predict(data_means)
kmeans_display(data_means, pred_label)