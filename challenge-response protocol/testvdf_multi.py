#import ctypes
from ctypes import cdll
import ctypes
import datetime
import time

if __name__ == "__main__":
    # Load the shared library into ctypes
    lib = cdll.LoadLibrary('./libtest-vdf.so')

    for xxxxxx in range(10):
        path = "./challenge-response protocol/data/1Mfile"
        evidencefilepath = "evidencefile.txt"
        for tau in [500, 5000, 10000, 50000, 100000, 300000, 500000, 1000000]:
            for x in range(10):
                fo = open("./challenge-response protocol/1Mfileoutcome.txt", "a+")
                fo.write("1M,")
                fo.write(str(tau))
                fo.write(',')
                T1 = time.time()
                pathencode = path.encode()
                evidencefilepathencode = evidencefilepath.encode()

                ret1 = lib.init_phase(pathencode,evidencefilepathencode,tau)
                data = ctypes.string_at(ret1, -1).decode("utf-8")
                # print("init phase output ",data)

                T2 = time.time()
                # print('init_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')

                T1 = time.time()
                challenge = "12345678901234567890123456789012"
                challengeencode = challenge.encode()
                ret2 = lib.challenge_phase(pathencode,evidencefilepathencode, challengeencode)
                challenge_data = ctypes.string_at(ret2, -1).decode("utf-8")
                # print("challenge phase output ", challenge_data)
                T2 = time.time()
                # print('challenge_phase running time:%sms' % ((T2 - T1) * 1000))

                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                challenge_dataencode = challenge_data.encode()

                T1 = time.time()
                ret3 = lib.verification_phase(pathencode,evidencefilepathencode,challenge_dataencode)
                verification_data = ctypes.string_at(ret3, -1).decode("utf-8")
                # print("verification phase output ", verification_data)
                T2 = time.time()
                # print('verification_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                fo.write('\n')
                fo.close()

        path = "./challenge-response protocol/data/5Mfile"
        evidencefilepath = "evidencefile.txt"
        for tau in [500, 5000, 10000, 50000, 100000, 300000, 500000, 1000000]:

            for x in range(10):
                fo = open("./challenge-response protocol/5Mfileoutcome.txt", "a+")
                fo.write("5M,")
                fo.write(str(tau))
                fo.write(',')
                T1 = time.time()
                pathencode = path.encode()
                evidencefilepathencode = evidencefilepath.encode()

                ret1 = lib.init_phase(pathencode, evidencefilepathencode, tau)
                data = ctypes.string_at(ret1, -1).decode("utf-8")
                # print("init phase output ",data)

                T2 = time.time()
                # print('init_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')

                T1 = time.time()
                challenge = "12345678901234567890123456789012"
                challengeencode = challenge.encode()
                ret2 = lib.challenge_phase(pathencode, evidencefilepathencode, challengeencode)
                challenge_data = ctypes.string_at(ret2, -1).decode("utf-8")
                # print("challenge phase output ", challenge_data)
                T2 = time.time()
                # print('challenge_phase running time:%sms' % ((T2 - T1) * 1000))

                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                challenge_dataencode = challenge_data.encode()

                T1 = time.time()
                ret3 = lib.verification_phase(pathencode, evidencefilepathencode, challenge_dataencode)
                verification_data = ctypes.string_at(ret3, -1).decode("utf-8")
                # print("verification phase output ", verification_data)
                T2 = time.time()
                # print('verification_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                fo.write('\n')
                fo.close()
        path = "./challenge-response protocol/data/50Mfile"
        evidencefilepath = "evidencefile.txt"
        for tau in [500, 5000, 10000, 50000, 100000, 300000, 500000, 1000000]:

            for x in range(10):
                fo = open("./challenge-response protocol/50Mfileoutcome.txt", "a+")
                fo.write("50M,")
                fo.write(str(tau))
                fo.write(',')
                T1 = time.time()
                pathencode = path.encode()
                evidencefilepathencode = evidencefilepath.encode()

                ret1 = lib.init_phase(pathencode, evidencefilepathencode, tau)
                data = ctypes.string_at(ret1, -1).decode("utf-8")
                # print("init phase output ",data)

                T2 = time.time()
                # print('init_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')

                T1 = time.time()
                challenge = "12345678901234567890123456789012"
                challengeencode = challenge.encode()
                ret2 = lib.challenge_phase(pathencode, evidencefilepathencode, challengeencode)
                challenge_data = ctypes.string_at(ret2, -1).decode("utf-8")
                # print("challenge phase output ", challenge_data)
                T2 = time.time()
                # print('challenge_phase running time:%sms' % ((T2 - T1) * 1000))

                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                challenge_dataencode = challenge_data.encode()

                T1 = time.time()
                ret3 = lib.verification_phase(pathencode, evidencefilepathencode, challenge_dataencode)
                verification_data = ctypes.string_at(ret3, -1).decode("utf-8")
                # print("verification phase output ", verification_data)
                T2 = time.time()
                # print('verification_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                fo.write('\n')
                fo.close()
        path = "./challenge-response protocol/data/100Mfile"
        evidencefilepath = "evidencefile.txt"
        for tau in [500, 5000, 10000, 50000, 100000, 300000, 500000, 1000000]:

            for x in range(10):
                fo = open("./challenge-response protocol/100Mfileoutcome.txt", "a+")
                fo.write("100M,")
                fo.write(str(tau))
                fo.write(',')
                T1 = time.time()
                pathencode = path.encode()
                evidencefilepathencode = evidencefilepath.encode()

                ret1 = lib.init_phase(pathencode, evidencefilepathencode, tau)
                data = ctypes.string_at(ret1, -1).decode("utf-8")
                # print("init phase output ",data)

                T2 = time.time()
                # print('init_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')

                T1 = time.time()
                challenge = "12345678901234567890123456789012"
                challengeencode = challenge.encode()
                ret2 = lib.challenge_phase(pathencode, evidencefilepathencode, challengeencode)
                challenge_data = ctypes.string_at(ret2, -1).decode("utf-8")
                # print("challenge phase output ", challenge_data)
                T2 = time.time()
                # print('challenge_phase running time:%sms' % ((T2 - T1) * 1000))

                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                challenge_dataencode = challenge_data.encode()

                T1 = time.time()
                ret3 = lib.verification_phase(pathencode, evidencefilepathencode, challenge_dataencode)
                verification_data = ctypes.string_at(ret3, -1).decode("utf-8")
                # print("verification phase output ", verification_data)
                T2 = time.time()
                # print('verification_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                fo.write('\n')
                fo.close()
        path = "./challenge-response protocol/data/500Mfile"
        evidencefilepath = "evidencefile.txt"
        for tau in [500, 5000, 10000, 50000, 100000, 300000, 500000, 1000000]:

            for x in range(10):
                fo = open("./challenge-response protocol/500Mfileoutcome.txt", "a+")
                fo.write("500M,")
                fo.write(str(tau))
                fo.write(',')
                T1 = time.time()
                pathencode = path.encode()
                evidencefilepathencode = evidencefilepath.encode()

                ret1 = lib.init_phase(pathencode, evidencefilepathencode, tau)
                data = ctypes.string_at(ret1, -1).decode("utf-8")
                # print("init phase output ",data)

                T2 = time.time()
                # print('init_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')

                T1 = time.time()
                challenge = "12345678901234567890123456789012"
                challengeencode = challenge.encode()
                ret2 = lib.challenge_phase(pathencode, evidencefilepathencode, challengeencode)
                challenge_data = ctypes.string_at(ret2, -1).decode("utf-8")
                # print("challenge phase output ", challenge_data)
                T2 = time.time()
                # print('challenge_phase running time:%sms' % ((T2 - T1) * 1000))

                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                challenge_dataencode = challenge_data.encode()

                T1 = time.time()
                ret3 = lib.verification_phase(pathencode, evidencefilepathencode, challenge_dataencode)
                verification_data = ctypes.string_at(ret3, -1).decode("utf-8")
                # print("verification phase output ", verification_data)
                T2 = time.time()
                # print('verification_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                fo.write('\n')
                fo.close()
        path = "./challenge-response protocol/data/700Mfile"
        evidencefilepath = "evidencefile.txt"
        for tau in [500, 5000, 10000, 50000, 100000, 300000, 500000, 1000000]:

            for x in range(10):
                fo = open("./challenge-response protocol/700Mfileoutcome.txt", "a+")
                fo.write("700M,")
                fo.write(str(tau))
                fo.write(',')

                T1 = time.time()
                pathencode = path.encode()
                evidencefilepathencode = evidencefilepath.encode()

                ret1 = lib.init_phase(pathencode, evidencefilepathencode, tau)
                data = ctypes.string_at(ret1, -1).decode("utf-8")
                # print("init phase output ",data)

                T2 = time.time()
                # print('init_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')

                T1 = time.time()
                challenge = "12345678901234567890123456789012"
                challengeencode = challenge.encode()
                ret2 = lib.challenge_phase(pathencode, evidencefilepathencode, challengeencode)
                challenge_data = ctypes.string_at(ret2, -1).decode("utf-8")
                # print("challenge phase output ", challenge_data)
                T2 = time.time()
                # print('challenge_phase running time:%sms' % ((T2 - T1) * 1000))

                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                challenge_dataencode = challenge_data.encode()

                T1 = time.time()
                ret3 = lib.verification_phase(pathencode, evidencefilepathencode, challenge_dataencode)
                verification_data = ctypes.string_at(ret3, -1).decode("utf-8")
                # print("verification phase output ", verification_data)
                T2 = time.time()
                # print('verification_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                fo.write('\n')
                fo.close()
        path = "./challenge-response protocol/data/1Gfile"
        evidencefilepath = "evidencefile.txt"
        for tau in [500, 5000, 10000, 50000, 100000, 300000, 500000, 1000000]:

            for x in range(10):
                fo = open("./challenge-response protocol/1Gfileoutcome.txt", "a+")
                fo.write("1G,")
                fo.write(str(tau))
                fo.write(',')
                T1 = time.time()
                pathencode = path.encode()
                evidencefilepathencode = evidencefilepath.encode()

                ret1 = lib.init_phase(pathencode, evidencefilepathencode, tau)
                data = ctypes.string_at(ret1, -1).decode("utf-8")
                # print("init phase output ",data)

                T2 = time.time()
                # print('init_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')

                T1 = time.time()
                challenge = "12345678901234567890123456789012"
                challengeencode = challenge.encode()
                ret2 = lib.challenge_phase(pathencode, evidencefilepathencode, challengeencode)
                challenge_data = ctypes.string_at(ret2, -1).decode("utf-8")
                # print("challenge phase output ", challenge_data)
                T2 = time.time()
                # print('challenge_phase running time:%sms' % ((T2 - T1) * 1000))

                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                challenge_dataencode = challenge_data.encode()

                T1 = time.time()
                ret3 = lib.verification_phase(pathencode, evidencefilepathencode, challenge_dataencode)
                verification_data = ctypes.string_at(ret3, -1).decode("utf-8")
                # print("verification phase output ", verification_data)
                T2 = time.time()
                # print('verification_phase running time:%sms' % ((T2 - T1) * 1000))
                fo.write(str(((T2 - T1) * 1000)))
                fo.write(',')
                fo.write('\n')
                fo.close()