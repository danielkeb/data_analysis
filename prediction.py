# Draw conclusions with descriptive statistics
import pandas as pd
data=pd.read_csv("titanic.csv")

# checking survival number interms of sex
survival_by_sex = data.groupby('sex')['survived'].mean()
print(survival_by_sex)

# Train a simple predictive model (e.g., logistic regression)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# data correction at age column
data['age'].fillna(data['age'].mean(), inplace=True)

#data correction at fare
data['fare'].fillna(data['fare'].mean(), inplace=True)

# Prepare features and target
X = data[['pclass', 'age', 'sibsp', 'parch', 'fare']]
y = data['survived']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')
