
#importing packages
import pandas as pd #pandas for data manipulation
import numpy as np #numpy for working with arrays
from sklearn.model_selection import train_test_split #for model selection for train and test and split
from sklearn.preprocessing import StandardScaler #for
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix #report generate panna,

import joblib # for save the model

#data preprocessing
df=pd.read_csv('/content/Iris Dataset.csv') #df=dataframe
df

# analyse or knowing data
#to displaying the first five data
df.head()

#to displaying the last five rows
df.tail() #(needed numbers)

df.columns #for printing the value

df.describe() #for statistical value

df.info() #for summarize the data

df.shape #for finding the no of rows and columns

df.size #total number of values

df.isnull() #for finding the null values and if null=true not null= false

df.isnull().sum() # total number of missing value or null value

#df.drop('Id',axis=1)# 1 is for column 0 is for row id is column name
#df.drop(columns='Id') # reason for the error is i deleted the id column so don't worry daijobu

#df.drop('Id',axis=1,inplace=True) #for permenantly deleting, True for giving permission for deleting the

df

df.size

d=pd.read_csv('/content/Iris Dataset.csv')

d



X= df.drop('Species',axis=1) #input

Y=df['Species'] #output

X

Y

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

knn= KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, Y_train)

x_predict=knn.predict(X_test)

#y_predict=knn.predict(Y_test)#optional

accuracy=accuracy_score(Y_test,x_predict)

print("Accuracy:",accuracy)

