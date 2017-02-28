#!/usr/bin/env python3.6
import subprocess


#  Variable definition
script = "randombytes.pl"


def main():
    proc = subprocess.Popen(["perl", script], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    print("Key is {0}".format(stdout.decode()))
    return 0


if __name__ == "__main__":
    main()
