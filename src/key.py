from shemcrypt.configuration import secret_key_file, get_private_key_location
from shemutils.encryption import Encryption, RSA
from gevent.event import Event
from sys import exit
import os
import shemcrypt
import subprocess
import base64


class KeyNotSet(Exception):
    pass


class InvalidKeySize(Exception):
    pass


class Key(object):
    """
    Key object.
    :param: bytes -> Key size

    Methods:
        new() -> generate a key
        get() -> returns a string with the key
    """
    def __init__(self, bits):
        self.key_size = bits
        self.key = ""
        self.key_status = Event()

    def new(self):
        if self._key_validation() is True:
            self.key = self._generate_key()
            self.key_status.set()
        return

    def get(self):
        if self.key_status.is_set() is True:
            return self.key
        else:
            raise KeyNotSet

    def _generate_key(self):
        #  Uses the new RNG system avoiding os.urandom()
        keygen = os.path.dirname(shemcrypt.__file__) + os.sep + "keygenerator"
        if not os.path.exists(keygen):
            print("[!] Error: Could not find key generator file. Maybe reinstall is needed.")
            exit(1)

        # Execute the key generator and retrieve a cryptographic base64-encoded key
        proc = subprocess.Popen([keygen, str(self.key_size)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        key, err = proc.communicate()
        if key is None or key is "":
            print("[!] Error: Could not generate a key.")
            exit(1)
        return key

    def _key_validation(self):
        if self.key_size % 2 != 0:
            raise InvalidKeySize
        return True


class KeyFile(object):
    def __init__(self, fd):
        self.data = str(fd.read().decode().replace(pem_header, "")).replace(
            pem_footer, "")
        self.encrypted_data = base64.b64decode(self.data)
        self.key_location = get_private_key_location()
        self.rsa = RSA()
        if not self.key_location:
            print("Type 'crypt-keygen' to generate a key file.")
            exit(1)
        self.priv_f, self.pub_f = self.key_location + ".priv.key", self.key_location + ".pub.key"
        self.rsa.load_keys(priv_f=self.priv_f, pub_f=self.pub_f)

    def _decrypt_key(self):
        return self.rsa.decrypt_message(self.encrypted_data)

    def get(self):
        return Encryption.hash256(self._decrypt_key())

