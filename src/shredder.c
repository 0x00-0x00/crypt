//
// Created by shemhazai on 3/7/17.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <time.h>
#include <math.h>

#define CHUNK_SIZE 1024
#define BUFSIZE 256


void get_rnd_byte(char *ptr, FILE* fp)
{
    fread(ptr, 0x1, CHUNK_SIZE, fp);
}


int shred(char* filename, long long size) {
    FILE* fp;
    FILE *urand;

    fp = fopen(filename, "wb");
    size_t k = sizeof(char) * CHUNK_SIZE;

    long long i = 0;

    char byte[CHUNK_SIZE];

    /* Open urandom file */
    urand = fopen("/dev/urandom", "r");
    if (urand == NULL)
    {
        printf("Error opening /dev/urandom!\n");
        return 1;
    }


    /* Set file descriptor to point to the 0-index byte of file. */
    fseek(fp, 0L, SEEK_SET);

    for(i = 0; i < size; i += k)
    {
        /* Function to get random data from urandom */
        get_rnd_byte(byte, urand);

        /* IF conditional to ensure the program does not over overwrite data. */
        if( (size - i) < CHUNK_SIZE )
        {
            k = sizeof(char) * (size - i);
        }

        /* Writes N(k) bytes to file pointer. */
        fwrite(byte, 0x1, k, fp);
    };


    /*Closes urand file descriptor */
    fclose(fp);
    fclose(urand);
    return 0;
}


int main(int argc, char* argv[])
{
    if(argc < 3) {
        return -1;
    }

    char* filename = argv[1];
    long long size = atoll(argv[2]);
    shred(filename,size);
    return 0;
}