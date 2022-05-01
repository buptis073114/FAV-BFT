#!/bin/sh

gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/ -c ./vdf_c/lib-misc.c -o ./vdf_c/lib-misc.o
gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/ -c ./vdf_c/lib-timing.c -o ./vdf_c/lib-timing.o
gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/ -c ./vdf_c/lib-mesg.c -o ./vdf_c/lib-mesg.o
gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/ -c ./vdf_c/lib-vdf.c -o ./vdf_c/lib-vdf.o
gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/   -c -o ./vdf_c/test-vdf.o ./vdf_c/test-vdf.c
gcc -DPBC_SUPPORT -std=gnu11 -Wall   -fPIC  -DUSE_RDTSCP -g -DPBC_DEBUG -Og    -I/opt/local/include/ -I/usr/local/include/ -I/usr/include/   -c -o ./vdf_c/sha256.o ./vdf_c/sha256.c
gcc ./vdf_c/lib-misc.o ./vdf_c/lib-timing.o ./vdf_c/lib-mesg.o ./vdf_c/lib-vdf.o ./vdf_c/test-vdf.o ./vdf_c/sha256.o -o ./vdf_c/libtest-vdf.so   -shared -lm -lgmp -lnettle -lhogweed -lpbc  -L/opt/local/lib/ -L/usr/local/lib/
cp ./vdf_c/libtest-vdf.so ./
