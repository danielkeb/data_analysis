import pandas as pd

# Load the Titanic dataset
titanic_data = pd.read_csv("titanic.csv")


#check shape of the data 

print(titanic_data.shape)
print(titanic_data.columns)
print(titanic_data['name'])

#Getting a statistical decription of our data 
print(titanic_data.describe())
# Check for missing values
# 0 indicates no missing data
# number indicates number of missing values
print(titanic_data.isnull().sum())

# Handle missing values (e.g., fill missing age values with the mean)
#titanic_data['age'].fillna(titanic_data['age'].mean(), inplace=True)

# Drop irrelevant columns
#titanic_data = titanic_data.drop(['Cabin', 'Embarked'], axis=1)

# Confirm changes
print(titanic_data.head())
print(titanic_data.tail())
print(titanic_data.info())