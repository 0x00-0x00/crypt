from setuptools import setup, find_packages

setup(name='crypt-en',
      version='1.8',
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
      package_dir={'shemcrypt': 'shemcrypt'},
      package_data={'shemcrypt': ['shemcrypt/*']},
      scripts=['bin/crypt', 'bin/crypt-keygen'],
      zip_safe=False, install_requires=['gevent'])
