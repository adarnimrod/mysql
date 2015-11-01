#!/bin/sh -e
# Back up all databases, each to a seperate file.

backup() {
    mysqldump --defaults-file=/etc/mysql/debian.cnf \
        --single-transaction \
        --force \
        --result-file=/var/backups/mysql_$1.sql $1
}

# TODO: Find a way to remove table formatting from this command.
#alias show='mysqlshow --defaults-file=/etc/mysql/debian.cnf'
alias show="mysql --defaults-file=/etc/mysql/debian.cnf -e 'show databases;'"

# The reason for dropping the first 4 lines is that the first line is the
# heading and 3 following lines are databases internal to MySQL and thus their
# backup is not needed.
for database in $(show | tail -n+5)
do
    backup $database
done
