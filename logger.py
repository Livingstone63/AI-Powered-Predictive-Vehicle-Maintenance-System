from datetime import datetime

def log_event(message):
    """Logs events into reports/daily_summary.txt"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("reports/daily_summary.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")
