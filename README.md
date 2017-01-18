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
1. Linux 
2. Python 2.7.12
3. gevent
4. rsa
5. pycrypto

## How to install
It is simple to start using this tool!

**via curl**
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/0x00-0x00/crypt/master/bootstrap.sh)"
```

**via wget**
```bash
sh -c "$(wget https://raw.githubusercontent.com/0x00-0x00/crypt/master/bootstrap.sh -O -)"
```

