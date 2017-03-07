import shemcrypt
import os
import time
import subprocess

from shemutils.logger import Logger
from shemutils.shred import Shredder
from sys import exit


shredlogger = Logger("Shred")


def shred_file(f):
    if os.name == "posix":
        shredder = os.path.dirname(shemcrypt.__file__) + os.sep + "shredder"
        if not os.path.exists(shredder):
            logger.error("Could not find shredder program. Maybe you need to reinstall crypt.")
            exit(1)

        proc = subprocess.Popen([shredder, str(os.path.abspath(f)), str(os.path.getsize(f))],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        while proc.poll() is None:
            time.sleep(1)

        if proc.poll() != 0:
            return -1

        try:
            os.remove(f)
        except Exception as e:
            logger.error(e)
            return -1

    elif os.name == "nt":
        shredder = Shredder()
        if shredder.shred(f, remove=True) != 0:
            return -1

    else:
        return -1
    return 0