#!/bin/bash

for i in 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015
do
  echo ${i} 
  for j in Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
  do
    echo -n "${j}: "
    ./print_archive_table.py $i | cut -d'>' -f5 | cut -d'<' -f1 | grep ${i} | grep ${j} | sort -n | uniq | wc -l
  done
  echo " "
done
