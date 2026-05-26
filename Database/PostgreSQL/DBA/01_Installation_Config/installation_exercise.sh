#!/bin/bash
# Installation exercise — verify PostgreSQL is running
pg_isready
psql -U <username> -d <database> -c "SELECT version();"
