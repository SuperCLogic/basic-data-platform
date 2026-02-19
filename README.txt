# Basic End-to-End Data Pipeline (Cloud-Inspired)

This project demonstrates a scalable ETL pipeline using only
basic Python libraries while replicating real cloud data flows.

## What This Simulates

| Cloud Tool | Local Replacement |
|----------|------------------|
| Kinesis | Python streaming loop |
| Lambda | Python function |
| S3 | SQLite raw table |
| Athena | SQL aggregation |
| Redshift / Snowflake | SQLite warehouse table |
| Airflow | Python orchestrator |
| CloudWatch / Datadog | Logging metrics |

## How To Run (10 Minutes)

1. Start producer

2. Run Lambda manually

3. Run batch pipeline

4. Observe logs for metrics
