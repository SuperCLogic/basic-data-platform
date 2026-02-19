CREATE TABLE IF NOT EXISTS daily_kpis AS
SELECT
    date(ts) AS event_date,      -- Day of activity
    COUNT(*) AS total_events,    -- Events per day
    SUM(value) AS revenue        -- Total revenue
FROM raw_events
GROUP BY date(ts);
