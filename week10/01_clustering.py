#!/usr/bin/env python

"""
Usage: ./01_clustering.py hema_data.txt
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
from sklearn.cluster import KMeans
from scipy.cluster.vq import vq

df = pd.read_csv(sys.argv[1], delimiter="\t")
data = df.as_matrix()[:,1:].astype(float)

linked = linkage(data, method='average')
l_led = leaves_list(linked)
ordered = data[l_led,:]
dendro_linked = linkage(data.T, method='complete')

# Plots heatmap
plt.figure()
plt.title('Clustered Heatmap of Gene Expression')
plt.pcolor(ordered)
plt.colorbar()
plt.xlabel("Cell Type")
plt.ylabel("Gene")
plt.yticks([])
plt.xticks(np.arange(0.5, df.shape[1], 1), df.columns[1:])
plt.savefig("gene_expression_heatmap.png")
plt.close()

# Plots dendrogram
lables = df.columns[1:]
plt.figure()
dendro = dendrogram(dendro_linked,labels=lables)
plt.title('Dendrogram')
plt.savefig("dendrogram.png")
plt.close()

# Plots k-means clustering of genes plotted against CFU and poly
kmeans = KMeans(n_clusters=6)
kmeans = kmeans.fit(data)
labels = kmeans.predict(data)
centroids = kmeans.cluster_centers_
idx,_ = vq(data, centroids)

plt.figure()
plt.plot(data[idx==0, 0], data[idx==0,1],'ob', data[idx==1,0],data[idx==1,1], 'or', data[idx==2, 0], data[idx==2,1],'og', data[idx==3, 0], data[idx==3,1],'oy', data[idx==4, 0], data[idx==4,1],'oc', data[idx==5, 0], data[idx==5,1], 'om')
plt.plot(centroids[:,0], centroids[:, 1], 'sk', markersize=5)
plt.title("K-means Clustering with 6 Centroids")
plt.xlabel('CFU')
plt.ylabel('poly')
plt.savefig("k-means_clustering.png")
plt.