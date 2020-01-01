#!/usr/bin/env python

from sys import argv
from warnings import filterwarnings
import MySQLdb, sys, time
import fileinput
import cgi

# Validate Argument

arguments = sys.argv[1:]
count = len(arguments)

if count != 2:
    print "\n"
    print "Usage:"
    print "%s <year> <file>" %sys.argv[0]
    print "\n"
    sys.exit(1)    

year_string = sys.argv[1]
if int(year_string) < 1999 or int(year_string) > 2020:
    print "\n"
    print "Year must be between 1999 and 2020\n"
    sys.exit(1)    

table_name = "archive_" + year_string
# table_name = "archive_test" 

file_name = sys.argv[2]

# filter MySQL warnings
filterwarnings('ignore', category = MySQLdb.Warning)

# Open database connection
db = MySQLdb.connect("localhost","root","menagerie","haiku_archive" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table using execute() method.

sql = "CREATE TABLE IF NOT EXISTS " + table_name  + """
         (haiku_text VARCHAR(120), 
         date_written CHAR(22))"""

cursor.execute(sql)

date_row = True
haiku_text = ""
date_list = ["<i>", "</i><br>"]

# remove blank lines and leading and trailing blanks from file

for line in open("%s" %file_name, "r"):
  line = line.rstrip()
  if line != '':
    newline = line
  line = line.strip()
  if line: # is not empty
    newline = line
    
# convert apostrophe and double-quote to HTML code
    newline = newline.replace("'", r"&#8217;")
    newline = newline.replace("\"", r"&quot;")
#   print(newline)

# insert line into table
    if date_row:
        date_written = newline.join(date_list)
        date_row = False
    else:
        haiku_text = haiku_text + newline + "<br>"

# print "%s" %haiku_text
# print "%s" %date_written

# SQL query to INSERT a haiku into the selected table 
cursor.execute('INSERT into ' + table_name + '(haiku_text, date_written) values (%s, %s)', (haiku_text, date_written))

# Commit your changes in the database
db.commit()

# disconnect from server
db.close()

