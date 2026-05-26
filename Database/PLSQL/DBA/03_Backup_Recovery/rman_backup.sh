#!/bin/bash
# RMAN Backup & Recovery Reference

# --- Full database backup ---
# Connect to RMAN and back up the entire database
rman target / <<EOF
BACKUP DATABASE PLUS ARCHIVELOG;
LIST BACKUP SUMMARY;
EOF

# --- Incremental backup ---
# Level 0 = full; Level 1 = incremental since last level 0/1
rman target / <<EOF
BACKUP INCREMENTAL LEVEL 0 DATABASE;
BACKUP INCREMENTAL LEVEL 1 DATABASE;
EOF

# --- Restore from RMAN ---
# Restore and recover to the latest available backup
rman target / <<EOF
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
RESTORE DATABASE;
RECOVER DATABASE;
ALTER DATABASE OPEN;
EOF
