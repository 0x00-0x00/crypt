import os
from shutil import copyfile
from sys import exit
from os import environ
from shemutils.logger import Logger
from shemutils.checksum import Checksum
from shemutils.encryption import Encryption
from shemcrypt.shred import shred_file

logger = Logger("INTEGRITY")


def get_temp_folder():
    if os.name == "posix":
        #  linux
        return "/tmp"
    elif os.name == "nt":
        #  windows
        return os.environ["TMP"]
    else:
        logger.critical("Error: Crypt does not support this operational system: {0}".format(os.name))
        exit(1)
    return 0


def integrity_check(origin_file, enc_file, key):
    """
    Function to verify the integrity of encrypted data.
    :param origin_file: Path to the unencrypted data file
    :param enc_file: Path to the encrypted data file
    :param key: Key object
    :return: 0 if succesfull
    """
    tmp_folder = get_temp_folder()
    tmp_file = tmp_folder + os.sep + os.path.basename(enc_file)

    #  Generate a hash from origin file
    origin_hash = Checksum(origin_file, "sha256")

    #  Copy encrypted data to a temporary folder for checkage.
    copyfile(os.path.abspath(enc_file), tmp_file)

    #  Check if temporary encrypted file exists.
    if not os.path.exists(tmp_file):
        logger.error("Integrity check failed as encrypted file is not on temporary folder.")
        return -1

    Encryption.decrypt_file(tmp_file, key)
    unencrypted_file, old_ext = os.path.splitext(tmp_file)

    if not os.path.exists(unencrypted_file):
        logger.error("Unencrypted file was not found.")
        return -1

    product_hash = Checksum(unencrypted_file, "sha256")

    if origin_hash.hexdigest != product_hash.hexdigest:
        logger.error("Hashes does not match!")
        logger.debug("O. Hash: {0} || P. Hash: {1}".format(origin_hash, product_hash))
        return -1

    try:
        shred_file(tmp_file)
        shred_file(unencrypted_file)
    except Exception as e:
        logger.error("Could not erase left-over data.")
        return -1
    return 0
