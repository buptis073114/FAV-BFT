#ifndef _SHA256_H
#define _SHA256_H

//#ifndef uint8
//#define uint8  unsigned char
//#endif

//#ifndef uint32
//#define uint32 unsigned int
//#endif
#ifdef  __cplusplus
extern "C" {
#endif

#ifdef unix
#define uint8  unsigned char
#define uint32 unsigned int
#else
#define uint8  unsigned char
#define uint32 unsigned int
#endif


typedef struct
{
    uint32 total[2];
    uint32 state[8];
    uint8 buffer[64];
}
sha256_context;

void sha256_starts( sha256_context *ctx );
void sha256_update( sha256_context *ctx, uint8 *input, uint32 length );
void sha256_finish( sha256_context *ctx, uint8 digest[32] );

void sha256(uint8 digest[], uint8 *input, uint32 length);
#ifdef  __cplusplus
}
#endif
#endif /* sha256.h */

