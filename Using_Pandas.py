import numpy as np
import pandas as pd
from numpy.random import randn

#series

labels=['A','B','C']
arr=np.array(['Apple','Banana','Orange'])
print(arr)
print(pd.Series(arr,labels))

#DataFrames

np.random.seed(102)
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#return column

print(df['W'])

#adding new column

df['new']=np.array(['DE','FG','we','po','RE'])
print(df) #prints with new col

#add another col
df['new2']=np.array(['E','G','w','o','R'])
print(df)

#drop new2
print(df.drop('new2',axis=1,inplace=True))
print(df.drop('E',axis=0))

#to commit the drop use inplace=True
print("      W greater than 0")
print(df[(df['W']>0)])

#print row
print(df.loc['A'])


#MISSING DATA
Data={'col1':['A','B','C'],'col2':[1,2,np.nan],'col3':[np.nan,'2X',np.nan]}
df2=pd.DataFrame(Data)
print("         ")
print(df2)
print("Dropping null elements whole row ") #bydefault axis=0
print(df2.dropna())
print(df2.dropna(axis=1))

#filling null blocks
print(df2.fillna(value='filled'))


                           #GroupBy
Data2={'Student':['Maida Farooqi','Chandler Bing','Joey Tribbiani','Rachel Green','Monica Geller'] ,'CompanyLoc':
       ['Pakistan','Newyork','Spain','Newyork','Spain'],'YearsOfExperience':[3,4,2,3,3]}
df3=pd.DataFrame(Data2)
print(df3)
GB=df3.groupby('CompanyLoc').describe()
print(GB)
print(df3.groupby('YearsOfExperience').sum())

                         #operations

def func(x): #applying func to col
    return x*2
print(df3['YearsOfExperience'].apply(func))

print(df3['CompanyLoc'].unique()) #unique func()
print(df3['CompanyLoc'].nunique()) #nunique defines length

