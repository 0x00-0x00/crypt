#!/bin/bash


KEYSIZE=32 # AES uses 256 bits key


if [[ $1 == "" ]]; then
    echo "Usage: $0 <Kn>";
    echo "Where Kn stands for number of keys to be generated.";
    exit;
fi

echo -n "[+] Generating keys: "
for i in $(seq 1 $1);
do
    ./keygen $KEYSIZE > chave_${i}.key;
    if [[ $i == $1 ]]; then
        echo "OK";
        exit;
    fi
done

echo "FAIL";
exit;
