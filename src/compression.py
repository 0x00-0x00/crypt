import gzip
import shutil
import os
import subprocess
import shemcrypt
from shemutils.logger import Logger
from shemcrypt.integrity import get_temp_folder
from sys import exit

logger = Logger("COMPRESSION")


def count_size(n):
    count_bytes = os.path.dirname(shemcrypt.__file__) + os.sep + "count_bytes"
    if not os.path.exists(count_bytes):
        logger.critical("Could not find the count_bytes binary. Maybe \
                a reinstall is needed.")
        exit(1)
    proc = subprocess.Popen([count_bytes, str(n)], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout


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

    #  Log the file size information
    logger.info("Original file size: {0}".format(count_size(original_size)))
    logger.info("Decompressed file size: {0}".format(
        count_size(decompressed_size)))

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

    #  Log the file size information
    logger.info("Original file size: {0}".format(count_size(original_size)))
    logger.info("Compressed file size: {0}".format(
        count_size(compressed_size)))

    pctg = (original_size/compressed_size) * 100.0
    if pctg < 100:
        logger.info("File '%s' got %.2f%% bigger due compression." % (file, pctg))
    else:
        logger.info("File '%s' got %.2f%% smaller due compression." % (file, pctg))

    return temporary_file

