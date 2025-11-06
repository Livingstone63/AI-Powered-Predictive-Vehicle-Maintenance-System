import random

def collect_feedback(vehicle):
    """Simulates customer feedback after service."""
    feedbacks = ["Excellent service", "Good", "Satisfied", "Needs improvement"]
    feedback = random.choice(feedbacks)
    print(f"💬 Feedback from Vehicle {vehicle['vehicle_id']}: {feedback}\n")
