import json                      # Reads and writes JSON
import os                        # File and directory handling
import time                      # Timestamping for filenames

RAW_DIR = "data/raw"             # Raw data storage location

os.makedirs(RAW_DIR, exist_ok=True)  # Create directory if missing

def ingest_events():
    """
    Simulates Lambda consuming a Kinesis stream.
    """

    with open("data/stream_events.json") as f:
        events = json.load(f)     # Load incoming stream events

    filename = f"events_{int(time.time())}.json"  # Unique file name
    path = os.path.join(RAW_DIR, filename)        # Full output path

    with open(path, "w") as f:
        json.dump(events, f)      # Write raw events to disk

    return path                   # Return path for downstream steps
