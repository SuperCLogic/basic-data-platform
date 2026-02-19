import sqlite3                              # SQL execution
from ingest.stream_to_raw import ingest_events
from transform.batch_transform import transform
from monitoring.metrics import log_metric

def run_pipeline():
    """
    End-to-end orchestration.
    """

    raw_path = ingest_events()              # Step 1: ingest
    log_metric("ingest_success", 1)          # Emit metric

    transform(raw_path)                     # Step 2: transform
    log_metric("transform_success", 1)       # Emit metric

    conn = sqlite3.connect("databases/athena.db")
    cur = conn.cursor()                     # SQL cursor

    for sql_file in ["load/analytics_load.sql", "load/ops_load.sql"]:
        with open(sql_file) as f:
            cur.executescript(f.read())     # Execute SQL scripts

    conn.commit()                           # Save results
    conn.close()                            # Close connection

    log_metric("pipeline_complete", 1)      # Final success metric

if __name__ == "__main__":
    run_pipeline()                          # Entry point
