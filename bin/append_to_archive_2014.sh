#!/bin/bash

# see if there's anything new to process

rsync -lat --delete mena@sasi.pair.com:/usr/www/users/mena/haikupoet/new_haiku/ /home/pablo/git/haiku_search/data/new_haiku/
if [ -e /home/pablo/git/haiku_search/data/new_haiku/0000.html ]

# if so append it

then 
  for i in `ls -1 ~/git/haiku_search/data/new_haiku/[0-9]???.html`
  cd /home/pablo/git/haiku_search/bin
  do
    ./extract_haiku_2014.rb ${i}
    sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
    ./insert_haiku_from_file_into_table.py 2014 qwert.txt
  done

# cleanup

  rm -rf snippet.txt qwert.txt
  ssh mena@sasi.pair.com "cat /dev/null > /usr/home/mena/mail/new_haiku"
  ssh mena@sasi.pair.com "rm -f /usr/www/users/mena/haikupoet/new_haiku/*"

else

# error handling

  echo "nothing new to process"
  exit 2 

fi

