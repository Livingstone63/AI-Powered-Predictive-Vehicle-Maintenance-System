from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask API is running successfully!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        X = np.array([[data["engine_temp"], data["vibration"], data["mileage"], data["brake_wear"]]])
        # Dummy prediction logic just to test
        if data["engine_temp"] > 120 or data["vibration"] > 1.5:
            pred = 1
        else:
            pred = 0
        return jsonify({"failure_risk": int(pred)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print("🚀 Flask API starting on port 5000...")
    app.run(port=5000, debug=True)
