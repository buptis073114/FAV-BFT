# FAV-BFT
FAV-BFT:An Efficient File Authenticity Verification Protocol for Blockchain-based File-Sharing System

Compared with traditional file-sharing system, the blockchain-based file-sharing system shows its superiority, such as electronic money incentive mechanism, decentralization, information tamper resistance and so on.
Benefiting from those properties,  it has attracted tons of users to participate in blockchain-based file-sharing and eventually forms an indestructible electronic library.  However, with such a huge amount of files, the problem of file authenticity verification is still not resolved.
This paper attempts to address the challenge of file authenticity verification for blockchain-based file-sharing system, specifically, verifying that the file is really stored by the claimer and needed by the file-downloader before the file is downloaded.
We propose an efficient file authenticity verification protocol, named File Authenticity Verification Byzantine Fault Tolerant(FAV-BFT).
We first apply Verifiable Delay Function to bind the shared file, and then reconstruct it to a challenge-response interactive protocol for file-sharing, and finally embedded with  Byzantine Fault  Tolerant protocol.
Due to the construction, with  2/3 of participants are honest,  FAV-BFT can correctly prove how long a file has been stored and whether a file meets the requirement of the file downloader.
Moreover, since all the file content is processed by hash function before transformation, FAV-BFT protects the shared-file from content disclosure during the verification process without trusted third parties.
Theoretical analysis and experiments are conducted and show that FAV-BFT not only has more efficient in verification phases compared with Filecoin, but also supports the authenticity verification of shared-file.

This experiment refers to HoneyBadgerBFT(https://github.com/initc3/HoneyBadgerBFT-Python) and VDF(https://github.com/Cris94x/vdf-c_implementation)

1. install gmp
```bash
$ sudo apt install libgmp3-dev
$ sudo ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/gmp.h
```

2. install essential software
```bash
$ sudo apt install build-essential
```
3. install flex and bison
```bash
$ sudo apt-get install flex bison
```
4. install pbc 
download pbc-0.5.14 from https://crypto.stanford.edu/pbc/download.html
```bash
$ ./configure
$ make
$ sudo make install
```
5. install nettle-dev
Download https://www.linuxfromscratch.org/blfs/view/8.4/postlfs/nettle.html package
```bash
./configure --prefix=/usr --disable-static &&
make
sudo make install
sudo ln -s /usr/include/nettle /usr/local/include/nettle
```

6. install python3-setuptools:
```bash
sudo apt-get install python3-setuptools
```


7. install openssl
```bash
sudo apt-get install libssl-dev
```

8. install pbc
```bash
wget https://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz --no-check-certificate
tar -xvf pbc-0.5.14.tar.gz
cd pbc-0.5.14 && ./configure && make && make install
```
9. compile a challenge-response protocol based on VDF

```bash
cd challenge-response protocol/vdf
./compile.sh
```
generate libtest-vdf.so

10. test vdf

```bash
python3 testvdf.py
```

![picture](https://github.com/buptis073114/FAV-BFT/tree/master/picture/testvdf.png)


11. test vdf_multi

```bash
python3 testvdf_multi.py
```
![picture2](https://github.com/buptis073114/FAV-BFT/tree/master/picture/test_vdf_multi.png)


12. test rbc

```bash
python3 ./test/testrbc.py

```

![picture2](https://github.com/buptis073114/FAV-BFT/tree/master/picture/test_rbc.png)