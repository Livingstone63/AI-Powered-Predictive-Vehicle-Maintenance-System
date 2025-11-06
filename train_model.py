import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Print debug info
print("📁 Current Directory:", os.getcwd())

# Step 1: Load the dataset
data = pd.read_csv("data/vehicle_data.csv")

# Step 2: Separate features (X) and target (y)
X = data[["engine_temp", "vibration", "mileage", "brake_wear"]]
y = data["failure_risk"]

# Step 3: Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate accuracy
accuracy = model.score(X_test, y_test)
print(f"✅ Model trained successfully! Accuracy: {accuracy*100:.2f}%")

# Step 6: Save the model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/predictive_model.pkl")
print("💾 Model saved at models/predictive_model.pkl")
