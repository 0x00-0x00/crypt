#include <time.h>
#include <stdlib.h>

unsigned int main(int argc, char* argv[])
{
    srand(time(NULL)); // Generate seed generator ///
    unsigned int outsider_seed;
    if(argv[1] == NULL) {
        outsider_seed = 0;
    } else {
        outsider_seed = atoi(argv[1]);
    }
    unsigned int x,y,z,c;
    x = (rand() * 23231313 + outsider_seed);
    y = (x + 331987663);
    z = (x * 32 - 1);
    c = (rand() + (z + 666) + outsider_seed);
    unsigned long long t;
    x = 314527869 * x + 1234567 + outsider_seed;
    y ^= y << 5; y ^= y >> 7; y ^= y << 22;
    t = 4294584393ULL * z + c; c = t >> 32; z = t;
    return x + y + z;
}
