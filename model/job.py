import joblib
import numpy as np
import pandas as pd

model=joblib.load("model.joblib")

def predict_iris(data):
    data=np.array([data])
    prediction=model.predict(data)
    return int(prediction[0])