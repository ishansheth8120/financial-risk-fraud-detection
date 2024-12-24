#Evaluate trained model's performance on a test set

import pandas as pd 
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix

model = joblib.load('models/fraud_model.pk1') #trained model

data = pd.read_csv('data/raw/test_data.csv') #test dataset

X_test = data[['TransactionID','Amount','CustomerID']]
y_test =data['FraudLabel']

y_pred = model.predict(X_test)

print ('Accuracy Score ',accuracy_score(y_test, y_pred))
print ('Confusion Matrix ', confusion_matrix(y_test, y_pred))


