from ctypes import cdll

def vdf():
    lib = cdll.LoadLibrary('./libtest-vdf.so')
    ret1 = lib.test()
    print(ret1)


if __name__ == "__main__":
            print("main")
            vdf()
