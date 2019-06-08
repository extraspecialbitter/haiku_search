#!/usr/bin/env python

from sys import argv
from warnings import filterwarnings
import MySQLdb, sys, time
import fileinput
import cgi

# Validate Argument

arguments = sys.argv[1:]
count = len(arguments)

if count != 1:
    print "\n"
    print "Usage:"
    print "%s <text>" %sys.argv[0]
    print "\n"
    sys.exit(1)    

search_string = sys.argv[1]

# filter MySQL warnings
filterwarnings('ignore', category = MySQLdb.Warning)

# Open database connection
db = MySQLdb.connect("localhost","root","menagerie","haiku_archive" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# loop through tables

years = (1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019)
for year_string in years:
    table_name = "archive_" + year_string

# do the actual query
    cursor.execute("SELECT COUNT(*) FROM %s WHERE haiku_text LIKE %s") % table_name search_string

# Commit your changes in the database
    db.commit()

# disconnect from server
db.close()

