#!/usr/bin/env python

from sys import argv
import MySQLdb, sys, time

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
if int(year_string) < 1999 or int(year_string) > 2014:
    print "\n"
    print "Year must be between 1999 and 2014\n"
    sys.exit(1)    

table_name = "archive_" + year_string

file_name = sys.argv[2]

# Open database connection
db = MySQLdb.connect("localhost","root","menagerie","haiku_archive" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table using execute() method.

sql = ""CREATE TABLE IF NOT EXISTS %s" % table_name
      haiku_text VARCHAR(120), 
      date_written CHAR(22))"
cursor.execute(sql)

# Open the file for processing
fh = open("%s" %file_name, "r")
print "Name of the file: ", fh.name
print "Closed or not : ", fh.closed
print "Opening mode : ", fh.mode
print "Softspace flag : ", fh.softspace

#     @date_row = true
#     @haiku_text = ""
#     @date_written = "<i>"

# remove blank lines from file

#     while( !fh.eof)
#         line = fh.readline.chomp
# remove leading and trailing blanks
#         line.strip!
# skip empty lines
#         next if line == ''
# convert tab chars to blanks
#         line.gsub!(/\t/,' ')
# convert apostrophe char to HTML code
#         line.gsub!(/'/,'&#8217;')
# substitute a single blank for a sequence of blanks
#         line.squeeze!(' ')
# insert line into table
#         if @date_row == true
#            @date_written << line
#            @date_written << '</i><br>'
#            @date_row = false
#         else
#            @haiku_text << line 
#            @haiku_text << '<br>' 
#         end
#   end
#   puts @haiku_text
#   puts @date_written
#    con.query("INSERT archive_2012(haiku_text, date_written) \
#       VALUES('#{@haiku_text}', '#{@date_written}')")
#   fh.close
#   exit(0)

# rescue Mysql::Error => e
#   puts e.errno
#   puts e.error
    
# ensure
#   con.close if con
# end
