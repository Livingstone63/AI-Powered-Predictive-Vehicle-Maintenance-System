import joblib
import numpy as np

# Load the trained ML model
try:
    model = joblib.load("models/predictive_model.pkl")
    print("✅ Predictive model loaded successfully.")
except FileNotFoundError:
    print("❌ Model not found. Please train it first (run utils/model_training.py).")
    model = None

def predict_failure(vehicle):
    """Predicts if a vehicle is likely to fail soon."""
    if model is None:
        return False
    
    X = np.array([[vehicle["engine_temp"],
                   vehicle["vibration"],
                   vehicle["mileage"],
                   vehicle["brake_wear"]]])
    
    prediction = model.predict(X)[0]
    return bool(prediction)
