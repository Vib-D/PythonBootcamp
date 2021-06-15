Original file is located at
    https://colab.research.google.com/drive/1TXXhL27KI0Z1A2xRP9EMQI-Ew9ZvmGQD

# Unsupervised Machine Learning - KMeans

Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection. SVMs are one of the most robust prediction methods. 

Sources: 
[sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html?highlight=kmeans#sklearn.cluster.KMeans), [wikipedia](https://en.wikipedia.org/wiki/K-means_clustering)

![kmeans.png](https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/52579/versions/9/screenshot.jpg)
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Take make moons in built dataset

data_ =

# check the dataset

data_

# create input dataframe

inputData =

inputData.head()

# create output dataframe

outputData = 
outputData.head()

# create a scatter plot for inputData set



# create a scatter plot for inputData set with outputData color



# Call the sklearn Kmeans and make a model with 200 samples


#model_fit

# check for labels



# call metrics and check silhoutte score

# create a scatter plot for inputData set with model labels color

"""#### finding right number of cluster"""

cluster_range = range(1, 20)
error_list = []

for i in cluster_range:
    model = KMeans(n_clusters=i)
    model.fit(inputData)
    res = model.inertia_
    error_list.append(res)

import matplotlib.pyplot as plt

plt.plot(cluster_range, error_list, marker = "o", color = "g", markersize = 10)
plt.xlabel("Cluster Range")
plt.ylabel("IntraCluster Sum")
plt.title("KMeans")
plt.show()



