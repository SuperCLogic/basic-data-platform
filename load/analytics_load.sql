CREATE TABLE IF NOT EXISTS user_metrics AS
SELECT
    user_id,                     -- User identifier
    date(ts) AS event_date,      -- Event date
    COUNT(*) AS event_count,     -- Number of events
    SUM(value) AS total_value    -- Aggregated value
FROM raw_events
GROUP BY user_id, date(ts);
