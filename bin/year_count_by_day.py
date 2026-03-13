#!/usr/bin/env python

import MySQLdb
import sys
import datetime

year = int(sys.argv[1])
table = "archive_{}".format(year)

db = MySQLdb.connect("localhost","root","menagerie","haiku_archive")
cur = db.cursor()

cur.execute("""
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(date_written,'<i>',-1),'-{}',1), COUNT(*)
FROM {}
GROUP BY 1
""".format(year,table))

counts = dict(cur.fetchall())

start = datetime.date(year,1,1)

# stop at today if it's the current year
today = datetime.date.today()
if year == today.year:
    end = today
else:
    end = datetime.date(year,12,31)

d = start

while d <= end:

    key = d.strftime("%d-%b").lstrip("0")

    print(key, counts.get(key,0))

    d += datetime.timedelta(days=1)
