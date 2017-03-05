from os import mkdir, path, environ, sep
import re


home = environ["HOME"] + sep
crypt_folder = home  + ".crypt"
config_file = "%s.crypt/crypt.conf" % home
secret_key_file = "%s.crypt/secret_key" % home

INSTRUCTIONS = """
Crypt-KeyGen instruction to private key storage
YOUR PRIVATE KEY IS YOUR MOST IMPORTANT FILE
So its storage MUST occur in removable media.
DO NOT STORE IT IN HARD DRIVES. EVEN IF ENCRYPTED.
"""


TEMPLATE = """
# CONFIG FILE FOR CRYPT KEYGEN
private_key_location=%s
"""


def create_folders(flds):
    for folder in flds:
        try:
            mkdir(folder)
            return 0
        except OSError as e:
            if e.errno == 17:
                pass
                return 0
            else:
                print("Error #%d: %s" % (e.errno, e.strerror))
                return e.errno


def set_up_main_folder():
    folders = [crypt_folder]
    if create_folders(folders) != 0:
        return -1
    return 0


def setup_full():

    #  Set-up all the required folders
    if set_up_main_folder() != 0:
        return -1
    return 0


def get_private_key_location(conf=config_file):
    """
    Function to handle configuration creation and key location finding
    :param conf:
    :return: private key location
    """
    def get_location(data):
        pattern = "(?P<config_var>[a-z_]+)\s?=\s?(?P<value>[aA-zZ~\/\.]+)"
        m = re.match(pattern, data.decode())
        if m is not None:
            return m.groupdict()
        else:
            return None

    if not path.isfile(conf):  # no configuration file == needs a key location
        print(INSTRUCTIONS)  # give some good advice
        k = input("Give a valid location (folder) to store your private key: ")
        with open(conf, "wb") as f:
            f.write((TEMPLATE % k).encode())

    file_data = open(conf, "rb").read()
    if len(file_data) < 1:
        return -1

    key_location = None
    for line in file_data.split(b"\n"):
        if get_location(line):
            try:
                x = get_location(line)
                if x["config_var"] == "private_key_location":
                    key_location = x["value"]
                    if key_location[len(key_location)-1] != sep:
                        key_location += sep
            except KeyError:
                print("key error")
                return -1

    return key_location
