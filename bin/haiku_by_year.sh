#!/bin/bash

for i in `ls -1 print_archive*rb`
do
  j=`echo $i | cut -d'_' -f3`
  echo -n "${j} : "
  ./${i} | tail -1 | awk '{print $3}'
done
