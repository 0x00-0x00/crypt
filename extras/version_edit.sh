#!/usr/bin/env bash

if [[ $1 == "" ]]; then
    echo -e "\033[1mUsage\033[0m: $0 <CURR_VERSION> <NEW_VERSION>";
    exit;
fi

function change_version
{
    cd ../
    echo -e -n "[*] Updating \033[092msetup.py\033[0m version ... "
    sed -i "s/version='${1}'/version='${2}'/" setup.py
    if [[ $? == 0 ]]; then
        echo -e "\033[092mOK\033[0m";
    else
        echo -e "\033[091mFAIL\033[0m";
    fi

    echo -e -n "[*] Updating \033[092mREADME.md\033[0m version ... ";
    sed -i "s/${1}/${2}/g" README.md;
    if [[ $? == 0 ]]; then
        echo -e "\033[092mOK\033[0m";
    else
        echo -e "\033[091mFAIL\033[0m";
    fi

    cd bin/
    echo -e -n "[*] Updating main \033[092mcrypt binary\033[0m version ... "
    sed -i "s/__VERSION__ = '${1}'/__VERSION__ = '${2}'/" crypt
    if [[ $? == 0 ]]; then
        echo -e "\033[092mOK\033[0m";
    else
        echo -e "\033[091mFAIL\033[0m";
    fi

    timestamp=$(date +%Y/%m/%d | sed 's/\//\\\//g')
    echo -e -n "[*] Updating revision date ... "
    sed -i "s/__revision__ = '[0-9/]*'/__revision__ = '${timestamp}'/" crypt
    if [[ $? == 0 ]]; then
        echo -e "\033[092mOK\033[0m";
    else
        echo -e "\033[091mFAIL\033[0m";
    fi
}


change_version "$1" "$2"
