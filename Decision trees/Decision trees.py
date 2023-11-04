
# Import necessary libraries
from sklearn.datasets import load_wine  # Load a different dataset
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load the Wine dataset (replace with your dataset)
data = load_wine()

X, y = data.data, data.target

# Create a Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)

# Fit the classifier on the data
clf.fit(X, y)

# Visualize the decision tree
plt.figure(figsize=(12, 6))

plot_tree(clf, filled=True, feature_names=data.feature_names, class_names=data.target_names)
plt.show()
