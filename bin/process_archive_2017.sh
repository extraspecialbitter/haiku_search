#!/bin/bash

./drop_haiku_archive_table.py 2017
for i in `ls -1 ~/git/haiku_search/data/archive/[0-9]???.html`
do
  ./extract_haiku_2017.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
# ./insert_haiku_from_file_into_table_2017.rb qwert.txt
  ./insert_haiku_from_file_into_table.py 2017 qwert.txt
done
# rm -rf snippet.txt qwert.txt
