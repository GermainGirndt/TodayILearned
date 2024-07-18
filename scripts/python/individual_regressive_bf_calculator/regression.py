# load data
import json
import pandas as pd

with open('data.json', 'r') as file:
    json_file = json.load(file)
    
print(json_file)
data_frame = pd.DataFrame(json_file["data"])
print(data_frame)
print(type(data_frame))

# regression analysis
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x = data_frame[['age', 'weight', 'height', 'neck', 'waist']]
y = data_frame['bf']

print("Instantiating model...")
# Create a polynomial regression model
model = LinearRegression() # uncomment this line to use linear regression
#DEGREE = 2
#model = make_pipeline(PolynomialFeatures(DEGREE), LinearRegression()) # uncomment this line to use polynomial regression

# Train the model on the training data
print("Training model...")

model.fit(x, y)

dummy_data = {
    'age': [31],
    'weight': [74],
    'height': [170],
    'neck': [37],
    'waist': [84]
}

dummy_data = pd.DataFrame(dummy_data)

print("Predicting model...")
# Make predictions on the test data
y_pred = model.predict(dummy_data)

print(y_pred)
print(model.intercept_)
print(model.coef_)