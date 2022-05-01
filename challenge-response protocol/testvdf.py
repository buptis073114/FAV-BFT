#import ctypes
from ctypes import cdll
import ctypes
import datetime
import time

if __name__ == "__main__":
    # Load the shared library into ctypes
    path = "/challenge-response protocol/data/1Gfile"
    evidencefilepath = "evidencefile.txt"
    lib = cdll.LoadLibrary('./libtest-vdf.so')
    T1 = time.time()
    pathencode = path.encode()
    evidencefilepathencode = evidencefilepath.encode()

    # 500, 5000, 10000, 50000, 100000, 300000, 500000, 1000000
    tau = 1000000
    ret1 = lib.init_phase(pathencode, evidencefilepathencode, tau)
    data = ctypes.string_at(ret1, -1).decode("utf-8")
    # print("init phase output ",data)

    T2 = time.time()
    print('init_phase running time:%sms' % ((T2 - T1) * 1000))


    T1 = time.time()
    challenge = "12345678901234567890123456789012"
    challengeencode = challenge.encode()
    ret2 = lib.challenge_phase(pathencode, evidencefilepathencode, challengeencode)
    challenge_data = ctypes.string_at(ret2, -1).decode("utf-8")
    # print("challenge phase output ", challenge_data)
    T2 = time.time()
    print('challenge_phase running time:%sms' % ((T2 - T1) * 1000))


    challenge_dataencode = challenge_data.encode()

    T1 = time.time()
    ret3 = lib.verification_phase(pathencode, evidencefilepathencode, challenge_dataencode)
    verification_data = ctypes.string_at(ret3, -1).decode("utf-8")
    # print("verification phase output ", verification_data)
    T2 = time.time()
    print('verification_phase running time:%sms' % ((T2 - T1) * 1000))