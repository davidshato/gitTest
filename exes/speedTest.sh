#!/bin/bash

USAGE()
{
	echo "USAGE : `basename $0` <Iterates> <Delay>"
	exit 1
}

if [[ $# == 2 ]]
	USAGE()
fi

echo "DATE,TIME,UPLOAD,DOWNLOAD" > speedtest.csv

delay=$2
iterates=$1

for (( i=0; $i<$iterates; i++ )) 
do

	speedtest-cli > temp.txt

	date=`date +%d-%m-%y`
	current_time=`date +%H:%M:%S`
	upload=`grep "Upload" temp.txt | cut -d ' ' -f 2`
	download=`grep "Download" temp.txt | cut -d ' ' -f 2`
	rm temp.txt
	echo "${date},${current_time},${upload},${download}" >> speedtest.csv

	sleep $delay
done

