CC=gcc
CFLAGS=-std=gnu99 -Wall
PROG=src/keygenerator

crypt: src/keygenerator.c
	$(CC) -o $(PROG) src/keygenerator.c $(CFLAGS)

