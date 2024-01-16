import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
df=pd.read_excel("./MarketUserBehavior/users_market_behavior.xlsx")
#check number of columns and row
print(df.shape)
#check if there is missing data
print(df.isnull().sum())

#It show that no missing data

#we i want to see columns name

print(df.columns)

# 1. Demographic Analysis
# Distribution of users based on gender
gender_distribution = df['Gender'].value_counts()
print(gender_distribution)
# Age distribution of users
age_distribution = df['Age'].hist()
print(age_distribution)

# Distribution of estimated salaries
salary_distribution = df['EstimatedSalary'].hist()
print(salary_distribution)
# 2. Purchase Behavior
# Number of users who made a purchase
purchase_count = df['Purchased'].value_counts()

# Percentage of users who made a purchase
purchase_percentage = (purchase_count / len(df)) * 100

# Correlation between age and purchase behavior
age_purchase_correlation = df['Age'].corr(df['Purchased'])

# Correlation between estimated salary and purchase behavior
salary_purchase_correlation = df['EstimatedSalary'].corr(df['Purchased'])

# 3. Gender-based Analysis
# Distribution of purchases among different genders
purchase_gender_distribution = df.groupby('Gender')['Purchased'].value_counts()

# Difference in age between male and female users
age_difference_gender = df.groupby('Gender')['Age'].mean()

# Difference in estimated salary between male and female users
salary_difference_gender = df.groupby('Gender')['EstimatedSalary'].mean()

# 4. Age-based Analysis
# Average estimated salary for different age groups
average_salary_age_groups = df.groupby('Age')['EstimatedSalary'].mean()

# Purchase behavior by age group
purchase_by_age_group = df.groupby('Age')['Purchased'].value_counts()

# Age group with the highest tendency to make a purchase
most_purchasing_age_group = purchase_by_age_group.idxmax()

# 5. Salary-based Analysis
# Purchasing pattern among users with different salary ranges
purchase_by_salary_range = pd.cut(df['EstimatedSalary'], bins=3)
purchase_by_salary_range_counts = df.groupby(purchase_by_salary_range)['Purchased'].value_counts()

# Correlation between estimated salary and likelihood of making a purchase
salary_purchase_correlation = df['EstimatedSalary'].corr(df['Purchased'])

# Gender distribution across different salary ranges
gender_distribution_salary_range = df.groupby(purchase_by_salary_range)['Gender'].value_counts()

# 6. Combined Analysis
# Age and salary combinations leading to higher purchase rates
age_salary_purchase = df.groupby(['Age', 'EstimatedSalary'])['Purchased'].mean()
print(age_salary_purchase)

# Relationship between age and purchase behavior by gender
age_purchase_gender = df.groupby(['Gender', 'Age'])['Purchased'].mean()
print(age_purchase_gender)

# Average estimated salary for users who made a purchase
average_salary_purchase = df.groupby('Purchased')['EstimatedSalary'].mean()
print(average_salary_purchase)

# Additional visualization (example using seaborn)
plt.figure(figsize=(15,10))
plt.title('Age vs. Estimated Salary with Purchase Information')
plt.scatter(x='Age', y='EstimatedSalary', color='purple')



plt.show()


#visualize df interms of age and EstimatedSalary by using seaborn
plt.figure(figsize=(15,10))
sns.countplot(x=df['Age'], hue=df['EstimatedSalary'], data=df)

plt.title('Age and EstimatedSalary')
plt.xlabel('Age')
plt.ylabel('EstimatedSalary')
plt.show()

#visualize Salary and purchased relation
plt.figure(figsize=(15,10))
#x=df['EstimatedSalary']
#y=df['Purchased']
sns.histplot(x=df['EstimatedSalary'],hue=df['Purchased'])
plt.show()

# Creating model 
# encode Gender
df['Gender'] = preprocessing.LabelEncoder().fit_transform(df['Gender'])

# Assuming 'Purchased' is your target variable
X = df.drop('Purchased', axis=1)
y = df['Purchased']
#instanciate LogisticRegression
logregression=LogisticRegression(solver='liblinear')

#splitting our df into training and testing df set
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

#fitting our training dfset
logregression.fit(X_train,y_train)

#using our model to predict our testing values and training values
pred=logregression.predict(X_test)
train=logregression.predict(X_train)

"""
# # # # 6)Model Evaluation
"""

#evaluating our model with df some training df
print("training model accuracy: " ,accuracy_score(y_train,train))
plt.scatter(y_train,train,)
plt.show()

#evaluating our model with df some testing df
print("testing model accuracy :",accuracy_score(y_test,pred))

plt.scatter(y_test,pred)
plt.show()

