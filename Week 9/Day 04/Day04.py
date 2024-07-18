import numpy as np
#Linear SVM
from sklearn.svm import SVC

# Example usage
X = np.array([[1, 1], [2, 2], [1, 2], [2, 3]])
y = np.array([0, 0, 1, 1])
clf = SVC(kernel='linear')
clf.fit(X, y)
print(clf.coef_)
print(clf.intercept_)

#Kernel SVM
# Example usage
clf = SVC(kernel='rbf')
clf.fit(X, y)
print(clf.support_vectors_)

#CART (Classification and Regression Trees)
from sklearn.tree import DecisionTreeClassifier

# Example usage
clf = DecisionTreeClassifier()
clf.fit(X, y)
print(clf.feature_importances_)
