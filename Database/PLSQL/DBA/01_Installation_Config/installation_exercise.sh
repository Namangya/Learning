#!/bin/bash
# Oracle installation exercise
docker exec -it oracle-xe sqlplus sys/<password>@XEPDB1 as sysdba <<EOF
SELECT * FROM v\$version;
EOF
