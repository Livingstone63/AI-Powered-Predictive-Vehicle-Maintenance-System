import random
import datetime

def schedule_service(vehicle):
    """Assigns a random time slot for vehicle service."""
    slots = ["10 AM", "2 PM", "4 PM"]
    day = datetime.date.today() + datetime.timedelta(days=random.randint(1, 3))
    slot = random.choice(slots)
    print(f"🛠️  Vehicle {vehicle['vehicle_id']} scheduled for {day} at {slot}.")
