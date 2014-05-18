#!/bin/bash

# see if there's anything new
rsync -latv --delete mena@sasi.pair.com:/usr/www/users/mena/haikupoet/new_haiku/ /home/pablo/git/haiku_search/data/new_haiku/

# ./drop_haiku_archive_table.py 2014
for i in `ls -1 ~/git/haiku_search/data/new_haiku/[0-9]???.html`
do
  ./extract_haiku_2014.rb ${i}
  sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
# ./insert_haiku_from_file_into_table_2014.rb qwert.txt
  ./insert_haiku_from_file_into_table.py 2014 qwert.txt
done

# cleanup
rm -rf snippet.txt qwert.txt
ssh mena@sasi.pair.com "cat /dev/null > /usr/home/mena/mail/new_haiku"
ssh mena@sasi.pair.com "rm -f /usr/www/users/mena/haikupoet/new_haiku/*"

