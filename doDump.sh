#!/bin/sh

pg_dump -U dmd1_user -d dmd1 -p 18636 -h localhost -a > dump.sql
