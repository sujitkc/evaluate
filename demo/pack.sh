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
  rn012
  rn013
)

files=(
  eval.sh
  __pycache__
  *.txt
  *.csv
)
for rn in ${rollnums[@]}; do
  if [ -d submissions/$rn ]; then
    # step 1
    mkdir evaluated-package/$rn
    mkdir evaluated-package/$rn/code
    touch evaluated-package/$rn/code/__init__.py


    # step 2 - copy answers
    cp submissions/$rn/* evaluated-package/$rn/code
    # step 3 - copy evaluation directories
    cp ~/IIITB/projects/evaluate/evaluate/evaluate.py evaluated-package/$rn/
    cp evaluation/*.py evaluated-package/$rn/
    cp -r evaluation/mycode evaluated-package/$rn/

    # step 4 - remove redundant files
    for fn in ${files[@]}; do
      rm -r evaluated-package/$rn/evaluation/$fn
    done

    # step 5
    cp -r evaluated-package/$rn .
    tar czf $rn.tar.gz $rn
    mv $rn.tar.gz evaluated-package
    rm -r $rn
  fi

done
