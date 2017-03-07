//
// Created by shemhazai on 3/7/17.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define BUFSIZE 256

char* count_bytes(long long size)
{

    char* buffer = malloc(sizeof(char) * BUFSIZE);
    long tera, giga, mega, kilo;

    tera = (long)pow(2, 40);
    giga = (long)pow(2, 30);
    mega = (long)pow(2, 20);
    kilo = (long)pow(2, 10);

    if(size >= tera) {
        double d = pow(10, 5);
        double q = size / tera;
        double y = (size % tera) /d;
        q += y;
        sprintf(buffer, "%2.2f TiB", q);
    } else
    if(size >= giga) {
        double d = pow(10, 4);
        double q = size / giga;
        double y = (size % giga) / d;
        q += y;
        sprintf(buffer, "%2.2f GiB", q);
    } else
    if(size >= mega) {
        double d = pow(10, 3);
        double q = size / mega;
        double y = (size % mega) / d;
        q += y;
        sprintf(buffer, "%2.2f MiB", q);
    } else
    if(size >= kilo) {
        double d = pow(10, 2);
        double q = size / kilo;
        double y = (size % kilo) / d;
        q += y;
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
    off_t size;
    size = atoll(argv[1]);
    str = count_bytes(size);
    fprintf(stdout, str);
    free(str);
    return 0;
}