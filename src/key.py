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
    :param: bits -> Key size

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
