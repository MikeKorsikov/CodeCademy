#!/bin/bash
first_greeting="Nice to meet you!"
later_greeting="How are you?"
greeting_occasion=1

if [ $greeting_occasion -lt 1 ]
then 
  echo $first_greeting
else
  echo $later_greeting
fi

# to run the script,  use the command: ./L6_3.sh
