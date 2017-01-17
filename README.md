# encrypt
Python program to encrypt files using AES-256bit cryptography and shred unencrypted files securely at the end of the process.
- - - - -
## What is this?
This is a python program that uses 'shemutils' and 'gevent' library to encrypt and decrypt files using AES algorithm with 128 or 256 bits key size.

## What more?
Aside from password encryption, this program offers to the user the option to generate 'key-files' that will act like passwords used in encryption.

This key file is stored in a local file in home folder of user, but encrypted with RSA 4096 bits.
Using the RSA private key, the program will decrypt the key file encryption and use its password to automatically conduce encryption/decryption operations.
By using this method - as it does not blocks with stdin inputs - enables the user to implement encryption/decryption shell scripts.

THE RSA PRIVATE KEY MUST BE STORED IN A SAFE, MOBILE DEVICE MEDIA TO ENSURE DATA SAFETY.

## Requirements
1. Linux (as it uses /dev/urandom)
2. Python 2.7.12
3. gevent
4. rsa
5. pycrypto

## How to install
To install this program you need to issue the following commands on your terminal:
> To install gevent: 
```bash 
cd /tmp
git clone https://github.com/gevent/gevent.git
cd gevent/
sudo python setup.py install
```

> To install shemutils:
```bash
cd /tmp
git clone https://github.com/0x00-0x00/shemutils.git
cd shemutils/
sudo python setup.py install
```

> To install "encrypt":
```bash
cd /tmp
git clone https://github.com/0x00-0x00/encrypt.git
cd encrypt/
sudo python setup.py install
```
