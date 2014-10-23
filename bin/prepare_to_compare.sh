#!/bin/bash

echo "synching up html archive"
rsync -lat --delete mena@sasi.pair.com:/usr/home/mena/public_html/haikupoet/archive/ /home/pablo/git/haiku_search/data/archive/

echo "generating a new table from the html archive"
./process_archive_2014_from_html.sh

echo "grabbing the last MySQL dump"
scp www.extraspecialbitter.com:~/tmp/archive_2014.sql ~/tmp

echo "sourcing the MySQL dump locally"
mysql -u root -p -e "source ~/tmp/archive_2014.sql" haiku_archive
