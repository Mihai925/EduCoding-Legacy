#!/bin/bash
if [[ "$1" = "python" ]]; then
   if [ -z "$3" ]
    then
      python $2
   else
      echo "$3" | python $2
   fi
fi