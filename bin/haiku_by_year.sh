#!/bin/bash

for i in 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015
do
  echo -n "${i} : "
  ./print_archive_table.py $i | tail -1 | awk '{print $3}'
done
