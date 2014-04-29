#!/usr/bin/env python

from sys import argv
import MySQLdb, sys, time

# Open database connection
db = MySQLdb.connect("localhost","root","menagerie","haiku_archive" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table using execute() method.

sql = """CREATE TABLE IF NOT EXISTS archive_test (
         haiku_text VARCHAR(120),
         date_written CHAR(22))"""

cursor.execute(sql)

# disconnect from server
db.close()
