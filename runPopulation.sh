#!/bin/sh

clear
git pull
python3 populate.py
echo '   ---   '
PGPASSWORD=passpass psql -U dmd1_user -d hospital -p 18636 -h localhost -a -f SQL/table_creation.sql | grep 'error'
PGPASSWORD=passpass psql -U dmd1_user -d hospital -p 18636 -h localhost -a -f insert_script.sql | grep 'error'
PGPASSWORD=passpass psql -U dmd1_user -d hospital -p 18636 -h localhost -a -f manual_inserts.sql | grep 'error'
