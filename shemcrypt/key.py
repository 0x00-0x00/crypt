from gevent.event import Event
import os


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

    def get(self, encoded=None):
        if self.key_status.is_set() is True and encoded is None:
            return self.key
        elif self.key_status.is_set() is True and encoded is not None:
            return self.key.encode("base64")
        else:
            raise KeyNotSet

    def _generate_key(self):
        return os.urandom(self.key_size)

    def _key_validation(self):
        if self.key_size % 2 != 0:
            raise InvalidKeySize
        return True
