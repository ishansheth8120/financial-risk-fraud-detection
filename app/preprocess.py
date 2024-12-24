#This file handles all preprocessing such as cleaning data, handling missing values, etc

import pandas as pd
def preprocess_data(data):
    data.fillna(0, inplace = True) #handling missing values, normalizing the data
    return data