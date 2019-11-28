#!/bin/sh

clear
git pull
python3 populate.py
echo '   ---   '
PGPASSWORD=passpass psql -U dmd1_user -d dmd1 -p 18636 -h localhost -a -f SQL/table_creation.sql > /dev/null
PGPASSWORD=passpass psql -U dmd1_user -d dmd1 -p 18636 -h localhost -a -f insert_script.sql | grep 'error'
