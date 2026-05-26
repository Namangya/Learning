#!/bin/bash
# Backup Recovery Exercise
# TODO: Take a pg_dump backup and restore to a test database
pg_dump -Fc <database> > exercise_backup.dump
# pg_restore -d <test_database> exercise_backup.dump
