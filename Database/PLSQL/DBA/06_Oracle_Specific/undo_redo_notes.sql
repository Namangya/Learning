-- Undo and Redo Log Management
-- Undo tablespace
CREATE UNDO TABLESPACE undotbs1 DATAFILE '/u01/oradata/undotbs01.dbf' SIZE 200M;
ALTER SYSTEM SET undo_tablespace = 'undotbs1';

-- Redo log groups
ALTER DATABASE ADD LOGFILE GROUP 2 ('/u01/oradata/redo02.log') SIZE 50M;
SELECT group#, members, bytes/1024/1024 AS size_mb, status FROM v$log;
