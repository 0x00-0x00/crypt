#!/bin/bash

# Bootstrap script for crypt
# Written by zc00l/shemhazai

# Static variables
uid=$(id -u)
python_modules=(pycrypto rsa gevent)

function header
{
    echo "##########################";
    echo "| crypt bootstrap script |";
    echo "##########################";
    echo "";
}

}
function check_root
{
    if [ "$1" != "0" ]; then
        echo "[!] Only root can install python modules.";
        exit;
    fi
}

function check_exists
{
    echo "[+] Check if $1 exists ...";
    $2 > /dev/null 2>&1
    if [ "$?" == "0" ]; then
        echo "[+] $1 detected on $(which $1)";
        return 0;
    else
        echo "[!] $1 is not installed or not in PATH variable";
        exit;
    fi
}

function install_python_modules
{
    for module in "${python_modules[@]}"
    do
        echo "[+] Installing python module: ${module}";
        pip install ${module} --upgrade > /dev/null 2>&1;
    done
}

function install_repo
{
    echo "[+] Changing current working directory to '/tmp' ...";
    cd /tmp;
    echo "[+] Cloning $1 ...";
    git clone $2 > /dev/null 2>&1;
    cd $1;
    echo "[+] Installing $1 ...";
    python setup.py install;
}

# Print header
header

# Checkage before running script to ensure working state
check_root ${uid}
check_exists "pip" "pip --help"
check_exists "git" "git --help"
check_exists "python" "python -V"

# Work
install_python_modules
install_repo "shemutils" "https://github.com/0x00-0x00/shemutils.git"

