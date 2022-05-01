
from ctypes import cdll

def test_vdf():
    print("test Wesolowski's VDF")
    # Load the shared library into ctypes
    lib = cdll.LoadLibrary('./libtest-vdf.so')
    ret1 = lib.test()
    print(ret1)

# def test_vdf():
#     print("test Wesolowski's VDF")
    