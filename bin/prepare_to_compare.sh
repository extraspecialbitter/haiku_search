#!/bin/bash

echo "synching up html archive"
rsync -lat --delete www.haikupoet.com:/var/www/haikupoet/archive/ /home/pablo/git/haiku_search/data/archive/

echo "generating a new table from the html archive"
./process_archive_2016_from_html.sh

echo "grabbing the last MySQL dump"
scp www.haikupoet.com:~/tmp/archive_2016.sql ~/tmp

echo "sourcing the MySQL dump locally"
mysql -u root -p -e "source ~/tmp/archive_2016.sql" haiku_archive
