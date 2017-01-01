#!/bin/bash

# initializations

export InFile=/home/pablo/mail/new_haiku
export OutFile=/var/www/haikupoet/new_haiku
export Hype=/usr/bin/hypermail

# process the mail

$Hype -m $InFile -d $OutFile -x

# see if there's anything new to add

if [ -e /var/www/haikupoet/new_haiku/0000.html ]

# if so append it

then 
  cd /home/pablo/git/haiku_search/bin
  for i in `ls -1 /var/www/haikupoet/new_haiku/[0-9]???.html`
  do
    ./extract_haiku_2017.rb ${i}
    sed  '/^Received\ on/,$d' snippet.txt > qwert.txt
    ./insert_haiku_from_file_into_table.py 2017 qwert.txt
  done

# cleanup

  rm -f snippet.txt qwert.txt
  rm -f /var/www/haikupoet/new_haiku/*
  cat /dev/null > /home/pablo/mail/new_haiku

else

# error handling

  echo "nothing new to process"
  exit 2 

fi

