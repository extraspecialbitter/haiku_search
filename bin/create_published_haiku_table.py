#!/usr/bin/env python

import csv
import sys
import MySQLdb

CSV_PATH = "published_haiku.csv"  # update to your actual CSV file path

# Open database connection
db = MySQLdb.connect("localhost", "root", "menagerie", "haiku_archive")
cursor = db.cursor()

# Create table if it doesn't exist yet
# Note: renamed "index" -> "haiku_index" since INDEX is a reserved word in MySQL
create_sql = """CREATE TABLE IF NOT EXISTS published_haiku (
         haiku_index INT,
         haiku_text VARCHAR(120),
         publication_name CHAR(22),
         year CHAR(6),
         month CHAR(6),
         volume CHAR(12),
         issue CHAR(12))"""

cursor.execute(create_sql)

# Populate table from CSV
# Expected CSV column order: haiku_text, publication_name, year, month, volume, issue
insert_sql = """INSERT INTO published_haiku
                 (haiku_index, haiku_text, publication_name, year, month, volume, issue)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader, None)  # skip header row; remove this line if your CSV has no header

    rows_inserted = 0
    for i, row in enumerate(reader, start=1):
        if len(row) != 6:
            print(f"Skipping malformed row {i}: {row}", file=sys.stderr)
            continue

        haiku_text, publication_name, year, month, volume, issue = row
        cursor.execute(insert_sql, (i, haiku_text, publication_name, year, month, volume, issue))
        rows_inserted += 1

db.commit()
print(f"Inserted {rows_inserted} rows.")

# disconnect from server
db.close()
