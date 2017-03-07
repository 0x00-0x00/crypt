import gzip
import shutil
import os
from shemutils.logger import Logger
from shemcrypt.integrity import get_temp_folder

logger = Logger("COMPRESSION")


def decompress_file(file):
    temporary_folder = get_temp_folder()
    if not os.path.exists(temporary_folder):
        logger.error("Temporary folder '{0}' does not exists.".format(temporary_folder))
        return -1

    base_name = os.path.basename(file)
    temporary_file = os.path.join(temporary_folder, base_name)

    with gzip.open(file, "rb", compresslevel=9) as f:
        _data = f.read()
    original_size = os.path.getsize(file)

    with open(temporary_file, "wb") as f:
        f.write(_data)
    decompressed_size = os.path.getsize(temporary_file)

    #  Temporary file checkage
    if not os.path.exists(temporary_file):
        logger.error("Could not detect compressed file.")
        return -1

    pctg = (decompressed_size / original_size) * 100.0
    if pctg > 100:
        logger.info("File '%s' got %.2f%% bigger due decompression." % (file, pctg))
    else:
        logger.info("File '%s' got %.2f%% smaller due decompression." % (file, pctg))

    return temporary_file


def compress_file(file):
    temporary_folder = get_temp_folder()
    if not os.path.exists(temporary_folder):
        logger.error("Temporary folder '{0}' does not exists.".format(temporary_folder))
        return -1

    #  Get the file base name
    base_name = os.path.basename(file)
    temporary_file = os.path.join(temporary_folder, base_name)

    #  Load  the file into memory
    with open(file, "rb") as f:
        _data = f.read()
    original_size = os.path.getsize(os.path.abspath(file))

    #  Write a compressed file into a temporary location
    with gzip.open(temporary_file, "wb", compresslevel=9) as f:
        f.write(_data)

    #  Temporary file checkage
    if not os.path.exists(temporary_file):
        logger.error("Could not detect compressed file.")
        return -1

    # Count the size
    compressed_size = os.path.getsize(temporary_file)

    pctg = (compressed_size/original_size) * 100.0
    if pctg < 100:
        logger.info("File '%s' got %.2f%% smaller due compression." % (file, pctg))
    else:
        logger.info("File '%s' got %.2f%% bigger due compression." % (file, pctg))

    return temporary_file

