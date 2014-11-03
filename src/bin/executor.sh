#!/bin/bash

if test ! -z "$GCP"
then
	cd $GCP/bin
fi

if test -z "$GCP"
	then
	echo "\n Not found GCP \n"
	GCP=..
  export GCP
  else 
  echo "GCP:$GCP"
fi

case "$1" in
	'start')
	cd $GCP/
	python lib/gcp/Startup.py
	;;
	*)
	echo "gcp v1.0, boco ltd. (c)2014-2015"
	echo "usage: ./executor.sh <command>"
	echo "       command = < start | help >"
	echo "       start: start  gcp in current shell, and in background if succeded with &."
	echo "              the program should be execute with root privelage."
	echo "       stop:  stop the running program."
	;;
esac
