#!/usr/bin/env python

from sys import argv
import MySQLdb, sys, time

# Validate Argument

arguments = sys.argv[1:]
count = len(arguments)

table_name = "archive_2021_duplicates"

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

