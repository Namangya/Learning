-- Oracle Initialization Parameters (init.ora / spfile)

-- db_cache_size
-- Default: platform-dependent (typically hundreds of MB)
-- Effect: Size of the database buffer cache; larger = fewer physical reads

-- shared_pool_size
-- Default: platform-dependent
-- Effect: Memory for SQL parsing and PL/SQL; increase if library cache misses

-- processes
-- Default: varies by edition (XE ~40-100)
-- Effect: Maximum number of OS processes connected to Oracle

-- undo_retention
-- Default: 900 (seconds)
-- Effect: How long undo data is kept for consistent reads and flashback

-- log_buffer
-- Default: platform-dependent
-- Effect: Size of redo log buffer before writing to disk

-- sga_target / pga_aggregate_target
-- Default: 0 (manual sizing) or auto-tuned if AMM enabled
-- Effect: Automatic Memory Management totals for SGA and PGA
