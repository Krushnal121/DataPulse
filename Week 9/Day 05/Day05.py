# ID3
# ID3 Algorithm implementation
# Note: sklearn uses CART for Decision Trees; pure ID3 implementation would be custom

from sklearn.tree import DecisionTreeClassifier

# Example usage
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)
print(clf.feature_importances_)

# C4.5
# Note: sklearn does not provide direct C4.5 implementation; similar to ID3 with pruning
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)
print(clf.feature_importances_)

# Pruning
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X, y)
print(clf.feature_importances_)

#Random Forest
from sklearn.ensemble import RandomForestClassifier

# Example usage
clf = RandomForestClassifier()
clf.fit(X, y)
print(clf.feature_importances_)

# Gradient Boosting
from sklearn.ensemble import GradientBoostingClassifier

# Example usage
clf = GradientBoostingClassifier()
clf.fit(X, y)
print(clf.feature_importances_)
