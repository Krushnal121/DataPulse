import matplotlib.pyplot as plt

# Basic plot
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# Line plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Line Plot')
plt.show()

# Bar plot
plt.bar(['A', 'B', 'C'], [1, 2, 3])
plt.title('Bar Plot')
plt.show()

# Histogram
plt.hist([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
plt.title('Histogram')
plt.show()

# Adding titles and labels
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Customized Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend(['Line'])
plt.show()
