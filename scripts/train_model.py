#Training machine learning model using the provided datasets

import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

#load the dataset
data = pd.read_csv('data\Data\Transaction Data\transaction_records.csv')

#Train-Test split
X = data[['TrancationID','Amount','CustomerID']] #features
y = data['FraudLabel'] #target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

#train model 
model =RandomForestClassifier()
model.fit(X_train,y_train)

joblib.dump(model, 'models/fraud_model.pk1')










