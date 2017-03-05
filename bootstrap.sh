#!/bin/bash
#  -----------------------
# Bootstrap script for crypt
# Written by zc00l/shemhazai
#  -----------------------


# Static variables
uid=$(id -u);
python_modules=("pycrypto" "rsa" "gevent");


function header
{
    echo "crypt bootstrap script";
    echo "----------------------";
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
    echo -n "[+] Checking $1: ";
    program_path=$(which $1);
    if [[ ! -e "$program_path" ]]; then
        echo "FAIL";
        return 1;
    else
        echo "OK";
        return 0;
    fi
}


function install_python_modules
{
    for module in "${python_modules[@]}"
    do
        echo -n "[+] Installing python module ${module}: ";
        pip3.6 install ${module} --upgrade > /dev/null 2>&1;
        if [[ $? != 0 ]]; then
            echo "FAIL";
            return 1;
        else
            echo "OK";
        fi
    done
    return 0;
}


function install_cpan_modules
{
    modules=("Log::Log4perl", "Bytes::Random::Secure");
    for module in "${modules[@]}"
    do
        echo -n "[+] Installing cpan module ${module}: ";
        cpan install ${module};
        if [[ $? != 0 ]]; then
            echo "FAIL";
            return 1;
        else
            echo "OK";
        fi
    done
    return 0;
}


function install_repo
{
    echo "[+] Changing current working directory to '/tmp' ...";
    cd /tmp;
    echo "[+] Cloning $1 ...";
    git clone $2 > /dev/null 2>&1;

    cd $1;
    echo "[+] Installing $1 ...";
    python3.6 setup.py install;
}


function not_installed
{
    echo "[!] $1 is not installed or included at the PATH variable.";
    exit;
}

# Print header
header

# Checkage before running script to ensure working state
check_root ${uid}

check_exists "make"
if [[ $? != 0 ]]; then
    not_installed "make"
fi

check_exits "gcc"
if [[ $? != 0 ]]; then
    not_installed "gcc"
fi

check_exists "pip3.6"
if [[ $? != 0 ]]; then
    not_installed "pip3.6";
fi

check_exists "git"
if [[ $? != 0 ]]; then
    not_installed "git";
fi

check_exists "python3.6"
if [[ $? != 0 ]]; then
    not_installed "python3.6";
fi

# Work

#  Perl is not used in the project right now.
#  So installing it is useless.

#check_exists "cpan"
#if [[ $? != 0 ]]; then
#    not_installed "cpan";
#fi

#install_cpan_modules
#if [[ $? != 0 ]]; then
#    echo "[!] Error: Perl modules could not be installed for some reason. Fix it.";
#    exit;
#fi

install_python_modules
if [[ $? != 0 ]]; then
    echo "[!] Error: Python modules could not be installed for some reason. Fix it.";
    exit;
fi


install_repo "shemutils" "https://github.com/0x00-0x00/shemutils.git"
install_repo "crypt" "https://github.com/0x00-0x00/crypt.git"

