-- Backup & Recovery (PostgreSQL)

-- Full backup
-- pg_dump -Fc mydb > backup.dump (custom format)
-- pg_dumpall > full.sql (all databases)

-- Incremental backup
-- WAL archiving: archive_mode = on, archive_command

-- PITR (Point-in-Time Recovery)
-- Base backup + WAL replay to target timestamp

-- Restore
-- pg_restore -d mydb backup.dump
-- psql -f full.sql for plain SQL dumps
