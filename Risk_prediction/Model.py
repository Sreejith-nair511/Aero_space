# Import libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load your dataset
data = pd.read_csv('flights.csv')

# Step 2: Prepare features and target
X = data[['PilotExp']]  # Feature: Pilot Experience
y = data['Accident']    # Target: 0 = No accident, 1 = Accident

# Step 3: Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X.values.reshape(-1, 1), y)

# Step 4: Predict for a new flight
new_flight = [[600]]  # Example: Pilot with 600 hours
pred = model.predict(new_flight)
prob = model.predict_proba(new_flight)
print(f"Prediction for pilot with {new_flight[0][0]} hours: {'Accident' if pred[0]==1 else 'Safe'}")
print(f"Probability: {prob[0]}")  # [P(No Accident), P(Accident)]

# Step 5: Plot Pilot Experience vs Accident Probability
# We'll compute probability for range of pilot experience
pilot_exp_range = np.arange(0, 2500, 50).reshape(-1, 1)
acc_prob = model.predict_proba(pilot_exp_range)[:, 1]  # Probability of accident

plt.figure(figsize=(8,5))
plt.scatter(X['PilotExp'], y, color='red', label='Data points')
plt.plot(pilot_exp_range, acc_prob, color='blue', label='Predicted Accident Probability')
plt.xlabel('Pilot Experience (hours)')
plt.ylabel('Accident Probability')
plt.title('Pilot Experience vs Accident Probability')
plt.legend()
plt.grid(True)
plt.show()
