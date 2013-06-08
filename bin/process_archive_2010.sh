#!/bin/bash

./drop_table_2010.rb
for i in `ls -1 ~/git/haiku_search/data/archive_2010/[0-9]???.html`
do
  ./extract_haiku.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
  sed  '/^Paul\ David\ Mena/,$d' snippet.txt > qwert.txt
  ./insert_haiku_from_file_into_table_2010.rb qwert.txt
done
rm -rf snippet.txt qwert.txt
