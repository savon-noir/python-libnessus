#!/bin/sh

# run pyflakes on all the python source files in the repo
# run this to make it on precommit :
# ln -s pep8-pyflakes-pre-commit.sh .git/hooks/pre-commit
#FAULTS=$(find ./* -iname "*.py" -exec pyflakes {} \; 2>&1)
pyflakes libnessus/*.py 
FAULTS=$?
pep8 . --exclude test,docs,examples,build,dictdiffer
PEP=$?

if [[ $FAULTS != 0  || $PEP != 0 ]];
then
        exit 1
fi
