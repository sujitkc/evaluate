#!/bin/bash

rollnums=(
	rn001
	rn002
	rn003
	rn004
	rn006
	rn007
	rn009
	rn010
	rn011
	rn012
	rn013
)

for rn in ${rollnums[@]}; do
  echo "*************************** $rn - begin ****************************************"
  if [ ! -d ../submissions/$rn ]; then
    echo "Submission not found."
  else
    ./eval.sh $rn
  fi
  echo "*************************** $rn - end ****************************************"
done
