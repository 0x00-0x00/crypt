[![Stories in Ready](https://badge.waffle.io/0x00-0x00/crypt.png?label=ready&title=Ready)](https://waffle.io/0x00-0x00/crypt)
# crypt - version 1.95
## Description
Python program to encrypt files using AES-256/128bit combined with RSA-4096 cryptography and shred unencrypted files securely at the end of the process.

## What more?
Aside from password encryption, this program offers to the user the option to generate 'key-files' that will act like passwords used in encryption.

This key file is stored in a local file in home folder of user, but encrypted with RSA 4096 bits.
Using the RSA private key, the program will decrypt the key file encryption and use its password to automatically conduce encryption/decryption operations.
By using this method - as it does not blocks with stdin inputs - enables the user to implement encryption/decryption shell scripts.

THE RSA PRIVATE KEY MUST BE STORED IN A SAFE, MOBILE DEVICE MEDIA TO ENSURE DATA SAFETY.

## Requirements
1. Linux
2. Python 3.6
3. git
4. make

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

Or clone it and install using bootstrap.sh:

```bash
git clone https://github.com/0x00-0x00/crypt.git
cd crypt/
./bootstrap.sh
```

And it will be installed!


Notes:


If your python3.6 is 'python' in your PATH, you'll need to link it using:
```bash
# confirm your python version
user@pc$ python -V
Python 3.6.0
...
root@pc# ln -s $(which python) /usr/local/bin/python3.6 
```

## Generating key files
To generate a key-file for your system user:
```bash
user@pc$ crypt-keygen
-
Crypt-KeyGen instruction to private key storage
YOUR PRIVATE KEY IS YOUR MOST IMPORTANT FILE
So its storage MUST occur in removable media.
DO NOT STORE IT IN HARD DRIVES. EVEN IF ENCRYPTED.
Give a valid location (folder) to store your private key: /home/test/keyfolder
14:42:45 [crypt-keygen] INFO: [*] Key location: /home/test/keyfolder/
14:42:45 [RSA] INFO: [*] Generating new 4096-bits key pair ...
14:43:48 [RSA] INFO: [*] Key pair generation took 63.14277672767639 seconds.
14:43:48 [RSA] INFO: [*] Private key saved to file '/home/test/keyfolder/.priv.key'

user@pc$ crypt-keygen --check
14:46:51 [crypt-keygen] INFO: [*] Key location: /home/test/keyfolder/
14:46:51 [crypt-keygen] INFO: [*] Secret key file: /home/test/.crypt/secret_key
14:46:51 [crypt-keygen] INFO: [*] Private key location: /home/test/keyfolder/
14:46:51 [crypt-keygen] INFO: [*] Everything is ok.
```

## Usage
To encrypt or decrypt a file 'FILE.EXT' using a text password:
```bash
crypt --encrypt --file FILE.EXT
crypt --decrypt --file FILE.EXT
```

To encrypt or decrypt a file 'FILE.EXT' using key-files: 
```bash
crypt --encrypt -k --file FILE.TXT
crypt --decrypt -k --file FILE.EXT
```

Not only files can be encrypted, all kinds of stdin data could be encrypted with "-m" (message) argument:
```bash
echo "This is a secret message" | crypt --encrypt -k -m -
[crypt v. 1.95]
revision: 2017/03/05
13:49:15 [CRYPT] INFO: [*] Operation mode set to: Encryption
13:49:15 [CRYPT] INFO: [*] Output option set to: Message
13:49:16 [CRYPT] INFO: [*] Cipher: 
SgAAAAAAAAA6yEpTDRMWkk8boUA7KxPyTtb8hOr/oyEyAcJW0olsTUezwfnPCZn10K4E/PAgBDI=
```