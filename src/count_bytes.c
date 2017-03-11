//
// Created by shemhazai on 3/7/17.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define BUFSIZE 256
#ifndef DEBUG
#define DEBUG 0
#endif

char* count_bytes(long long size)
{
    if(DEBUG == 1) {
        fprintf(stdout, "[DEBUG] long long size: %llu\n", size);
    }

    char* buffer = malloc(sizeof(char) * BUFSIZE);
    long long tera, giga, mega, kilo;

    tera = (long long)pow(2, 40);
    giga = (long long)pow(2, 30);
    mega = (long long)pow(2, 20);
    kilo = (long long)pow(2, 10);

    if(size >= tera) {
        double q = size / (double)tera;
        sprintf(buffer, "%2.2f TiB", q);
    } else
    if(size >= giga) {
        double q = size / (double)giga;
        sprintf(buffer, "%2.2f GiB", q);
    } else
    if(size >= mega) {
        double q = size / (double)mega;
        sprintf(buffer, "%2.2f MiB", q);
    } else
    if(size >= kilo) {
        double q = size / (double)kilo;
        sprintf(buffer, "%2.2f KiB", q);
    } else {
        sprintf(buffer, "%2.0f Bytes", (double)size);
    }

    return buffer;
}


int main(int argc, char* argv[])
{
    char *str = NULL;
    if(argc < 2) {
        return -1;
    }
    long long size;
    size = atoll(argv[1]);
    str = count_bytes(size);
    fprintf(stdout, str);
    free(str);
    return 0;
}
