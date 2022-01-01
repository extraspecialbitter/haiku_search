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
if int(year_string) < 1999 or int(year_string) > 2022:
    print "\n"
    print "Year must be between 1999 and 2022\n"
    sys.exit(1)

table_name = "archive_" + year_string

# Open database connection
db = MySQLdb.connect("localhost","root","menagerie","haiku_archive" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# do the actual query
cursor.execute("SELECT * FROM %s" % table_name)

# fetch all of the rows from the query
data = cursor.fetchall ()

# print the rows
for row in data :
    print row[0], row[1]

# count the rows
n_rows = cursor.rowcount
print "There are %s rows in the result set" %n_rows
    
# disconnect from server
db.close()

