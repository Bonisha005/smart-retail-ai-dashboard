import numpy as np
from sklearn.linear_model import LinearRegression

# Sample historical sales data
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([120, 135, 150, 160, 170, 185])

model = LinearRegression()
model.fit(X, y)

def predict_demand(day):
    return round(float(model.predict([[day]])[0]), 2)

def inventory_recommendation(current_stock, predicted_demand):
    if current_stock < predicted_demand:
        return "Restock Recommended"
    return "Stock Sufficient"
