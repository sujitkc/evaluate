#!/bin/bash
rn=$1
echo "Getting submission for ${rn} ..."
rm -r code/*
cp -r ../submissions/${rn}/*.py code
# cp drivers/*.py code
echo "Getting submission for ${rn} ... done."
touch code/__init__.py
echo "Evaluating submission for ${rn} ..."
python3 eval_all.py ${rn}
echo "Evaluating submission for ${rn} ... done."
