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

if [[ -e "jawiki-country.json.gz" ]]; then
    echo "File 'jawiki-country.json.gz' found."
else
    echo "There is no file 'jawiki-country.json.gz'. Please DL from NLP100本ノック."
    exit 1
fi

if [[ -e out ]]; then
    rm out
fi

echo "In this chapter, out only 30 lines each program"
for i in `seq 0 9`; do
    efile="p2${i}.py"
    echo "Execute ${efile}..." 
    echo "<< Problem 2${i} >>" >> out
    ${com} ${efile} | head -n 30 >> out
    if [[ $i -eq 0 ]];then
        echo "In this, BrokenPipeError not break result. (It cause for redirect to 'head' command)"
    fi
    echo "" >> out
done
echo "All execute out to 'out' "
