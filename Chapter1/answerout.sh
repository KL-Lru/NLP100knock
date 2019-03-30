#!/bin/bash
if type "python3" > /dev/null 2>&1; then
    com="python3"
elif type "python" > /dev/null 2>&1; then
    if [[ `python -V 2>&1 | awk '{print $2}'` =~ ^3 ]]; then
        com="python"
    else
        echo "Please setup environment to execute Python3."
        exit 1
    fi
else
    echo "Not Found Python... Please set up Python environment."
    exit 1
fi

if [[ -e out ]]; then
    rm out
fi

for i in `seq 0 9`; do
    efile="p0${i}.py"
    echo "Execute ${efile}..." 
    echo "<< Problem 0${i} >>" >> out
    ${com} ${efile} >> out
    echo "" >> out
done
echo "All execute out to 'out' "
