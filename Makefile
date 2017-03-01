CC=gcc
CFLAGS=-std=gnu99 -Wall
PROG=shemcrypt/keygenerator

crypt: shemcrypt/keygenerator.c
	$(CC) -o $(PROG) shemcrypt/keygenerator.c $(CFLAGS)

