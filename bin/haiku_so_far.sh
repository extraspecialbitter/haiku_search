#!/bin/bash

export count=0
for i in `ls -1 print_archive*rb`
do
  j=`echo $i | cut -d'_' -f3`
  k=`./${i} | tail -1 | awk '{print $3}'`
  count=`expr $count + $k`
done
echo "$count haiku written so far"
