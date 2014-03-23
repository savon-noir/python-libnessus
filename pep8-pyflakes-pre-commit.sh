#!/bin/sh

# run pyflakes on all the python source files in the repo
#FAULTS=$(find ./* -iname "*.py" -exec pyflakes {} \; 2>&1)
pyflakes .
FAULTS=$?
pep8 . --exclude test,docs,examples
PEP=$?

if [[ $FAULTS != 0  || $PEP != 0 ]];
then
        exit 1
fi
