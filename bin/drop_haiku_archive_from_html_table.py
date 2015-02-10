#!/usr/bin/env python

import MySQLdb, sys, time

table_name = "archive_2015_from_html"

# Open database connection
db = MySQLdb.connect("localhost","root","menagerie","haiku_archive" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS %s" % table_name)

# disconnect from server
db.close()
