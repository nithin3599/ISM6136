import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import pickle


#import os
#exit(os.getcwd())
lawn_prediction = pickle.load(open('C:/Users/Kanna/Downloads/choosen.pkl', "wb"))

income = float(input("person income "))
lot_size = float(input("mention the size of the lot "))
df = pd.DataFrame({'income': [income]},{'lot_size': [lot_size]})
result = choosen.predict_proba(df)
probability = choosen.predict(df)

