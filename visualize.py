import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("titanic.csv")
data['age'].fillna(data['age'].mean(), inplace=True)
data['fare'].fillna(data['fare'].mean(), inplace=True)

# Example 1: Visualizing survival count by class
sns.countplot(x='pclass', hue='survived', data=data)
plt.title('Survival Count by passenger Class')
plt.show()

x=data['age']
y=data['fare']
plt.xlabel('Age')
plt.ylabel('Ticket Price')
plt.scatter(x,y)
plt.show()

# Example 2: Distribution of age
sns.histplot(data['age'].dropna(), bins=30, kde=True)
plt.title('Distribution of Age')
plt.show()

# Example 3: Correlation heatmap
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

# Example 4: Boxplot of fare by passenger class
sns.boxplot(x='pclass', y='fare', data=data)
plt.title('Boxplot of ticket price or fare by passenger Class')
plt.xlabel('Passenger class')
plt.ylabel('ticket price')
plt.show()

# x axis indicated survived person number
# y axis indicates ticket price 
x=data['survived']
y=data['fare']

plt.xlabel('survived')
plt.ylabel('fare')
plt.scatter(x,y)
plt.show()