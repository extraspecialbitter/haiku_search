#!/bin/bash

day_and_month=`date +%d-%b`
day_month_and_year=`date +%d-%b-%Y`
this_year=`date +%Y`

day_tally=`${HOME}/git/haiku_search/bin/print_archive_table.py ${this_year} | grep ${day_and_month}`
day_count=`${HOME}/git/haiku_search/bin/print_archive_table.py ${this_year} | grep -c ${day_and_month}`

echo " "
echo "${day_tally}"
echo " "
echo "${day_count} haiku written on ${day_month_and_year} (so far)"
