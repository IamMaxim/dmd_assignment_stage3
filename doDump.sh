#!/bin/sh

PGPASSWORD=passpass pg_dump -U dmd1_user -d hospital -p 18636 -h localhost -a > dump.sql
