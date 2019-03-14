#!/bin/bash

cat < /dev/ttyACM0 > $1_oh.csv &
sleep 1m
pkill cat


awk -v FS=',' 'NF==5' $1_oh.csv > $1.csv

