from shemutils import Logger
import os

shredlogger = Logger("Shred")


def shred_file(f, n=2):
    """
    Shred a file in a really tight secure manner
    :param f: string containing file name
    :param r: string containing random generator file
    :param n: int containing number of passes
    :return: 0 if successful
    """
    '# Get file size in bytes'
    file_size = os.path.getsize(f)
    if file_size < 0:
        return None

    patterns = [os.urandom(1) for x in range(n)]

    x = 1  # count passes

    '# Open file handle'
    with open(f, "wb+") as fd:
        for p in patterns:

            '# Overwrite data with random pattern byte '
            for y in xrange(file_size):
                fd.write(p)
            shredlogger.info("Shred pass #{0} using byte '{1}' done for file '{2}'".format(x, p, f))
            x += 1

        lpb = '\x00'
        for y in xrange(file_size):
            fd.write(lpb)
        shredlogger.info("Shred pass #{0} using byte '{1}' done for file '{2}'".format(x, lpb, f))

    os.remove(f)  # deletes file from OS
    return 0
