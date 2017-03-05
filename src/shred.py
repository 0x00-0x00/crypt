from shemutils.logger import Logger
import os

shredlogger = Logger("Shred")


def shred_file(f, n=2):
    """
    Shred a file in a really tight secure manner
    :param f: string containing file name
    :param n: int containing number of passes
    :return: 0 if successful
    """
    '# Get file size in bytes'
    file_size = os.path.getsize(f)
    if file_size < 0:
        return None

    patterns = [os.urandom(1) for _ in range(n)]

    x = 1  # count passes

    '# Open file handle'
    with open(f, "wb+") as fd:
        for p in patterns:

            '# Overwrite data with random pattern byte '
            for _ in range(file_size):
                fd.write(p)
            shredlogger.info("Shred pass #{0} using byte '{1}' done for file '{2}'".format(x, p, f))
            x += 1

        for _ in range(file_size):
            fd.write(b'\x00')
        shredlogger.info("Shred pass #{0} using byte '{1}' done for file '{2}'".format(x, '\00', f))

    os.remove(f)  # deletes file from OS
    return 0
