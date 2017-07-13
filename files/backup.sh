#!/bin/sh
set -eu

echo "MySQL backup: Starting at $(date -u)."

# Grep filter to remove heading and internal MySQL databases.
filter='Database\|information_schema\|performance_schema\|mysql'

if databases="$(mysql --defaults-file=/etc/mysql/mysqldump.cnf \
                      --execute 'show databases;' | grep -vx $filter)"
then
    mysqldump --defaults-file=/etc/mysql/mysqldump.cnf
              --databases "$databases" || \
    echo "MySQL backup: Failed to backup."
else
    echo "MySQL backup: No databases to backup."
fi

echo "MySQL backup: Finished at $(date -u)."
