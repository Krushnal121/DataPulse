# K-Means Clustering
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate some sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Apply K-Means
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Plot the results
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.title("K-Means Clustering")
plt.show()

# Hierarchical Clustering
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

# Generate some sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Perform Hierarchical Clustering
linked = linkage(X, 'single')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            distance_sort='descending',
            show_leaf_counts=True)
plt.title("Hierarchical Clustering")
plt.show()

# DBSCAN
from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Apply DBSCAN
db = DBSCAN(eps=1.5, min_samples=2).fit(X)

# Plot the results
plt.scatter(X[:, 0], X[:, 1], c=db.labels_, cmap='viridis')
plt.title("DBSCAN Clustering")
plt.show()
