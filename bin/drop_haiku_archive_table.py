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
if int(year_string) < 1999 or int(year_string) > 2014:
    print "\n"
    print "Year must be between 1999 and 2014\n"
    sys.exit(1)    

# begin
#     con = Mysql.new 'localhost', 'root', 'menagerie', 'haiku_archive'

#     con.query("DROP TABLE IF EXISTS archive_2014")

# rescue Mysql::Error => e
#     puts e.errno
#     puts e.error
    
# ensure
#     con.close if con
# end
