gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/ -c lib-misc.c
gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/ -c lib-timing.c
gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/ -c lib-mesg.c
gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/ -c lib-vdf.c
#gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/  -lgmp -o main.o main.c
gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/   -c -o sha256.o sha256.c
gcc lib-misc.o lib-timing.o lib-mesg.o lib-vdf.o sha256.o -o libtest-vdf.so   -shared -lm -lgmp -lnettle -lhogweed -lpbc -ljson-c -L/opt/local/lib/ -L/usr/local/lib/
cp libtest-vdf.so ../
