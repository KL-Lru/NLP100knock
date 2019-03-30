#!/bin/bash
if test -e split_0; then
    rm split_*
fi

if test -e col1.txt; then
    rm col*.txt
fi

rm out