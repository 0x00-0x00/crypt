#!/usr/bin/env bash
mkdir ~/.crypt
cp crypt.conf ~/.crypt/crypt.conf
cp ./.priv.key ./.pub.key /
echo "[*] Deployed keys and configuration."