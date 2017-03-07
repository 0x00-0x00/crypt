CC=gcc
CFLAGS=-std=gnu99 -Wall
PROG1=src/keygenerator
PROG2=src/shredder
PROG3=src/count_bytes

crypt: src/keygenerator.c
	$(CC) -o $(PROG1) src/keygenerator.c $(CFLAGS)
	$(CC) -o $(PROG2) src/shredder.c $(CFLAGS)
	$(CC) -o $(PROG3) src/count_bytes.c $(CFLAGS)


