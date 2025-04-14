from firebase_config import init_connection
import datetime
import csv
import os

db = init_connection()
CSV_PATH = "fallback_mood_log.csv"

def log_mood_entry(mood: str):
    entry = {
        "mood": mood,
        "timestamp": datetime.datetime.utcnow()
    }
    try:
        db.collection("mood_logs").add(entry)
    except Exception as e:
        with open(CSV_PATH, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([entry["timestamp"], entry["mood"]])

def get_mood_logs():
    try:
        docs = db.collection("mood_logs").order_by("timestamp").stream()
        return [{"mood": d.to_dict()["mood"], "timestamp": d.to_dict()["timestamp"]} for d in docs]
    except Exception:
        if os.path.exists(CSV_PATH):
            with open(CSV_PATH, mode="r") as file:
                reader = csv.reader(file)
                return [{"timestamp": row[0], "mood": row[1]} for row in reader]
        return []
