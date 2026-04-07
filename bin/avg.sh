#!/bin/bash

  first=$(${HOME}/git/haiku_search/bin/print_archive_table.py 2026 | tail -1)
  tally=$(echo "${first}" | awk '{print $3}')
  jdate=$(date +%j)
  avg=$(expr ${tally} / ${jdate})
  echo "Average number of daily haiku so far this year = ${avg}"
