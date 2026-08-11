#!/usr/bin/env python
# Written for Python 2.7

from __future__ import print_function

import csv
import sys
import MySQLdb

CSV_PATH = "published_haiku.csv"  # update to your actual CSV file path

# Open database connection
db = MySQLdb.connect("localhost", "root", "menagerie", "haiku_archive")
cursor = db.cursor()

# Always start fresh: drop the table if it exists, then recreate it
drop_sql = "DROP TABLE IF EXISTS published_haiku"
cursor.execute(drop_sql)

# Note: renamed "index" -> "haiku_index" since INDEX is a reserved word in MySQL
create_sql = """CREATE TABLE published_haiku (
         haiku_index INT,
         haiku_text VARCHAR(120),
         publication_name CHAR(22),
         year CHAR(6),
         month VARCHAR(12),
         volume CHAR(12),
         issue CHAR(12))"""

cursor.execute(create_sql)

# Populate table from CSV
# Expected CSV column order: haiku_text, publication_name, year, month, volume, issue
insert_sql = """INSERT INTO published_haiku
                 (haiku_index, haiku_text, publication_name, year, month, volume, issue)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""

with open(CSV_PATH, "rb") as f:
    reader = csv.reader(f)
    header = next(reader, None)  # skip header row; remove this line if your CSV has no header

    rows_inserted = 0
    for i, row in enumerate(reader, start=1):
        if len(row) != 6:
            print("Skipping malformed row {0}: {1}".format(i, row), file=sys.stderr)
            continue

        haiku_text, publication_name, year, month, volume, issue = row
        haiku_text = haiku_text.replace("/", "<br>")
        cursor.execute(insert_sql, (i, haiku_text, publication_name, year, month, volume, issue))
        rows_inserted += 1

db.commit()
print("Inserted {0} rows.".format(rows_inserted))

# disconnect from server
db.close()
