#!/bin/bash


curl -s  https://weather.gc.ca/rss/city/$1.xml | sed -n 's:.*<summary type="html">\(.*\)</summary>.*:\1:p'| sed '1d' | sed  's/in effect//gI' | sed  's/Forecast issued.*//gI' | cut -d',' -f1 | sed  's/\ mm\>/ milimeters/g' | sed 's/\km\/h\>/ kilometers per hour/g' | sed  's/\High\>/High of/g' | sed  's/\Low\>/Low of/g' | tail -12 | head -1

