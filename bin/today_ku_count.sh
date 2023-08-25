#!/bin/bash

day_and_month=`date +%d-%b`
day_month_and_year=`date +%d-%b-%Y`
this_year=`date +%Y`

day_tally=`${HOME}/git/haiku_search/bin/print_archive_table.py ${this_year} | grep -c ${day_and_month}`

echo "${day_tally} haiku written on ${day_month_and_year} (so far)"
