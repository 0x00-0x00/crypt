#!/bin/bash
# ------------------------------------------------
# Post-installation script by zc00l
#  Removes all files specified at junk array.
# ------------------------------------------------

junk=("src/keygenerator")

for junk_file in "${junk[@]}";
do
    if [[ -e ${junk_file} ]]; then
        echo -n "Deleting ${junk_file}: ";
        rm ${junk_file};
        if [[ $? != 0 ]]; then
            echo "FAIL";
        else
            echo "OK";
        fi
    fi
done
