#!/bin/bash

# process the year to date
 
export InFile=/home/pablo/mail/haiku_archive
export OutFile=/var/www/haikupoet/archive
export Hype=/usr/bin/hypermail

echo "processing the Haiku Archive mailbox for `date +%Y`" 
$Hype -m $InFile -d $OutFile -x
# rm -f ${Outfile}/*html
# $Hype -m $InFile -d $OutFile -u

