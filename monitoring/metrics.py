import json                      # JSON formatting
import time                      # Timestamping

def log_metric(name, value):
    """
    Emits structured metrics.
    """

    metric = {
        "metric": name,          # Metric name
        "value": value,          # Metric value
        "timestamp": time.time() # Unix timestamp
    }

    print(json.dumps(metric))    # Log output (collector reads this)
