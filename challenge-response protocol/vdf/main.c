
#include <gmp.h>
#include <libgen.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <string.h>

#include "lib-vdf.h"
#include "lib-mesg.h"
#include "lib-timing.h"



#ifndef __TEST_H__
#define __TEST_H__
int test(unsigned long  TTTT);
#endif

void make_data_package(char buff[] , long out[])
{
    char tempBuffer[8] = {0};
    char *end ;
    for (int i=0 , targetIndex =0, tIndex =0; i<256; i++ , tIndex++ )
    {
        if( tIndex >=8 )
            tIndex = 0;
        tempBuffer[tIndex] = buff[i];
        //        printf("%c  " ,  tempBuffer[tIndex]);
        if ( (i+1) % 8 ==0) {
            //            printf("\n");
            out[targetIndex] =strtol(tempBuffer, &end, 2);
            printf("\nout[%d] = %lx \n" , targetIndex ,out[targetIndex] );
            targetIndex++;
        }
    }
}
int main() {

    unsigned long T = 100;
    verification(T);
}
