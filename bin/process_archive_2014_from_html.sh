#!/bin/bash

./drop_haiku_archive_from_html_table.py
for i in `ls -1 ~/git/haiku_search/data/archive/[0-9]???.html`
do
  ./extract_haiku_2014.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_from_html.py qwert.txt
done
# rm -rf snippet.txt qwert.txt
