from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd

# Load the historical stock data from the Excel file
stock_data = pd.read_excel('stock_data.xlsx')

# Step 2 & 3: Data Preprocessing and Feature Engineering (for demonstration, let's assume we use only Close prices as features)
features = stock_data[['Close']].shift(1)  # Use previous day's Close price as a feature
target = stock_data[['Close']]
features.columns = ['Previous_Close']

# Step 4: Split Data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, shuffle=False)

# Step 5: Model Selection
model = RandomForestRegressor()

# Step 6: Model Training
model.fit(X_train, y_train)

# Step 7: Model Evaluation
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Step 8: Prediction
future_features = features[-3:].values.reshape(1, -1)  # Assuming the last 3 days' Close prices
#future_predictions = model.predict(future_features)
# Reshape the input features to match the shape used during training
future_features = future_features[:, -1].reshape(-1, 1)

# Predict next 3-day stock prices
future_predictions = model.predict(future_features)
print("Predicted next 3-day stock prices:", future_predictions)

# Step 9: Visualization
plt.plot(y_test.index, y_test, label='Actual Prices')
plt.plot(y_test.index, predictions, label='Predicted Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Actual vs. Predicted Stock Prices')
plt.legend()
plt.show()

# Step 10: Iterate and Improve (e.g., by experimenting with different features, models, and hyperparameters)
