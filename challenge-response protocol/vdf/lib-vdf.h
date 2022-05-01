#ifndef LIB_VDF_H
#define LIB_VDF_H
#include "lib-mesg.h"
#include <assert.h>
#include <gmp.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include "lib-timing.h"
#include <libgen.h>
#include <nettle/md5.h>
#include <nettle/sha1.h>
#include <nettle/sha2.h>
#include <nettle/sha3.h>
#include <json-c/json.h>
#define rsa_mr_iterations 12
#define  SHA256_DIGEST_LENGTH 32


#ifdef unix
#define uint8  unsigned char
#define uint32 unsigned int
#else
#define uint8  unsigned char
#define uint32 unsigned int
#endif



#define prng_sec_level 128
#define default_mod_bits 4096

#define sampling_time 5 /* secondi */
#define max_samples (sampling_time * 200)

#define HASH_FUNCTION 2
//1000000



typedef struct
{
    uint32 total[2];
    uint32 state[8];
    uint8 buffer[64];
}
sha256_context;



struct pp_struct {
    mpz_t N;
    unsigned long  T;
    int hash_f; //1,2,3
};
typedef struct pp_struct *pp_ptr;
typedef struct pp_struct pp_t[1];

struct output_eval_struct {
    mpz_t g; //H(x)
    mpz_t h; //output
    mpz_t proof;
};

typedef struct output_eval_struct *output_eval_ptr;
typedef struct output_eval_struct output_eval_t[1];

struct proof_metadata_struct {
    mpz_t l; //a prime number
    mpz_t q;
    mpz_t r_prover;
    mpz_t r_verifier;
    mpz_t _tmp;//2^t
};

typedef struct proof_metadata_struct *proof_metadata_ptr;
typedef struct proof_metadata_struct proof_metadata_t[1];

void setup(pp_t ,unsigned int ,gmp_randstate_t,int,unsigned long );
void generateProof(output_eval_t output_eval);
void printPublicParameters(pp_t);
void initialization_phase(char* path ,int, pp_t ,output_eval_t,mpz_t pi,mpz_t nextprime_l,char * identity );
void challenge_phase_impl(char * identity,pp_t pp,output_eval_t init,mpz_t pi,mpz_t nextprime_l,char* path ,char * ch);
void verification_phase_impl(char* path ,char * identity,pp_t pp,mpz_t pi,mpz_t nextprime_l,output_eval_t output_eval,char * ch);


void sha256_hash_string (unsigned char hash[SHA256_DIGEST_LENGTH],unsigned char outputBuffer[65]);
int calc_sha256_str_str(char* str, int len, char* result);
int calc_sha256_str(char* str, int len, mpz_t sum);
void challenge_sha256(char* identity,char* path,mpz_t pi,char* ch,char* challenge_phase_hash);

int calc_sha256(char* path, unsigned char* identity, mpz_t sum);

#ifndef __TEST_H__
#define __TEST_H__
int verification(unsigned long  TTTT);
#endif




#endif

