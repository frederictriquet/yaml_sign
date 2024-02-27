#!/usr/bin/env bash
export SIGNKEY=S0m3key
echo "Sign files"
python sign.py unsigned.yml signed.yml
python sign.py unsigned2.yml signed2.yml
echo
echo "Check signed.yml"
python check.py signed.yml
echo
echo "Modify signed.yml -> altered.yml"
sed s/abcd/abdc/ signed.yml > altered.yml
echo
echo "Check altered.yml"
python check.py altered.yml
echo
echo "Compare signatures of identical files"
grep signature signed.yml signed2.yml
