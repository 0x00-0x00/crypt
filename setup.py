from setuptools import setup, find_packages
from setuptools.command.install import install
from sys import exit
import os


#  Compile the C source code
def compile_c_sources():
    try:
        os.system("make")
        os.system("chmod 755 src/keygenerator")
    except:
        print("[!] Error: Could not compile C sources.")
        exit(1)
    return 0
compile_c_sources()


class PostInstall(install):
    def run(self):
        os.system("./post-install.sh")
        install.run(self)


setup(name='crypt-en',
      version='1.9.5',
      description="""
Shemhazai`s cryptography utility for cryptography.\n
    This program has the following features:
        AES (128-256bit key) file and message cryptography,
        Secure Key Storage system for Scripting cryptography.
        """,
      url='https://github.com/0x00-0x00/encrypt.git',
      author='Shemhazai',
      author_email='andre.marques@fatecp.sp.gov.br',
      license='MIT',
      packages=['shemcrypt'],
      package_dir={'shemcrypt': 'src'},
      package_data={'shemcrypt': ['src/*']},
      data_files=[
          ("shemcrypt", ["src/keygenerator"]),
          ],
      scripts=['bin/crypt', 'bin/crypt-keygen'],
      cmdclass={"install":PostInstall},
      zip_safe=False, install_requires=['gevent', 'rsa', 'pycrypto'])
