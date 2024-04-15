import numpy as np
import pandas as pd

#fetch iris dataset

url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv' #this is a github link, after navigating to the dataframe on github, we go to raw then we copy the link from there. 
df = pd.read_csv(url)

#OR 
#if we download the csv file
#df = pd.read_csv('/Users/BatoulSbat/Desktop/Courses/CoGrammar/Weeks Lectures/Data Science/Week 5/Lecture 1/iris.csv') #use this line if your file is a .csv and in the same directory as the script

#[] for dataframes, () for methods, {} for changing the name of the column


print(df.head()) #for the 5 top, tail() for the bottom 
print(df.shape)
print(df.info())
print(df.describe())

#selecting columns
print(df.columns)

#use specific columns
df_selected = df[['species','petal_length', 'petal_width']]
df_selected.info()

#filter rows by flower species
df_setosa = df[df['species'] == 'setosa']
df_setosa.info()

#creating new column
df['petal area'] = df['petal_length'] * df['petal_width']
print(df.head())

#rename
df = df.rename(columns = {'petal area' : 'petal_area (cm^2)'})
print(df.head())

#statistic
print(df['petal_area (cm^2)'].mean())
print(df['species'].unique()) #nunique

#grouping
print(df.groupby('species')['petal_length'].std())

#aggregating
print(df.groupby('species').agg(mean_petal_length = ('petal_length', 'mean'), 
                                max_sepal_length = ('sepal_length', 'max')))