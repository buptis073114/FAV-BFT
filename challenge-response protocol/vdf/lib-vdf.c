
#include "lib-vdf.h"

#define primes 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571,3581,3583,3593,3607,3613,3617,3623,3631,3637,3643,3659,3671,3673,3677,3691,3697,3701,3709,3719,3727,3733,3739,3761,3767,3769,3779,3793,3797,3803,3821,3823,3833,3847,3851,3853,3863,3877,3881,3889,3907,3911,3917,3919,3923,3929,3931,3943,3947,3967,3989,4001,4003,4007,4013,4019,4021,4027,4049,4051,4057,4073,4079,4091,4093,4099,4111,4127,4129,4133,4139,4153,4157,4159,4177,4201,4211,4217,4219,4229,4231,4241,4243,4253,4259,4261,4271,4273,4283,4289,4297,4327,4337,4339,4349,4357,4363,4373,4391,4397,4409,4421,4423,4441,4447,4451,4457,4463,4481,4483,4493,4507,4513,4517,4519,4523,4547,4549,4561,4567,4583,4591,4597,4603,4621,4637,4639,4643,4649,4651,4657,4663,4673,4679,4691,4703,4721,4723,4729,4733,4751,4759,4783,4787,4789,4793,4799,4801,4813,4817,4831,4861,4871,4877,4889,4903,4909,4919,4931,4933,4937,4943,4951,4957,4967,4969,4973,4987,4993,4999,5003,5009,5011,5021,5023,5039,5051,5059,5077,5081,5087,5099,5101,5107,5113,5119,5147,5153,5167,5171,5179,5189,5197,5209,5227,5231,5233,5237,5261,5273,5279,5281,5297,5303,5309,5323,5333,5347,5351,5381,5387,5393,5399,5407,5413,5417,5419,5431,5437,5441,5443,5449,5471,5477,5479,5483,5501,5503,5507,5519,5521,5527,5531,5557,5563,5569,5573,5581,5591,5623,5639,5641,5647,5651,5653,5657,5659,5669,5683,5689,5693,5701,5711,5717,5737,5741,5743,5749,5779,5783,5791,5801,5807,5813,5821,5827,5839,5843,5849,5851,5857,5861,5867,5869,5879,5881,5897,5903,5923,5927,5939,5953,5981,5987,6007,6011,6029,6037,6043,6047,6053,6067,6073,6079,6089,6091,6101,6113,6121,6131,6133,6143,6151,6163,6173,6197,6199,6203,6211,6217,6221,6229,6247,6257,6263,6269,6271,6277,6287,6299,6301,6311,6317,6323,6329,6337,6343,6353,6359,6361,6367,6373,6379,6389,6397,6421,6427,6449,6451,6469,6473,6481,6491,6521,6529,6547,6551,6553,6563,6569,6571,6577,6581,6599,6607,6619,6637,6653,6659,6661,6673,6679,6689,6691,6701,6703,6709,6719,6733,6737,6761,6763,6779,6781,6791,6793,6803,6823,6827,6829,6833,6841,6857,6863,6869,6871,6883,6899,6907,6911,6917,6947,6949,6959,6961,6967,6971,6977,6983,6991,6997,7001,7013,7019,7027,7039,7043,7057,7069,7079,7103,7109,7121,7127,7129,7151,7159,7177,7187,7193,7207,7211,7213,7219,7229,7237,7243,7247,7253,7283,7297,7307,7309,7321,7331,7333,7349,7351,7369,7393,7411,7417,7433,7451,7457,7459,7477,7481,7487,7489,7499,7507,7517,7523,7529,7537,7541,7547,7549,7559,7561,7573,7577,7583,7589,7591,7603,7607,7621,7639,7643,7649,7669,7673,7681,7687,7691,7699,7703,7717,7723,7727,7741,7753,7757,7759,7789,7793,7817,7823,7829,7841,7853,7867,7873,7877,7879,7883,7901,7907,7919

void getSecureN(pp_t pp, unsigned int n_bits,unsigned long int fixed_exp,
                gmp_randstate_t prng) {
    
    mpz_t p, q, phi, tmp1, tmp2;
    unsigned int p_bits, q_bits;
    
    //    pmesg(msg_verbose, "Genero un numero N sicuro...");
    
    assert(pp->N);
    assert(n_bits > 1);
    assert(prng);
    assert((fixed_exp == 0) || (fixed_exp % 2 == 1));
    p_bits = n_bits >> 1;
    q_bits = n_bits - p_bits;
    
    mpz_inits(tmp1, tmp2, NULL);
    
    mpz_inits(p, q, phi, NULL);
    mpz_inits(pp->N, NULL);
    
    do {
        /* p e q */
        do
            mpz_urandomb(p, prng, p_bits);
        while ((mpz_sizeinbase(p, 2) < p_bits) ||
               !mpz_probab_prime_p(p, rsa_mr_iterations));
        do
            mpz_urandomb(q, prng, q_bits);
        while ((mpz_sizeinbase(q, 2) < q_bits) ||
               !mpz_probab_prime_p(q, rsa_mr_iterations));
        mpz_sub_ui(tmp1, p, 1L);
        mpz_sub_ui(tmp2, q, 1L);
        mpz_mul(phi, tmp1, tmp2);
    } while ((fixed_exp > 0) && (mpz_gcd_ui(NULL, phi, fixed_exp) != 1L));
    mpz_mul(pp->N, p, q);

    pmesg_mpz(msg_very_verbose, "pp->N:", pp->N);
    pmesg_mpz(msg_very_verbose, "p:", p);
    pmesg_mpz(msg_very_verbose, "q:", q);

    mpz_clears(p, q, phi, tmp1, tmp2, NULL);
}

int getNBlocks(int n){
//    printf("in getNBlocks\n");
    int i;
    for(i=0;n>0;i++)
    {
//        printf("%d\n",n);
        n=n/16;
    }
//    printf("end getNBlocks\n");
    return i;
}

int getDecimalNumbers(int n){
    //    printf("in getDecimalNumbers\n");
    int i = 0;
    for(i=0;n>0;i++)
    {
        //        printf("%d\n",n);
        n=n/10;
    }
    //    printf("end getDecimalNumbers i is %d\n",i);
    return i;
}

void getBlocksFromInt(int n,uint8_t block_to_hash[]){
    int i;
    for(i=0;n>0;i++)
    {
        block_to_hash[i]= n%16;
        n=n/16;
    }
    
}
void getFactorMul(int in[],int out[],int dim){
    out[dim-1]=0;
    for(int i=dim-2;i>=0;i--){
        out[i]=out[i+1]+in[i+1];
    }

    
}

void sha256_hash_string(unsigned char hash[SHA256_DIGEST_LENGTH],unsigned char outputBuffer[65])
{
    int i = 0;
//    printf("sha256_hash_string is ");
    for(i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf(outputBuffer + (i * 2), "%02x", hash[i]);
        //printf("%x",hash[i]);
    }
//    printf("\n");
    outputBuffer[64] = 0;
}

void challenge_sha256(char* identity,char* path,mpz_t pi,char* ch,char* challenge_phase_hash){


//    printf("in challenge_sha256 path is %s\n",path);
    unsigned char hash[SHA256_DIGEST_LENGTH] = "\0";
    struct sha256_ctx sha256;
    const int bufSize = 32768;
    char* buffer = malloc(bufSize);
    if(!buffer) return;

    int bytesRead = 0;

    char* pi_str = malloc(4097);
    if(!pi_str) return;

    mpz_get_str(pi_str, 16, pi);
    FILE* file = fopen(path, "rb");
    if(!file) return;

    sha256_init(&sha256);


    sha256_update(&sha256, strlen(identity), identity);

//    printf("identity is %s \n",identity);
//    printf("pi_str is %s \n",pi_str);
//    printf("ch is %s \n",ch);

    while((bytesRead = fread(buffer, 1, bufSize, file)))
    {
        sha256_update(&sha256, bytesRead, buffer);
    }
//    sha256_update(&sha256, strlen(ch), ch );
    sha256_update(&sha256, strlen(pi_str), pi_str );
    sha256_update(&sha256, strlen(ch), ch );

    sha256_digest(&sha256, SHA256_DIGEST_LENGTH, hash);
    sha256_hash_string(hash, challenge_phase_hash);


    fclose(file);
    if(NULL!=buffer){
        free(buffer);
    }
    if(NULL!=pi_str){
        free(pi_str);
    }
}


int calc_sha256_str_str(char* str, int len, char* result)
{
//    printf("calc_sha256_str_str\n");
    //char output[65]="\0";
    unsigned char hash[SHA256_DIGEST_LENGTH] = "\n";
    struct sha256_ctx sha256;

    sha256_init(&sha256);

    sha256_update(&sha256, len, str);

    sha256_digest(&sha256, SHA256_DIGEST_LENGTH, hash);
    sha256_hash_string(hash, result);
    return 0;
}




int calc_sha256_str(char* str, int len, mpz_t sum)
{
//    printf("calc_sha256_str\n");
    char output[65]="\0";
    unsigned char hash[SHA256_DIGEST_LENGTH] = "\n";
    struct sha256_ctx sha256;

    sha256_init(&sha256);

    sha256_update(&sha256, len, str);

    sha256_digest(&sha256, SHA256_DIGEST_LENGTH, hash);
    sha256_hash_string(hash, output);


    mpz_t hashmpz;
    int flag;
    mpz_init(hashmpz);
    mpz_set_ui(hashmpz,0);//assign n = 0
    flag = mpz_set_str(hashmpz,output, 16);

    mpz_set(sum,hashmpz); //assign hashmpz value to sum

    mpz_clear(hashmpz);
    return 0;
}

int calc_sha256(char* path, unsigned char *identity, mpz_t sum)
{
//    printf("calc_sha256\n");
    char output[65]="\0";
    unsigned char hash[SHA256_DIGEST_LENGTH] = "\n";
    struct sha256_ctx sha256;
    const int bufSize = 32768;
    char* buffer = malloc(bufSize);
    int bytesRead = 0;
    FILE* file = fopen(path, "rb");
    if(!file) return -1;
    sha256_init(&sha256);
    if(!buffer) return -1;
    while((bytesRead = fread(buffer, 1, bufSize, file)))
    {
        sha256_update(&sha256, bytesRead, buffer);
    }

    sha256_update(&sha256, strlen(identity), identity);
    sha256_digest(&sha256, SHA256_DIGEST_LENGTH, hash);
    sha256_hash_string(hash, output);
    mpz_t hashmpz;
    int flag;
    mpz_init(hashmpz);
    mpz_set_ui(hashmpz,0);//assign n = 0
    flag = mpz_set_str(hashmpz,output, 16);
    mpz_set(sum,hashmpz); //assign hashmpz value to sum
    char* getstr = malloc(65);
    if(!getstr) return -1;
    mpz_get_str(getstr, 16, hashmpz);
    //    printf("getstr %s\n",getstr);
    mpz_clear(hashmpz);
    fclose(file);
    if(NULL!=buffer){
        free(buffer);
    }
    if(NULL!=getstr){
        free(getstr);
    }
    return 0;
}



//function to convert ascii char[] to hex-string (char[])
void string2hexString(char* input, char* output, int len)
{
    int loop;
    int i;

    i=0;
    loop=0;

    while(loop<len)
    {
        sprintf((char*)(output+i),"%02X", input[loop]);
        loop+=1;
        i+=2;
    }
    //insert NULL at the end of the output string
    output[i++] = '\0';
}


void getDigestSHA1(int x,mpz_t sum){

//    printf("getDigestSHA1\n");
    struct sha1_ctx context;
    uint8_t digest[SHA1_DIGEST_SIZE];
    char buffer[2048];
    sha1_init(&context);
    int block=getNBlocks(x);

//    printf("block:%d\n",block);

    uint8_t block_to_hash[block];
    getBlocksFromInt(x,block_to_hash);
    sha1_update(&context, block, block_to_hash);
    sha1_digest(&context, SHA1_DIGEST_SIZE, digest);


    int digits[SHA1_DIGEST_SIZE] ={0};
    for(int i=0;i<SHA1_DIGEST_SIZE;i++){
        digits[i]=getDecimalNumbers(digest[i]); //
    }
    int aa[SHA1_DIGEST_SIZE] ={0};
    getFactorMul(digits,aa,SHA1_DIGEST_SIZE);
    mpz_t tmp,factMul;
    mpz_inits(tmp,factMul,NULL);
    for (int i = SHA1_DIGEST_SIZE-1; i >=0 ; i--) {
        mpz_ui_pow_ui(factMul, 10, aa[i]); //calculate the value factMul = 10^(aa[i])
        mpz_mul_ui(tmp, factMul, digest[i]); // Set tmp = factMul * digest[i].
        mpz_add(sum, sum, tmp);
    }
    
    pmesg_mpz(msg_very_verbose, "HASH COME INTERO:", sum);
    
    snprintf(buffer, sizeof(buffer), "input (%d bit)", block * 8);
    pmesg_hex(msg_verbose, buffer, block, block_to_hash);

    snprintf(buffer, sizeof(buffer), "digest (%d bit)", SHA1_DIGEST_SIZE * 8);
    pmesg_hex(msg_verbose, buffer, SHA1_DIGEST_SIZE, digest);

}



void setup(pp_t pp,unsigned int n_bits,gmp_randstate_t prng, int hash,unsigned long t){
    getSecureN(pp,n_bits,0,prng);
    pp->hash_f=hash;
    pp->T=t;
}

void printPublicParameters(pp_t pp){
    pmesg_mpz(msg_very_verbose, "Gruppo G:", pp->N);
    printf("Hash:SHA-%d\n",pp->hash_f);
    printf("T:%lu\n",pp->T);
}

void initialization_phase_impl(char* path ,
                          pp_t pp,output_eval_t output_eval,
                          mpz_t pi,mpz_t nextprime_l,char * identity){

    unsigned long iter = 1;
    mpz_t tmp;
    mpz_inits(tmp, NULL);//Large value tmp should be initialized before use to dynamically allocate space
    mpz_t tmp1;
    mpz_inits(tmp1, NULL);//Large value tmp should be initialized before use to dynamically allocate space
    //x->x^2->x^(2^(2))->x^(2^(3))->x^(2^(4))...->x^(2^(T))
    mpz_t exp;
    mpz_inits(exp, NULL);//Large value tmp should be initialized before use to dynamically allocate space
    mpz_set_ui(exp,2);//assign exp value to 2

    calc_sha256(path, identity, output_eval->g);

    mpz_set(tmp,output_eval->g);
//    printf("pp->T is %d\n",pp->T);

    for(iter=0;iter<pp->T;iter++){
        mpz_powm(tmp1, tmp, exp, pp->N); //calculate the value of (tmp)^2 mod (pp->N)
        mpz_set(tmp,tmp1); //assign tmp1 value to tmp
    }
//    pmesg_mpz(msg_very_verbose, "tmp:", tmp);
    mpz_set(output_eval->h,tmp);

    mpz_t add_result;
    mpz_inits(add_result, NULL);
//    pmesg_mpz(msg_very_verbose, "output_eval->g:", output_eval->g);
//    pmesg_mpz(msg_very_verbose, "output_eval->h:", output_eval->h);

    char* xxxxxx = malloc(4097);
    mpz_get_str(xxxxxx, 16, output_eval->g);
//    printf("xxxxxx is %s\n",xxxxxx);

    char* yyyyyyy = malloc(4097);
    mpz_get_str(yyyyyyy, 16, output_eval->h);
//    printf("yyyyyyy is %s\n",yyyyyyy);
    mpz_sub(add_result,output_eval->g,output_eval->h);

    char* add_result_str = malloc(4097);
    add_result_str = mpz_get_str(NULL, 16, add_result);
//    printf("add_result_str %s\n",add_result_str);
    mpz_t hmac_prime;
    mpz_inits(hmac_prime, NULL);
    calc_sha256_str(add_result_str,strlen(add_result_str), hmac_prime);

    mpz_nextprime(nextprime_l,hmac_prime);//Set nextprime to the next prime greater than op.

    mpz_t exp22;//mpz_t is the large number type for GMP
    mpz_inits(exp22, NULL); //Large value exps should be initialized before use to dynamically allocate space
    mpz_ui_pow_ui(exp22,2,pp->T); //2^t
    mpz_t exp3333;
    mpz_inits(exp3333, NULL); //Large value exps should be initialized before use to dynamically allocate space
//    pmesg_mpz(msg_very_verbose, "exp22:", exp22);
//    pmesg_mpz(msg_very_verbose, "nextprime_l:", nextprime_l);
    //There are three modes of integer division in GMP: ceil, floor and truncate, which correspond to cidv, fdiv and tdiv respectively
    //Where n is the divisor, D is the divisor, q is the quotient, and R is the remainder. Q only calculates quotient, r only calculates remainder, QR calculates quotient and remainder at the same time. In QR function, Q and R cannot use the same variable, otherwise the behavior is uncertain.
    mpz_fdiv_q(exp3333,exp22,nextprime_l);//floor exp22/l
//    pmesg_mpz(msg_very_verbose, "exp3333:", exp3333);
    mpz_powm(pi, output_eval->g, exp3333 , pp->N); //pi = x^exp3333 mod N
//    pmesg_mpz(msg_very_verbose, "pi:", pi);

    if(NULL!=add_result_str){
        free(add_result_str);
    }
    mpz_clear(tmp);
    mpz_clear(tmp1);
    mpz_clear(exp);
    mpz_clear(add_result);
    mpz_clear(exp22);
    mpz_clear(exp3333);
    mpz_clear(hmac_prime);

}



//challenge phase
void challenge_phase_impl(char * identity,pp_t pp,output_eval_t output_eval,mpz_t pi,mpz_t nextprime_l,char* path ,char * ch){

    //hash(identity+f+pi+ch)
    char * challenge_phase_hash = malloc(65);
    challenge_sha256(identity,path,pi,ch,challenge_phase_hash);
//    printf("challenge_phase_hash is %s\n",challenge_phase_hash);
    if(NULL!=challenge_phase_hash){
        free(challenge_phase_hash);
    }

}



//challenge phase
void verification_phase_impl(char* path ,char * identity,pp_t pp,mpz_t pi,mpz_t nextprime_l,output_eval_t output_eval,char * ch){

    mpz_t x;
    mpz_inits(x, NULL);



    calc_sha256(path,identity, x);
    mpz_t r;//mpz_t is the large number type for GMP
    mpz_inits(r, NULL); //Large value exps should be initialized before use to dynamically allocate space

    mpz_t expvvvv;
    mpz_inits(expvvvv, NULL);//Large value expvvvv should be initialized before use to dynamically allocate space
    mpz_set_ui(expvvvv,2);//assign expvvvv value to 2

//    printf("before mpz_powm\n");

    mpz_t exp22;//mpz_t is the large number type for GMP
    mpz_inits(exp22, NULL); //Large value exps should be initialized before use to dynamically allocate space

    mpz_ui_pow_ui(exp22,2,pp->T); //2^t
    mpz_mod(r, exp22, nextprime_l);

    pmesg_mpz(msg_very_verbose, "r:", r);

    //pi^l
    mpz_t piexpi;
    mpz_inits(piexpi, NULL);
    mpz_powm(piexpi,pi,nextprime_l,pp->N);


    pmesg_mpz(msg_very_verbose, "piexpi:", piexpi);


    //x^r
    mpz_t xexpr;
    mpz_inits(xexpr, NULL);
    mpz_powm(xexpr,x,r,pp->N);
    pmesg_mpz(msg_very_verbose, "xexpr:", xexpr);


    mpz_t mulresult;
    mpz_inits(mulresult, NULL);
    mpz_mul(mulresult,piexpi,xexpr);
    pmesg_mpz(msg_very_verbose, "mulresult:", mulresult);

    mpz_t verifyy;
    mpz_inits(verifyy, NULL);

    mpz_mod(verifyy,mulresult,pp->N);
    pmesg_mpz(msg_very_verbose, "verifyy:", verifyy);

    int result = mpz_cmp(output_eval->h,verifyy);
//    printf("result is %d\n",result);

    mpz_clear(expvvvv);
    mpz_clear(verifyy);
    mpz_clear(mulresult);
    mpz_clear(xexpr);
    mpz_clear(piexpi);

}


int get_random_prime(){
    int primes_vector[]= {primes};
    long int seed = 0;
    extract_randseed_os_rng((uint8_t *)&seed, 20);
    srand(seed);
    int x=primes_vector[rand()%1000];
    return x;
}

void generateProof(output_eval_t output_eval){

    mpz_t addoutcome;
    mpz_inits(addoutcome, NULL);
    mpz_add(addoutcome,output_eval->g,output_eval->h);//Assign the result of the large number g + h to addoutcome, that is, addoutcome = g + h

    //    getDigestSHA1(x,output_eval->g);

    //    mpz_t nextprime;
    //    mpz_nextprime(nextprime,op);//Set nextprime to the next prime greater than op.
    mpz_clear(addoutcome);
}


void getRandom_mpzl(proof_metadata_t proof_metadata){
    //check g,h \in G  TODO
    mpz_inits(proof_metadata->l,NULL);

    mpz_set_ui(proof_metadata->l, get_random_prime());
}





char * init_phase(char* path,char* evidencefilepath, unsigned long  TTTT){
//    char* path ="/home/ss/article/PythonCallC/file.txt";
    //printf("Version: %s\n", json_c_version());
    //printf("Version Number: %d\n", json_c_version_num());
//    printf("begin initialization_phase\n");
//    printf("path: %s\n", path);
//    printf("evidencefilepath: %s\n", evidencefilepath);
    json_object *root = json_object_new_object();
    pp_t pp;
    output_eval_t output_eval;
    gmp_randstate_t prng;
    mpz_t nextprime_l;
    mpz_inits(nextprime_l, NULL);
    mpz_t pi;//mpz_t is the large number type for GMP
    mpz_inits(pi, NULL); //Large value exps should be initialized before use to dynamically allocate space

//    char *identity = malloc(65);
    unsigned char *identity = malloc(65);
    gmp_randinit_default(prng);//Initialize state using default algorithm
    gmp_randseed_os_rng(prng, prng_sec_level);
    mpz_inits(output_eval->g, NULL); //Large value output_eval->g should be initialized before use to dynamically allocate space
    mpz_inits(output_eval->h, NULL); //Large value output_eval->h should be initialized before use to dynamically allocate space
    setup(pp,default_mod_bits,prng,HASH_FUNCTION,TTTT);//generate the public key


    char* big_prime = malloc(2049);
    if(!big_prime) return "";
    mpz_get_str(big_prime, 16, pp->N);

    calc_sha256_str_str(big_prime,strlen(big_prime),identity);
//    printf("identity %s\n",identity);

    initialization_phase_impl(path, pp, output_eval,pi,nextprime_l,identity);  //calculate the value of hash(x)^(2^t) mod N


    char * Nstr = malloc(4096);
    mpz_get_str(Nstr,16,pp->N);
//    printf("Nstr is %s \n",Nstr);

    json_object_object_add(root, "N", json_object_new_string(Nstr));
    json_object_object_add(root, "T", json_object_new_int(TTTT));

    char * pistr = malloc(4096);
    mpz_get_str(pistr,16,pi);
//    printf("pistr is %s \n",pistr);

    json_object_object_add(root, "pi", json_object_new_string(pistr));

    char * nextprime_lstr = malloc(4096);
    mpz_get_str(nextprime_lstr,16,nextprime_l);
//    printf("nextprime_lstr is %s \n",nextprime_lstr);

    json_object_object_add(root, "nextprime_l", json_object_new_string(nextprime_lstr));
    json_object_object_add(root, "identity", json_object_new_string(identity));

    char * jsonstr = json_object_to_json_string_ext(root, JSON_C_TO_STRING_PRETTY);

//    printf("evidencefilepath: %s\n", evidencefilepath);
    if (json_object_to_file(evidencefilepath, root))
      printf("Error: failed to save %s!!\n", evidencefilepath);
    else
      printf("%s saved.\n", evidencefilepath);

    if(NULL!=big_prime){
        free(big_prime);
    }


    return jsonstr;
}


char * challenge_phase(char* filepath,char* evidencefilepath, char* ch){

    mpz_t piexpi;
    mpz_inits(piexpi, NULL);

    printf("in challenge_phase, challenge string is %s \n",ch);

    json_object *getroot;
//    getroot = json_tokener_parse(jsonstr);
    getroot = json_object_from_file(evidencefilepath);
    json_object *getNStr = json_object_object_get(getroot, "N");
    char* getNstrout = json_object_get_string(getNStr);
//    printf("getNstrout is %s \n",getNstrout);

    json_object *getpiStr = json_object_object_get(getroot, "pi");
    char* getpistrout = json_object_get_string(getpiStr);
//    printf("getpistrout is %s \n",getpistrout);

    json_object *getnextprime_lstrStr = json_object_object_get(getroot, "nextprime_l");
    char* getnextprime_lstrstrout = json_object_get_string(getnextprime_lstrStr);
//    printf("getnextprime_lstrstrout is %s \n",getnextprime_lstrstrout);

    json_object *getidentitystrStr = json_object_object_get(getroot, "identity");
    char* getidentitystrstrout = json_object_get_string(getidentitystrStr);
//    printf("getidentitystrstrout is %s \n",getidentitystrstrout);

    mpz_set_str(piexpi,getpistrout,16);

    char * challenge_phase_hash = malloc(65);

    challenge_sha256(getidentitystrstrout,filepath,piexpi,ch,challenge_phase_hash);
//    printf("challenge_phase_hash is %s\n",challenge_phase_hash);

    json_object_object_add(getroot, "challenge", json_object_new_string(ch));
    json_object_object_add(getroot, "challenge_response", json_object_new_string(challenge_phase_hash));


    char * jsonstr = json_object_to_json_string_ext(getroot, JSON_C_TO_STRING_PRETTY);
    mpz_clear(piexpi);
    return jsonstr;
}

char* verification_phase(char* filepath,char* evidencefilepath,char * response){
//char* verification_phase(char* filepath,char* evidencefilepath){

//    printf("in verification_phase \n");

    json_object *root;
    root = json_tokener_parse(response);
//    root = json_object_from_file(evidencefilepath);

    json_object *getNStr = json_object_object_get(root, "N");
    char* getNstrout = json_object_get_string(getNStr);
//    printf("getNstrout is %s \n",getNstrout);


    json_object *getTStr = json_object_object_get(root, "T");
    unsigned int getTstrout = json_object_get_int(getTStr);
//    printf("getTstrout is %d \n",getTstrout);

    json_object *getpiStr = json_object_object_get(root, "pi");
    char* getpistrout = json_object_get_string(getpiStr);
//    printf("getpistrout is %s \n",getpistrout);

    json_object *getnextprime_lstrStr = json_object_object_get(root, "nextprime_l");
    char* getnextprime_lstrstrout = json_object_get_string(getnextprime_lstrStr);
//    printf("getnextprime_lstrstrout is %s \n",getnextprime_lstrstrout);

    json_object *getidentitystrStr = json_object_object_get(root, "identity");
    char* getidentitystrstrout = json_object_get_string(getidentitystrStr);
//    printf("getidentitystrstrout is %s \n",getidentitystrstrout);

    json_object *challengeStr = json_object_object_get(root, "challenge");
    char* challengestrout = json_object_get_string(challengeStr);
//    printf("challengestrout is %s \n",challengestrout);

    json_object *challenge_responseStr = json_object_object_get(root, "challenge_response");
    char* challenge_responsestrout = json_object_get_string(challenge_responseStr);
//    printf("challenge_responsestrout is %s \n",challenge_responsestrout);



    mpz_t gggg;
    mpz_inits(gggg, NULL);
//    unsigned char *identity = "id+time";
    calc_sha256(filepath,getidentitystrstrout, gggg);


    mpz_t getN;
    mpz_inits(getN, NULL);
    mpz_set_str(getN,getNstrout,16);

//    mpz_t getT;
//    mpz_inits(getT, NULL);
//    mpz_set_str(getT,TTTT,16);

    mpz_t getl;
    mpz_inits(getl, NULL);
    mpz_set_str(getl,getnextprime_lstrstrout,16);


    mpz_t getpi;
    mpz_inits(getpi, NULL);
    mpz_set_str(getpi,getpistrout,16);

    mpz_t exp22;//mpz_t is the large number type for GMP
    mpz_inits(exp22, NULL); //Large value exps should be initialized before use to dynamically allocate space
    mpz_t value;
    mpz_inits(value, NULL);
    mpz_set_ui(value,2);
    mpz_powm_ui(exp22,value,getTstrout,getl); //2^t
    //pi^l
    mpz_t piexpi;
    mpz_inits(piexpi, NULL);
    mpz_powm(piexpi,getpi,getl,getN);

    //x^r
    mpz_t xexpr;
    mpz_inits(xexpr, NULL);
    mpz_powm(xexpr,gggg,exp22,getN);
//    pmesg_mpz(msg_very_verbose, "xexpr:", xexpr);
    mpz_t mulresult;
    mpz_inits(mulresult, NULL);
    mpz_mul(mulresult,piexpi,xexpr);
    mpz_t verifyy;
    mpz_inits(verifyy, NULL);

    mpz_mod(verifyy,mulresult,getN);

    char* yyyyyyy = malloc(4097);
    mpz_get_str(yyyyyyy, 16, verifyy);
//    printf("verifyy is %s\n",yyyyyyy);

    mpz_t add_result;
    mpz_inits(add_result, NULL);
//    pmesg_mpz(msg_very_verbose, "output_eval->g:", output_eval->g);
//    pmesg_mpz(msg_very_verbose, "output_eval->h:", output_eval->h);

    mpz_sub(add_result,gggg,verifyy);

    char* add_result_str = malloc(4097);
    add_result_str = mpz_get_str(NULL, 16, add_result);
//    printf("add_result_str %s\n",add_result_str);
    mpz_t hmac_prime;
    mpz_inits(hmac_prime, NULL);
    calc_sha256_str(add_result_str,strlen(add_result_str), hmac_prime);

    mpz_t nextprime_l;
    mpz_inits(nextprime_l, NULL);
    mpz_nextprime(nextprime_l,hmac_prime);//Set nextprime to the next prime greater than op.

    mpz_t verifyl;
    mpz_inits(verifyl, NULL);
    mpz_set_str(verifyl,getnextprime_lstrstrout,16);

    int result = mpz_cmp(nextprime_l,verifyl);


    char * sigma = malloc(65);
    challenge_sha256(getidentitystrstrout,filepath,getpi,challengestrout,sigma);


    int result1 = strcmp(challenge_responsestrout, sigma);
//    printf("result1 is %d\n",result1);

    mpz_clear(gggg);
    mpz_clear(getN);
    mpz_clear(getl);
    mpz_clear(getpi);
    mpz_clear(exp22);
    mpz_clear(value);
    mpz_clear(piexpi);
    mpz_clear(xexpr);
    mpz_clear(mulresult);
    mpz_clear(verifyy);
    mpz_clear(add_result);
    mpz_clear(hmac_prime);
    mpz_clear(nextprime_l);
    mpz_clear(verifyl);


    json_object *retroot = json_object_new_object();
    json_object_object_add(retroot, "verification_result", json_object_new_int(result^result1));

    char * jsonstr = json_object_to_json_string_ext(retroot, JSON_C_TO_STRING_PRETTY);
    return jsonstr;
}

