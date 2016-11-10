from setuptools import setup, find_packages

setup(name='crypt-br',
      version='1.6',
      description="""
Shemhazai`s cryptography utility for cryptography.\n
    This program has the following features:
        AES (128-256bit key) file and message cryptography,
        """,
      url='https://github.com/0x00-0x00/encrypt.git',
      author='Shemhazai',
      author_email='nestorm2486@gmail.com',
      license='MIT',
      scripts=['bin/crypt'],
      zip_safe=False)
