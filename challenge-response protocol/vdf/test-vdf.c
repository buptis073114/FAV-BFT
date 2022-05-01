#include "lib-vdf.h"
#include "lib-mesg.h"
#include "lib-timing.h"
#include <gmp.h>
#include <libgen.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <string.h>
#define T 100

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
//            printf("\nout[%d] = %lx \n" , targetIndex ,out[targetIndex] );
            targetIndex++;
        }
    }
}
int main() {
    test(T);
}
