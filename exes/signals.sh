#!/bin/bash


trap "echo hi!!" SIGINT SIGTERM
echo "PID is $$"

while :
do
	sleep 60
done
