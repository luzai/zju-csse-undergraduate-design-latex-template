#!/usr/bin/env bash
#
# run make whenever something (anything, really) changes in the directory
# needs inotifywait which is in
# $ apt-get install inotify-tools
while [ 1 ] ;  do
  # inotifywait -e close_write,moved_to,create,modify thesis.tex |
  # while read -r filename events; do
  #   echo ">> GUARD: running make " ${events} ${filename} 
  #   make
  # done
  make 
  sleep 600
done