import pandas as pd

def read_vehicle_data():
    """Reads vehicle data from CSV and returns a list of dictionaries."""
    try:
        df = pd.read_csv("data/vehicle_data.csv")
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print("❌ Vehicle data file not found.")
        return []
