#!/usr/bin/env python

from sys import argv
import MySQLdb, sys, time

# Validate Argument

arguments = sys.argv[1:]
count = len(arguments)

if count < 1:
    print "\n"
    print "Usage:"
    print "%s <year>" %sys.argv[0]
    print "\n"
    sys.exit(1)    

year_string = sys.argv[1]
if int(year_string) < 1999 or int(year_string) > 2015:
    print "\n"
    print "Year must be between 1999 and 2015\n"
    sys.exit(1)    

table_name = "archive_" + year_string

# Open database connection
db = MySQLdb.connect("localhost","root","menagerie","haiku_archive" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS %s" % table_name)

# disconnect from server
db.close()
