-- Oracle V$ Dynamic Performance Views

-- V$SESSION — active database sessions
-- Purpose: identify connected users, status, wait events
SELECT sid, serial#, username, status, machine, program
FROM v$session
WHERE username IS NOT NULL;

-- V$SQL — SQL statements in the shared pool
-- Purpose: find top SQL by elapsed time or executions
SELECT sql_id, executions, elapsed_time, sql_text
FROM v$sql
WHERE ROWNUM <= 10
ORDER BY elapsed_time DESC;

-- V$SYSSTAT — system-wide statistics
-- Purpose: monitor DB-wide counters (logical reads, commits, etc.)
SELECT name, value
FROM v$sysstat
WHERE name IN ('user commits', 'physical reads', 'db block gets');

-- V$WAITSTAT — wait event statistics by class
-- Purpose: identify contention (buffer busy, free buffer waits)
SELECT class, count, time
FROM v$waitstat
ORDER BY time DESC;
