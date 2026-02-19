import json                      # JSON handling
import sqlite3                   # Embedded SQL engine
from datetime import datetime    # Date parsing

def transform(raw_file):
    """
    Simulates Spark / EMR batch processing.
    """

    with open(raw_file) as f:
        events = json.load(f)    # Load raw events

    conn = sqlite3.connect("databases/athena.db")  # Athena-like DB
    cur = conn.cursor()          # Cursor for SQL execution

    cur.execute("""
        CREATE TABLE IF NOT EXISTS raw_events (
            user_id TEXT,
            event TEXT,
            value INTEGER,
            ts TEXT
        )
    """)                          # Create external-style table

    for e in events:
        cur.execute(
            "INSERT INTO raw_events VALUES (?, ?, ?, ?)",
            (e["user_id"], e["event"], e["value"], e["ts"])
        )                         # Insert each event

    conn.commit()                # Save changes
    conn.close()                 # Close DB
