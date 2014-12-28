#!/bin/bash

# start out with a sleep to make sure the mailboxes are populated

sleep 60

# first process the year to date
 
export InFile=/home/pablo/mail/haiku_archive
export OutFile=/var/www/haikupoet/archive
export InFile2=/home/pablo/mail/new_haiku
export OutFile2=/var/www/haikupoet/new_haiku
export Hype=/usr/bin/hypermail

echo "processing the Haiku Archive mailbox for `date +%Y`" 
$Hype -m $InFile -d $OutFile -x
# rm -f ${Outfile}/*html
# $Hype -m $InFile -d $OutFile -u

echo "processing new haiku into archive"
$Hype -m $InFile2 -d $OutFile2 -x

