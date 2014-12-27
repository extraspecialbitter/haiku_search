#!/bin/bash

# see if there's anything new to process

if [ -e /home/pablo/git/haiku_search/data/new_haiku/0000.html ]

# if so append it

then 
  cd /home/pablo/git/haiku_search/bin
  for i in `ls -1 ~/git/haiku_search/data/new_haiku/[0-9]???.html`
  do
    ./extract_haiku_2014.rb ${i}
    sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
    ./insert_haiku_from_file_into_table.py 2014 qwert.txt
  done

# cleanup

  rm -rf snippet.txt qwert.txt
  cat /dev/null > /home/pablo/mail/new_haiku
  rm -f /var/www/haikupoet/new_haiku/*

else

# error handling

  echo "nothing new to process"
  exit 2 

fi

