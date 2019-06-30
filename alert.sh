#!/bin/bash
curl -s  https://weather.gc.ca/rss/battleboard/$1.xml | sed -n 's:.*<title>\(.*\)</title>.*:\1:p' | sed  '1d' | sed  's/in effect//gI' | cut -d',' -f1 | head -1 

