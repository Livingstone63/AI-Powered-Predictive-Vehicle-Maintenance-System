from agents.data_agent import read_vehicle_data
from agents.prediction_agent import predict_failure
from agents.customer_agent import alert_customer
from agents.scheduler_agent import schedule_service
from agents.feedback_agent import collect_feedback
from utils.logger import log_event

def master_agent():
    print("🚗 Predictive Maintenance System Started\n")
    vehicles = read_vehicle_data()

    for v in vehicles:
        failure_risk = predict_failure(v)
        if failure_risk:
            alert_customer(v)
            schedule_service(v)
            collect_feedback(v)
            log_event(f"Vehicle {v['vehicle_id']} scheduled for maintenance.")
        else:
            print(f"✅ Vehicle {v['vehicle_id']} is healthy.\n")
            log_event(f"Vehicle {v['vehicle_id']} running normally.")
    
    print("✅ All vehicles processed successfully.\n")

if __name__ == "__main__":
    master_agent()
