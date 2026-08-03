#!/usr/bin/env python

from sys import argv
import MySQLdb, sys, time

# Open database connection
db = MySQLdb.connect("localhost","root","menagerie","haiku_archive" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table using execute() method.

sql = """CREATE TABLE IF NOT EXISTS published_haiku (
         index INT,
         haiku_text VARCHAR(120),
         publication_name CHAR(22),
         year CHAR(6),
         month CHAR(6),
         volume CHAR(12),
         issue CHAR(12))"""

cursor.execute(sql)

# disconnect from server
db.close()
