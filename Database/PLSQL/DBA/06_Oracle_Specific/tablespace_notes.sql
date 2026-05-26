-- Oracle Tablespace Management
CREATE TABLESPACE app_data DATAFILE '/u01/oradata/app_data01.dbf' SIZE 100M AUTOEXTEND ON;
ALTER TABLESPACE app_data ADD DATAFILE '/u01/oradata/app_data02.dbf' SIZE 100M;
SELECT tablespace_name, status, contents FROM dba_tablespaces;
