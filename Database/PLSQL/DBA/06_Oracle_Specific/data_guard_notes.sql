-- Oracle Data Guard Basics
-- Primary → Standby replication for high availability
-- Modes: Maximum Protection, Maximum Availability, Maximum Performance
ALTER DATABASE CREATE STANDBY CONTROLFILE AS '/tmp/standby.ctl';
-- Configure LOG_ARCHIVE_DEST_n parameters on primary
