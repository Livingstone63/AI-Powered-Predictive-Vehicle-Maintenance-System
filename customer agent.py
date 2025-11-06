def alert_customer(vehicle):
    """Alerts the customer if vehicle needs service."""
    print(f"📢 Alert: Vehicle {vehicle['vehicle_id']} shows high failure risk!")
    print(f"   Engine Temp: {vehicle['engine_temp']}°C | Vibration: {vehicle['vibration']} | Brake wear: {vehicle['brake_wear']}")
    print("   Customer notified successfully.\n")
